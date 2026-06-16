# taiwan-freego-a11y

A [Claude Code](https://code.claude.com) **skill** that makes Claude apply Taiwan's
**《網站無障礙規範 2.0》**（≡ **WCAG 2.0 AA**）accessibility patterns — the rules the
government **Freego** scanner checks — whenever it writes, edits, or reviews web UI.

It enforces, by default:

- **Relative `font-size`** (rem/em/%/named, never px) — Freego `CS2140401C`
- **Labelled form controls** (`<label for>`+`id`, or `aria-label`) — Freego `HM1130104C`
- **Table header `scope`** + `<caption>` (empty corner = `<td>`) — Freego `HM1130101C`
- **AA colour contrast ≥ 4.5:1** (e.g. avoid Tailwind `gray-400` for muted text)
- ARIA patterns: page `<h1>`, `role="alert"` errors, `aria-hidden` decor, `aria-pressed` /
  `aria-expanded`, `inert` off-canvas, `lang` + zoomable viewport

Full rules: [`plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/SKILL.md`](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/SKILL.md).

---

## Install — Option A: as a plugin (recommended, auto-updates)

In Claude Code, add this repo as a marketplace, then install the plugin:

```text
/plugin marketplace add happyloa/taiwan-freego-a11y-skill
/plugin install taiwan-freego-a11y@happyloa-skills
```

(Replace `happyloa/taiwan-freego-a11y-skill` with your `owner/repo` if you fork it.)

Update later with:

```text
/plugin marketplace update
/plugin update taiwan-freego-a11y@happyloa-skills
```

## Install — Option B: copy the skill folder (simplest, no plugin)

```bash
git clone https://github.com/happyloa/taiwan-freego-a11y-skill.git
# personal (all projects):
cp -r taiwan-freego-a11y-skill/plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y ~/.claude/skills/
# or project-only: cp -r ... <your-project>/.claude/skills/
```

## Usage

Claude **auto-invokes** the skill based on its `description` whenever you work on web UI
(forms, tables, buttons, styling). You can also call it explicitly:

- Plugin install: `/taiwan-freego-a11y:taiwan-freego-a11y`
- Folder copy (Option B): `/taiwan-freego-a11y`

---

## Repository layout

```text
taiwan-freego-a11y-skill/
├── .claude-plugin/
│   └── marketplace.json                 # marketplace catalog (Option A)
├── plugins/
│   └── taiwan-freego-a11y/
│       ├── .claude-plugin/
│       │   └── plugin.json              # plugin manifest
│       ├── skills/
│       │   └── taiwan-freego-a11y/
│       │       └── SKILL.md             # the skill itself
│       └── README.md
├── README.md
└── LICENSE
```

## License

MIT — see [LICENSE](LICENSE).
