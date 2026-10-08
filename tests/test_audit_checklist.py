import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y"
spec = importlib.util.spec_from_file_location("audit", SKILL / "scripts/audit_checklist.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class AuditChecklistTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((SKILL / "references/coverage.json").read_text(encoding="utf-8"))

    def test_published_inventory_and_machine_identifiers(self):
        audit.validate_inventory(self.data)
        expected = {
            "CS2140401C", "CS3140800C", "CS3140801C", "CS3140802C",
            "HM1110100C", "HM1110101C", "HM1110103C", "HM1110104C", "HM1110105C", "HM1110106C",
            "HM1130100C", "HM1130101C", "HM1130102C", "HM1130103C", "HM1130104C", "HM1130105C",
            "HM1130200C", "HM1240102C", "HM1240200C", "HM1240400C", "HM1240401C",
            "HM1310100C", "ME1320200C", "HM1410200C", "HM1410201C", "HM2310200C",
            "HM3240900C", "HM3241000C",
        }
        self.assertEqual(expected, {c["id"] for c in self.data["codes"] if c["kind"] == "machine"})

    def test_cumulative_levels_and_deleted_parsing(self):
        for level, counts in [("A", (31, 21, 103)), ("AA", (55, 23, 161)), ("AAA", (86, 28, 216))]:
            result = audit.worksheet(self.data, level)
            self.assertEqual(counts, (len(result["criteria"]),
                                     sum(c["kind"] == "machine" for c in result["codes"]),
                                     sum(c["kind"] == "manual" for c in result["codes"])))
            self.assertNotIn("4.1.1", {c["id"] for c in result["criteria"]})
            self.assertTrue(all(c["status"] == "Pending" and c["evidence"] == ""
                                for c in result["criteria"] + result["codes"]))

    def test_new_aa_criteria_and_aaa_exclusions(self):
        result = audit.worksheet(self.data, "AA")
        ids = {c["id"] for c in result["criteria"]}
        self.assertTrue({"2.4.11", "2.5.7", "2.5.8", "3.2.6", "3.3.7", "3.3.8"} <= ids)
        self.assertTrue({"2.4.12", "2.4.13", "3.3.9", "2.5.5"}.isdisjoint(ids))

    def test_report_lookup_never_implies_pass(self):
        text = '<p>HM1130105C fails; HM1130105C repeated</p><p>HM3240900C CS2140400C HM1410100C HM1999900C</p>'
        result = audit.worksheet(self.data, "AA", text)
        lookup = result["report_code_lookup"]
        self.assertEqual(["HM1130105C", "HM3240900C"], lookup["recognized"])
        self.assertEqual(["HM3240900C"], lookup["outside_selected_level"])
        self.assertEqual(["CS2140400C", "HM1410100C", "HM1999900C"], lookup["unknown"])
        self.assertTrue(all(c["status"] == "Pending" for c in result["codes"]))

    def test_duplicate_missing_and_bad_mapping_rejected(self):
        for mutation in ["duplicate", "missing", "mapping", "removed", "guidance"]:
            data = copy.deepcopy(self.data)
            if mutation == "duplicate": data["codes"][-1] = data["codes"][0]
            if mutation == "missing": data["codes"].pop()
            if mutation == "mapping": data["codes"][0]["criterion"] = "1.1.1"
            if mutation == "removed": data["criteria"][-3]["status"] = "active"
            if mutation == "guidance": data["criteria"][0]["check"] = ""
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                audit.validate_inventory(data)

    def test_markdown_escapes_messages_and_preserves_every_row(self):
        data = copy.deepcopy(self.data)
        data["codes"][0]["message"] = '<input> | literal pipe'
        result = audit.worksheet(data, "AA")
        rendered = audit.markdown(result)
        self.assertIn('&lt;input&gt; \\| literal pipe', rendered)
        self.assertEqual(55 + 23 + 161, rendered.count('| Pending |'))


if __name__ == "__main__":
    unittest.main()
