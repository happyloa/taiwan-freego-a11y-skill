# Contributing

Take normative requirements and C/E identifiers from the official Taiwan documents.
Keep each code's source edition, exact identifier, full message, level, and PDF page.
See the [source notes](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/references/sources-and-versions.md).

## Local checks

Requires Node.js 22+ and Python 3.10+.

```bash
npm ci
npm run validate
npm test
npm run test:install
npm run test:browser
```

- `npm ci` installs the pinned Claude Code CLI; `allowScripts` in `package.json` lets its postinstall run under npm 12. Skill users need none of these packages.
- `test:install` uses a temporary Claude configuration and sends no model or API request.
- `test:browser` runs a local fixture with @sparticuz/chromium, which is Linux x64 only. Elsewhere, set `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH` to a compatible Chromium, such as the one from `npx playwright install chromium`. It does not run desktop Freego or a screen reader.
- On Windows the npm scripts call `python`. If that resolves to the Microsoft Store alias, turn the alias off under Settings → Apps → Advanced app settings → App execution aliases, or run `py -m unittest discover -s tests -v`.

## Behavior evals

`plugins/taiwan-freego-a11y/evals/` holds four `claude plugin eval` cases: repairing the checkout page, triaging a 110.07 Freego report, an audit-only login page, and edition and date questions. They run Claude on your own login and use model credit (about US$4 for the default two runs per case plus the no-plugin arm).

```bash
cd plugins/taiwan-freego-a11y
claude plugin eval . --trust-plugin --allow-tools Write Edit --judge-model sonnet --no-publish
```

By default each case also runs without the plugin and the report shows the difference; `--ablation none` runs only the plugin arm. Do not grant Bash: native Windows has no eval sandbox. Run the suite after changing `SKILL.md` or `references/`, and compare against the previous version with the same judge and run count. LLM judges are noisy: read a failed answer before changing the skill, and give a grader the facts it needs (such as the current Freego release) instead of expecting the judge to know them. Results in [docs/verification.md](docs/verification.md).

## Changes

- Keep the plugin, marketplace, and package versions in sync. Raise the plugin version whenever published skill content changes, so installed users receive it.
- When an official document or tool version changes, re-read the publication record, the full appendix, and the tool release notes. Keep the source edition and date with the inventory, and reconcile counts, code-to-criterion mappings, changed messages, the criterion checklist, source notes, and tests together. A new standard name alone is not an update, and a third-party rule inventory is never the authority.
- When checking AI behavior by hand, give a fresh agent the skill and a raw task artifact, without expected diagnoses or fixes. Report measured results apart from untested ones and record the model and runtime. The checked-in repair fixture is a regression example; passing it does not prove future answers correct.
