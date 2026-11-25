---
name: taiwan-freego-a11y
description: >-
  Apply Taiwan 網站無障礙規範 (115.11), aligned with WCAG 2.2, when building,
  editing, or reviewing web UI (HTML, JSX, Vue, Svelte, CSS), preparing an
  accessibility audit, or fixing a Freego report. Default to AA, include all
  applicable A requirements, use the complete official C/E code inventory,
  and distinguish automated evidence from keyboard, screen-reader, visual,
  media, and authentication checks.
---

# Taiwan Web Accessibility: 115.11 / WCAG 2.2

Target **《網站無障礙規範 (115.11)》 AA** unless the user names A or AAA. Apply the
rules while coding; do not wait for a report.

For development or remediation, edit the project files and verify the result. For an
audit-only request, leave the source unchanged and report evidence with concrete
fixes. Use the text after the slash command to pick pages, components, or a report.
Resolve bundled files relative to this skill directory. If they are missing, report a
broken installation; never create `references/` or `scripts/` in the user's project.

## Edition and certification dates

- 115.11 was published on 2026-05-29. Certification under it starts on
  **2026-11-30**, when MODA stops accepting 110.07 applications. Badges issued
  through 2026-11-29 stay valid for three years.
- Use 115.11 for new work now, but do not describe it as in effect before 2026-11-30.
- As of 2026-11-25 the only official Freego release (Dec 19 2025) targets 110.07.
  Check the download area for a newer edition before relying on a report, and never
  invent a version.
- Freego is one source of evidence, not a certification.

## Load what the task needs

The rules in this file cover most implementation work. Also read:

- [sources-and-versions.md](references/sources-and-versions.md) for editions, dates,
  Freego versions, or any code taken from a report.
- [machine-checks.md](references/machine-checks.md) (all **28 C codes**) when fixing or
  explaining a C code.
- [criteria-checklist.md](references/criteria-checklist.md) (all **86 active
  criteria**; AA covers **31 A + 24 AA = 55**) plus machine-checks.md for an audit,
  worksheet, or full-scope review. A full audit uses the whole selected-level
  inventory: every applicable criterion and C/E code.
- [coverage.json](references/coverage.json) for an E code or the official wording of
  any code: 216 E codes with message, criterion, level, and PDF page. Search it, for
  example `rg -n 'HM1130105C' "${CLAUDE_SKILL_DIR}/references/coverage.json"`; do not
  read the whole file.
- [verification-and-reporting.md](references/verification-and-reporting.md) before
  reporting test results or statuses.

Generate the complete AA worksheet of **pending checks** (not a website scan):

```bash
python "${CLAUDE_SKILL_DIR}/scripts/audit_checklist.py" --level AA --output a11y-audit.md
```

Use `python3` or `py` where `python` is unavailable; the output is UTF-8. Add
`--format json` for structured evidence or `--report freego-report.html` to list known
and unknown codes in an exported report. Recognizing a code is never a pass.

## Workflow

1. Settle the level and the pages, routes, states, languages, downloads, third-party
   content, and complete processes in scope.
2. Inspect shared components and rendered HTML as well as source: login, dialogs,
   validation errors, empty/loading states, menus, filters, SPA route changes, mobile
   layouts, and themes.
3. Apply the relevant criteria and C/E messages. Sufficient techniques are
   alternatives, not a list to implement together; mark one not applicable only with a
   reason and the method used instead. An `FA...` code is a failure to check for.
4. Repair shared components at their source, keep the intended design and behavior,
   and inspect the pages that use them.
5. Run available build/lint and automated checks, then the relevant keyboard,
   screen-reader, visual, media, and process checks.
6. Re-test the same states. Report tested evidence, failures, justified exclusions,
   and untested checks separately; leave unavailable tests Pending.

## Rules that are easy to get wrong

### Images and media (1.1, 1.2)

- Informative images and image buttons need meaningful `alt`; linked image-map areas
  need a purpose. Decorative images use `alt=""` **without `title`** (HM1110106C).
  Hide an icon from AT only when it is decorative or its information is already there.
- Give SVG, canvas, charts, and objects text equivalents, with detailed descriptions or
  data nearby for complex graphics. Do not introduce obsolete `longdesc`.
- Check captions, transcripts, and audio descriptions for accuracy and timing, not
  only the presence of `<track>`.
- A CAPTCHA needs its purpose and an equivalent alternative; also apply 3.3.8/3.3.9.

### Structure, tables, and forms (1.3, 3.3, 4.1.2)

- Mark real headings in meaningful nesting order. Prefer one page `h1`, but "exactly
  one h1" is not a WCAG rule. Keep heading levels configurable in reusable cards;
  accordions use `<h2><button aria-expanded="false" aria-controls="panel">…</button></h2>`.
- Tables: `scope` for suitable headers (HM1130101C); unique `id` plus `headers` for
  complex tables (HM1130102C). Valid `headers`/`id` associations do not also need
  `scope`. Give data tables a caption where needed, use `td` for an empty corner, and
  never add header or caption semantics to a layout table.
- Prefer a visible `<label for>` with a unique `id`. Wrapping labels work, but check
  Freego compatibility. An ARIA-only name can satisfy the accessible name and still
  fail HM1130104C; never promise that `aria-label` alone passes it.
- Group related radios/checkboxes with `fieldset` and a non-empty `legend` as its first
  child (HM1130105C). Group meaningful select options with labelled `optgroup`
  (HM1130103C). Do not turn button toolbars into fieldsets.
