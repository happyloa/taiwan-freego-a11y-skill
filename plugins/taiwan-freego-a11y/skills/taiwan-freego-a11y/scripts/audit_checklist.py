#!/usr/bin/env python3
"""Generate pending 115.11 checks and recognize report codes; never scan a site."""

import argparse
import html
import json
import re
import sys
from collections import Counter
from pathlib import Path

LEVELS = {"A": 1, "AA": 2, "AAA": 3}
CODE_RE = re.compile(r"\b(?:AR|SC|CS|FA|FL|GN|HM|ME|PD|SV|SL|SM|TX)\d{7}[CE]\b")
INVENTORY = Path(__file__).resolve().parents[1] / "references" / "coverage.json"


def validate_inventory(data):
    """Reject missing, duplicated, or inconsistent catalog entries."""
    if data.get("standard") != "Taiwan 115.11" or data.get("schema_version") != 1:
        raise ValueError("Expected schema 1, Taiwan 115.11 inventory")
    criteria = data["criteria"]
    codes = data["codes"]
    criterion_ids = {item["id"] for item in criteria}
    if len(criteria) != 87 or len(criterion_ids) != 87:
        raise ValueError("Expected 87 unique criterion entries")
    active = [item for item in criteria if item["status"] == "active"]
    removed = [item["id"] for item in criteria if item["status"] == "removed"]
    if removed != ["4.1.1"] or len(active) != 86:
        raise ValueError("Only 4.1.1 is removed; expected 86 active criteria")
    if Counter(item["level"] for item in active) != {"A": 31, "AA": 24, "AAA": 31}:
        raise ValueError("Active criterion levels differ from the verified source")
    for item in criteria:
        if not item.get("check") or not item.get("title"):
            raise ValueError(f"Missing criterion guidance: {item['id']}")
    if len(codes) != 244 or len({item["id"] for item in codes}) != 244:
        raise ValueError("Expected 244 unique C/E codes")
    expected = {
        ("machine", "A"): 21, ("machine", "AA"): 2, ("machine", "AAA"): 5,
        ("manual", "A"): 103, ("manual", "AA"): 58, ("manual", "AAA"): 55,
    }
    if Counter((item["kind"], item["level"]) for item in codes) != expected:
        raise ValueError("C/E level counts differ from the verified appendix")
    for item in codes:
        identifier = item["id"]
        if not CODE_RE.fullmatch(identifier):
            raise ValueError(f"Invalid code: {identifier}")
        criterion = f"{identifier[3]}.{identifier[4]}.{int(identifier[5:7])}"
        kind = "machine" if identifier.endswith("C") else "manual"
        if (item["criterion"] != criterion or item["criterion"] not in criterion_ids
                or item["criterion"] == "4.1.1" or item["kind"] != kind
                or item["level"] != ["", "A", "AA", "AAA"][int(identifier[2])]):
            raise ValueError(f"Inconsistent code mapping: {identifier}")
        if not item.get("message") or not 49 <= item.get("source_page", 0) <= 64:
            raise ValueError(f"Missing code message/provenance: {identifier}")
    # Preserve appendix code levels even where a linked criterion has another level.
    # Do not silently rewrite normative identifiers or their source classifications.
    return data


def report_codes(text, data, level):
    index = {item["id"]: item for item in data["codes"]}
    observed = sorted(set(CODE_RE.findall(html.unescape(text))))
    return {
        "recognized": [identifier for identifier in observed if identifier in index],
        "outside_selected_level": [identifier for identifier in observed
                                   if identifier in index
                                   and LEVELS[index[identifier]["level"]] > LEVELS[level]],
        "unknown": [identifier for identifier in observed if identifier not in index],
        "note": "Code recognition only; no report outcome or website pass is inferred.",
    }


def worksheet(data, level, report_text=None):
    limit = LEVELS[level]
    criteria = [dict(item, status="Pending", evidence="") for item in data["criteria"]
                if item["status"] == "active" and LEVELS[item["level"]] <= limit]
    codes = [dict(item, status="Pending", evidence="") for item in data["codes"]
             if LEVELS[item["level"]] <= limit]
    result = {
        "standard": data["standard"], "target_level": level,
        "effective_on": data["effective_on"], "inventory_verified_on": data["verified_on"],
        "note": "Pending worksheet only. No website, scanner, or screen-reader test has run.",
        "criteria": criteria, "codes": codes,
    }
    if report_text is not None:
        result["report_code_lookup"] = report_codes(report_text, data, level)
    return result


def cell(value):
    return html.escape(str(value), quote=False).replace("|", "\\|").replace("\n", " ")


def markdown(result):
    lines = [f"# {result['standard']} {result['target_level']} audit worksheet", "",
             result["note"], "", "Record page/state, method, date, evidence, and result for each applicable check.",
             "Use Pass / Fail / Pending / Not applicable; explain exceptions and alternative techniques.",
             "FA codes describe failures to investigate, not techniques to implement.", "",
             f"Scope: {len(result['criteria'])} active criteria; "
             f"{sum(c['kind'] == 'machine' for c in result['codes'])} C codes; "
             f"{sum(c['kind'] == 'manual' for c in result['codes'])} E codes.", "",
             "## Criteria", "", "| Criterion | Level | Check | Status | Evidence |",
             "| --- | --- | --- | --- | --- |"]
    for item in result["criteria"]:
        lines.append(f"| {cell(item['id'] + ' ' + item['title'])} | {item['level']} | "
                     f"{cell(item['check'])} | Pending | |")
    for kind, title in [("machine", "C codes"), ("manual", "E codes")]:
        lines += ["", f"## {title}", "", "| Code | Criterion | Level | Official message | Status | Evidence |",
                  "| --- | --- | --- | --- | --- | --- |"]
        for item in result["codes"]:
            if item["kind"] == kind:
                lines.append(f"| {item['id']} | {item['criterion']} | {item['level']} | "
                             f"{cell(item['message'])} | Pending | |")
    if "report_code_lookup" in result:
        lookup = result["report_code_lookup"]
        lines += ["", "## Report code lookup", "", lookup["note"]]
        for key in ["recognized", "outside_selected_level", "unknown"]:
            lines.append(f"- {key}: {', '.join(lookup[key]) or '(none)'}")
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--level", choices=LEVELS, default="AA")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    parser.add_argument("--report", type=Path, help="UTF-8 text/HTML report for code recognition only")
    parser.add_argument("--validate", action="store_true", help="Validate the bundled catalog and exit")
    args = parser.parse_args(argv)
    try:
        data = validate_inventory(json.loads(INVENTORY.read_text(encoding="utf-8")))
        if args.validate:
            print("Valid: 86 active criteria, 28 C codes, 216 E codes; 4.1.1 removed.")
            return 0
        report_text = args.report.read_text(encoding="utf-8-sig") if args.report else None
        result = worksheet(data, args.level, report_text)
        print(json.dumps(result, ensure_ascii=False, indent=2) if args.format == "json"
              else markdown(result), end="\n" if args.format == "json" else "")
        return 0
    except (ValueError, OSError, KeyError, TypeError, IndexError) as exc:
        print(f"Cannot generate checklist: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
