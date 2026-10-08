"""Exercise official Claude CLI installation without a model/API request."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = "taiwan-freego-a11y@happyloa-skills"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", default=str(ROOT), help="Local marketplace or GitHub owner/repo")
    args = parser.parse_args()
    claude = shutil.which("claude")
    if not claude:
        raise SystemExit("Claude CLI missing: run npm ci, then npm run test:install")
    with tempfile.TemporaryDirectory(prefix="freego-install-") as directory:
        env = {**os.environ, "CLAUDE_CONFIG_DIR": directory,
               "CLAUDE_CODE_PLUGIN_PREFER_HTTPS": "1", "GIT_TERMINAL_PROMPT": "0"}

        def run(*arguments):
            result = subprocess.run([claude, *arguments], env=env, text=True,
                                    capture_output=True, timeout=180, check=True)
            print(result.stdout.strip())
            return result.stdout

        run("plugin", "validate", str(ROOT), "--strict")
        run("plugin", "validate", str(ROOT / "plugins/taiwan-freego-a11y"), "--strict")
        run("plugin", "marketplace", "add", args.source)
        run("plugin", "install", PLUGIN, "--scope", "user", "--json")
        installs = json.loads(run("plugin", "list", "--json"))
        installed = next(item for item in installs if item["id"] == PLUGIN)
        assert installed["enabled"] is True, "Plugin is not enabled"
        cache = Path(installed["installPath"])
        manifest = json.loads((ROOT / "plugins/taiwan-freego-a11y/.claude-plugin/plugin.json").read_text())
        assert installed["version"] == manifest["version"], "Installed version differs"
        original = ROOT / "plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y"
        skill = cache / "skills/taiwan-freego-a11y"
        required = [original / "SKILL.md", *(original / "references").glob("*"),
                    original / "scripts/audit_checklist.py"]
        for path in required:
            copied = skill / path.relative_to(original)
            assert copied.is_file(), f"Missing installed resource: {copied}"
            assert hashlib.sha256(path.read_bytes()).digest() == hashlib.sha256(copied.read_bytes()).digest(), path
        details = run("plugin", "details", PLUGIN)
        assert "Skills (1)" in details and "taiwan-freego-a11y" in details, "Skill not discovered"
        subprocess.run([shutil.which("python") or "python3", str(skill / "scripts/audit_checklist.py"),
                        "--validate"], check=True)
        print(f"Installation verified: {installed['version']}, {len(required)} identical skill resources.")


if __name__ == "__main__":
    main()
