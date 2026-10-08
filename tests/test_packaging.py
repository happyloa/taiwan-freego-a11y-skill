import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y"


class PackagingTests(unittest.TestCase):
    def test_manifest_identity_versions_and_paths(self):
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        plugin = json.loads((ROOT / "plugins/taiwan-freego-a11y/.claude-plugin/plugin.json").read_text())
        package = json.loads((ROOT / "package.json").read_text())
        entry = marketplace["plugins"][0]
        self.assertEqual("happyloa-skills", marketplace["name"])
        self.assertEqual("taiwan-freego-a11y", plugin["name"])
        self.assertEqual(plugin["name"], entry["name"])
        self.assertEqual(plugin["version"], entry["version"])
        self.assertEqual(plugin["version"], package["version"])
        self.assertTrue((ROOT / entry["source"] / "skills/taiwan-freego-a11y/SKILL.md").is_file())

    def test_bundled_resources_and_frontmatter(self):
        content = (SKILL / "SKILL.md").read_text()
        self.assertTrue(content.startswith("---\nname: taiwan-freego-a11y\ndescription:"))
        for name in ["coverage.json", "criteria-checklist.md", "machine-checks.md",
                     "sources-and-versions.md", "verification-and-reporting.md"]:
            self.assertTrue((SKILL / "references" / name).is_file())
            self.assertIn("references/" + name, content)
        self.assertIn("${CLAUDE_SKILL_DIR}", content)
        self.assertTrue((SKILL / "scripts/audit_checklist.py").is_file())

    def test_relative_document_links(self):
        for path in ROOT.rglob("*.md"):
            if any(part in {"node_modules", ".git", "test-results", "playwright-report"} for part in path.parts):
                continue
            for target in re.findall(r"\]\(([^\s)]+)\)", path.read_text()):
                if not target.startswith(("https:", "http:", "#")):
                    self.assertTrue((path.parent / target.split("#")[0]).exists(), (path, target))

    def test_published_guides_cover_catalog_rows(self):
        data = json.loads((SKILL / "references/coverage.json").read_text())
        criteria = (SKILL / "references/criteria-checklist.md").read_text()
        rows = re.findall(r"^\| (\d\.\d\.\d+) ", criteria, re.MULTILINE)
        self.assertEqual({c["id"] for c in data["criteria"]}, set(rows))
        self.assertEqual(87, len(rows))
        machine = (SKILL / "references/machine-checks.md").read_text()
        codes = re.findall(r"^\| ([A-Z]{2}\d{7}C) \|", machine, re.MULTILINE)
        self.assertEqual({c["id"] for c in data["codes"] if c["kind"] == "machine"}, set(codes))
        self.assertEqual(28, len(codes))


if __name__ == "__main__":
    unittest.main()