- Use correct `autocomplete` tokens, visible required/format instructions, and keep
  user input after validation errors. Accessible names include the visible label (2.5.3).
- Keep reading and focus order meaningful when CSS reorders content; mark language
  changes and mixed text direction.

**115.11 code mapping:** HM1130101C table scope; HM1130102C table headers/id;
HM1130103C select/optgroup; HM1130104C labels/title; HM1130105C fieldset/legend.
Reports from the current 110.07 Freego (Dec 19 2025) use **HM1130103C for
fieldset/legend**, the check 115.11 numbers HM1130105C: fix a missing legend there,
not optgroup. For any report, read its edition and full message before mapping a code.

### Presentation (1.4)

- CS2140401C: use relative `font-size` (rem/em/%/named) in inline, generated,
  imported, and relevant third-party CSS. Units alone do not prove 200% text resize or
  reflow; do not assume a 16px base or that every utility token is rem.
- Measure actual contrast, including transparency, gradients, images,
  hover/focus/disabled states, and themes: 4.5:1 for normal text, 3:1 for large text
  (at least 24 CSS px, or about 18.67 CSS px bold), and 3:1 for control, state, and
  graphic information. Never rely on colour alone.
- Reflow at 320 CSS px width (or 256 CSS px height for horizontal content); confine
  genuinely two-dimensional tables and maps to their own region.
- Survive user text spacing without loss: line height 1.5, paragraph spacing 2em,
  letter spacing .12em (**.14em for Chinese**), word spacing .16em.
- Avoid images of text. Make hover/focus popovers dismissible, hoverable, and
  persistent. Do not lock orientation or disable zoom; give controls for autoplay audio
  and moving or updating content.

### Keyboard, navigation, and focus (2.1–2.4)

- Operate everything by keyboard with component-appropriate keys and no traps. Keep
  focus visible and order meaningful; avoid positive `tabindex`.
- Provide a working skip link, landmarks, distinguishable multiple `nav` regions,
  descriptive titles (updated on SPA navigation), clear link purpose, and multiple
  ways to find pages where required.
- Dialogs and drawers: set initial focus, contain it when modal, allow dismissal, and
  return focus. Make closed content hidden or inert. `aria-hidden` does not remove
  focusable descendants from the tab order; never hide a subtree holding focus.
- No context change on focus or input without warning. Single-character shortcuts must
  be disableable, remappable, or focus-only. Time limits are adjustable under 2.2.1;
  moving and auto-updating content can be paused, stopped, or hidden. Reduced-motion
  support alone does not prove the flash thresholds.

### New in 115.11

| Criterion | Level | Implementation and verification                                                                                                                                                       |
| --------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.4.11    | AA    | Author-created sticky headers, cookie banners, footers, and dialogs must not **fully** cover the focused component. Tab through them at zoom and small viewports.                     |
| 2.4.12    | AAA   | **No part** of the focused component may be obscured; keep this stricter rule apart from AA.                                                                                          |
| 2.4.13    | AAA   | Focus indicator area at least a 2 CSS px perimeter and 3:1 focused/unfocused contrast at the same pixels, with the stated exceptions.                                                 |
| 2.5.7     | AA    | Give dragging a single-pointer alternative such as click-select/click-place or move buttons. Keyboard support alone does not satisfy it.                                              |
| 2.5.8     | AA    | Targets at least 24×24 CSS px, or a documented exception; check the 24px-circle spacing rule for undersized targets.                                                                  |
| 3.2.6     | A     | Keep repeated help mechanisms in the same relative order across pages; it does not require adding help everywhere.                                                                    |
| 3.3.7     | A     | Auto-fill or offer information already given in the same process, apart from essential, security, or no-longer-valid exceptions.                                                      |
| 3.3.8     | AA    | No unsupported cognitive test at any authentication step: allow password managers, copy/paste, and assisted code entry, or give a qualifying alternative. Assess CAPTCHA and MFA too. |
| 3.3.9     | AAA   | The stricter rule: the object-recognition and personal-content exceptions do not apply.                                                                                               |

Use `scroll-padding`/`scroll-margin` where appropriate and test real focus behavior.
Do not substitute 44×44 (AAA 2.5.5) for the AA target rule, or require AAA focus
geometry for AA.

### Feedback, downloads, and robustness

- Associate error text with its field, set `aria-invalid`, and suggest corrections.
  Give review, confirmation, or reversal for sensitive submissions.
- Announce non-urgent status with `role="status"` or another polite live region, urgent
  errors with `role="alert"`, and sequences with `role="log"`; do not make every
  message assertive.
- ME1320200C: offer downloads in open formats (ODF, accessible PDF, HTML) and check the
  document itself; a PDF extension proves nothing.
- Give each `iframe` a descriptive non-empty `title` and assess the embedded content.
- 4.1.1 is removed in 115.11. Still fix duplicate IDs and broken references when they
  break names, relationships, states, or behavior, and report them under the active
  criterion instead of reviving 4.1.1.

## Scanner and evidence boundaries

Inspect authenticated and hidden states explicitly. Check what a flagged URL actually
serves: redirects, trailing-slash variants, proxy errors, HTTP status, loaded CSS, and
the rendered DOM. Never mark missing or blocked pages or timeouts as passes. Never add
`aria-hidden` or exclude pages just to silence Freego. Use
[verification-and-reporting.md](references/verification-and-reporting.md) for the
evidence format and the difference between code coverage and runtime results.
