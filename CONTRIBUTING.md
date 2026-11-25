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

## Changes

- Keep the plugin, marketplace, and package versions in sync. Raise the plugin version whenever published skill content changes, so installed users receive it.
- For a normative update, reconcile the inventory, criterion checklist, source notes, counts, and tests together; a new standard name alone is not an update.
- To check AI behavior, give a fresh agent the skill and a raw task artifact, without expected diagnoses or fixes. Report measured results apart from untested ones and record the model and runtime. The checked-in repair fixture is a regression example; passing it does not prove future answers correct.
