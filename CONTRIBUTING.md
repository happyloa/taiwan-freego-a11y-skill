# Contributing

Use official Taiwan documents for normative requirements and C/E identifiers.
Preserve source edition, exact code, full message, level, and PDF page. See the
[source notes](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/references/sources-and-versions.md).

For local development, install Node.js 22+ and Python 3.10+, then run:

```bash
npm ci
npm run validate
npm test
npm run test:install
npm run test:browser
```

Development dependencies are optional for skill users. The installation test uses
a temporary Claude configuration; it makes no model/API request. Browser tests
exercise a local fixture and do not launch desktop Freego or a screen reader.

Keep plugin, marketplace, and package versions synchronized. Increment the plugin
version when published skill content changes so installed users can receive it.
For normative updates, reconcile the entire inventory, criterion checklist, source
notes, counts, and tests; never replace only the standard name.

When validating AI behavior, give a fresh agent the skill and a raw task artifact.
Do not provide expected diagnoses or fixes. Keep measured results separate from
untested outcomes, and record the model/runtime used. The checked-in repair fixture
is a regression example; passing it does not prove every future AI answer is correct.
