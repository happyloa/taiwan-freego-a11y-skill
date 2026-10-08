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

# Taiwan Web Accessibility — 115.11 / WCAG 2.2

Target **《網站無障礙規範 (115.11)》 AA** unless the user specifies A or AAA.
Apply the rules while coding; do not wait for a report.

The revised standard was published on 2026-05-29 and takes effect for certification
on **2026-11-30**. Use it now for new work. Do not describe it as already in effect
before that date. Treat Freego as one source of evidence, not a complete accessibility
certification.

## Load the complete scope

1. Read [sources-and-versions.md](references/sources-and-versions.md) for authority,
   version selection, changed codes, and the removed 4.1.1 criterion.
2. Read [criteria-checklist.md](references/criteria-checklist.md). It covers all
   **86 active criteria**; AA includes **31 A + 24 AA = 55**.
3. Read [machine-checks.md](references/machine-checks.md) for all **28 C codes**.
4. Look up every applicable **E code** in [coverage.json](references/coverage.json):
   it includes **216 E codes**, their official messages, criterion, level, and
   source page. Use the entire selected-level inventory for a full audit. Follow
   each relevant message, including the documented failure conditions.
5. Read [verification-and-reporting.md](references/verification-and-reporting.md)
   before reporting results.

Find a code with `rg -n 'HM1130105C' <skill-dir>/references/coverage.json`.
Generate the complete AA worksheet with:

```bash
python <skill-dir>/scripts/audit_checklist.py --level AA > a11y-audit.md
```

This generates **pending checks**, not a website scan. Use `--format json` for
structured evidence or `--report freego-report.html` to list known and unknown
codes in an exported text/HTML report. Never treat code recognition as a pass.

## Workflow

1. Establish the target level and the pages, routes, states, languages, downloads,
   third-party content, and complete processes in scope. Default to 115.11 AA.
2. Inspect shared components and rendered HTML as well as source. Include login,
   create/edit dialogs, validation errors, empty/loading states, menus, filters,
   SPA route changes, mobile layouts, and light/dark themes.
3. Apply the relevant criteria and C/E messages. Mark an alternative technique
   not applicable only with a reason and the method used instead. A list of
   sufficient techniques does not require implementing every technique together.
   A `FA...` code describes a failure: check whether that failure occurs.
4. Repair shared components at their source and inspect their consuming pages.
   Preserve intended visual design and behavior while adding semantics.
5. Run available build/lint and automated accessibility checks, then execute the
   relevant keyboard, screen-reader, visual, media, and process checks.
6. Re-run the same states after fixes. Report tested evidence, failures, justified
   exclusions, and untested checks separately. Leave unavailable tests pending.

## Core implementation rules

### Non-text content and media — 1.1, 1.2

- Provide meaningful `alt` for informative images and image submit buttons, and
  non-empty purpose descriptions for linked image-map areas.
- Use `alt=""` without `title` for decorative images. Hide an icon from AT only
  when its information is already available or it is decorative.
- Give SVG, canvas, charts, embedded objects, and sensory experiences appropriate
  text equivalents. Offer nearby detailed descriptions or accessible data for
  complex diagrams; do not introduce obsolete `longdesc` as a new requirement.
- Provide accurate transcripts, captions, and audio descriptions at the selected
  level. Check their information and timing, not only the presence of `<track>`.
- Provide CAPTCHA purpose and equivalent alternatives; additionally apply the
  authentication requirements in 3.3.8/3.3.9.

### Structure, tables, and forms — 1.3.1, 1.3.2, 3.3, 4.1.2

- Mark genuine headings with `h1`–`h6` in meaningful nesting order. Prefer one
  page-level `h1`; do not claim that exactly one is an independent WCAG rule.
  A list item may contain a heading. Decide from meaning, not font weight.
- Keep heading level configurable in reusable cards. For accordions, use
  `<h2><button aria-expanded="false" aria-controls="panel">…</button></h2>`.
- Use `scope="col|row|colgroup|rowgroup"` for suitable table headers. Use unique
  `id` and explicit `headers` associations for complex tables. Do not require
  scope when valid headers/id associations provide the relationship.
- Give data tables a useful caption or other programmatic identification where
  needed. Use `td` for a genuinely empty corner. Avoid tables for layout; do not
  add header/caption semantics to an existing layout table.
- Prefer visible `<label for>` + unique `id` for input/select/textarea. Support
  wrapping labels, but verify exact Freego compatibility. An ARIA-only name can
  satisfy accessible-name requirements while failing a structural scanner rule.
  Do not promise that `aria-label` alone passes HM1130104C.
- Group related radio/checkbox controls with `fieldset` and a non-empty
  `legend` as the first child element. Use labelled `optgroup` for meaningful
  select groups. Do not turn arbitrary button toolbars into fieldsets.
- Use correct `autocomplete` tokens for user-information fields. Include visible
  required/format instructions and preserve user input after validation errors.
- Match accessible names to visible labels (2.5.3). Prefer native buttons/links
  and expose custom roles, values, states, and changes correctly.
- Keep reading and focus order meaningful; CSS visual reordering must not create
  a conflicting sequence. Mark language changes and mixed text direction.

**115.11 code mapping:** HM1130101C = table scope; HM1130102C = table headers/id;
HM1130103C = select/optgroup; HM1130104C = labels/title;
HM1130105C = fieldset/legend. Never apply the old skill's legend mapping to
HM1130103C. For an older report, inspect its version and full message first.

### Presentation — 1.4

- Use relative `font-size` (rem/em/%/named) for CS2140401C, including inline
  styles, generated CSS, imported stylesheets, and relevant third-party styles.
  Test 200% text resizing and reflow; changing units alone does not prove either.
  Do not assume every browser's base font is 16px or every utility token is rem.
- Calculate actual foreground/background contrast, including transparency,
  gradients, images, hover/focus/disabled states, and themes. AA normal text
  requires 4.5:1; large text requires 3:1. Large means at least 18pt (24 CSS px)
  regular or 14pt (about 18.67 CSS px) bold. Respect specified exceptions.
- Give relevant controls, states, and graphics 3:1 non-text contrast. Do not rely
  on color alone for errors, links, selections, or chart series.
- Allow zoom and reflow at 320 CSS px width for vertically scrolling content, or
  256 CSS px height for horizontally scrolling content. Confine legitimately
  two-dimensional tables/maps to their own region.
- Permit user text spacing without clipping or loss: line height 1.5, paragraph
  spacing 2em, letter spacing .12em (.14em for Chinese), word spacing .16em;
  observe the Taiwan language-specific notes.
- Avoid images of text where real text works. Keep hover/focus popovers
  dismissible, hoverable, and persistent under the criterion's conditions.
- Do not lock orientation or disable browser zoom. Provide controls for
  applicable autoplay audio and moving/updating content.

### Keyboard, navigation, and focus — 2.1–2.4

- Operate all functionality using the keyboard, with meaningful Tab/Shift+Tab,
  Enter/Space, and component-appropriate arrow/Escape behavior; avoid traps.
- Keep visible focus and meaningful order; avoid positive `tabindex`.
  Offer a working skip link, landmarks, grouped `nav`, descriptive page titles,
  understandable link purposes, and multiple ways to locate pages where required.
- Update the document title on SPA navigation and manage focus according to the
  new content and user action.
- Manage dialogs/drawers through opening focus, containment when modal, dismissal,
  and return focus. Make closed content hidden/inert as appropriate.
  `aria-hidden` alone does not remove descendants from the tab order; never hide
  a subtree containing the current focus.
- Do not change context merely on focus/input without the required warning.
  Make single-character shortcuts disableable, remappable, or focus-specific.
- Make time limits adjustable under 2.2.1; warn and offer extension where used.
  Pause/stop/hide applicable moving content and control auto-update frequency.
  Test flashing thresholds; animation preferences alone do not prove compliance.

### New 115.11 requirements

| Criterion | Level | Implementation and verification |
| --- | --- | --- |
| 2.4.11 | AA | Ensure author-created sticky headers, cookie banners, footers, and dialogs do not **fully** cover the focused component. Tab through them at zoom and small viewports. |
| 2.4.12 | AAA | Ensure **no part** of the focused component is obscured; distinguish this stricter requirement from AA. |
| 2.4.13 | AAA | Provide a focus indicator with area at least that of a 2 CSS px perimeter and 3:1 focused/unfocused contrast at the same pixels, subject to the stated exceptions. |
| 2.5.7 | AA | Supply a single-pointer alternative to dragging, such as click-select/click-place or move buttons. Keyboard support alone does not satisfy this pointer requirement. |
| 2.5.8 | AA | Provide 24×24 CSS px pointer targets or meet a documented exception; check the 24px-diameter circle spacing rule for undersized targets. |
| 3.2.6 | A | Keep repeated help mechanisms in consistent relative order across pages; do not invent a requirement to add a help mechanism everywhere. |
| 3.3.7 | A | Auto-fill or let users select information already supplied within the same process, subject to essential/security/invalid-data exceptions. |
| 3.3.8 | AA | Avoid unsupported cognitive tests at every authentication step; allow password managers, copy/paste, and assisted code entry, or provide a qualifying alternative. Assess CAPTCHA and MFA too. |
| 3.3.9 | AAA | Apply the stricter authentication requirement; object recognition/personal-content exceptions from AA do not apply. |

Use `scroll-padding`/`scroll-margin` where appropriate and test real focus
behavior. Do not substitute 44×44 AAA target sizing for the AA rule, or impose
AAA focus geometry as an AA prerequisite. See the criterion checklist for exceptions.

### Feedback, downloads, and robust interaction

- Associate error text with its field, set `aria-invalid` when invalid, and give
  useful corrections. Provide review/confirmation/reversal for sensitive submissions.
- Announce nonurgent status changes with `role="status"` or a suitable polite live
  region; use `role="alert"` for urgent errors and `role="log"` for sequential
  updates. Avoid adding redundant assertive announcements to every message.
- Provide open download formats (ME1320200C) and verify the accessibility of the
  document itself. A PDF extension alone is insufficient.
- Give iframes descriptive non-empty titles and assess embedded/third-party content.
- Treat 4.1.1 as removed in 115.11. Continue fixing duplicate IDs/broken references
  when they break actual names, relationships, states, or behavior; attribute the
  failure to the relevant active criterion rather than resurrecting 4.1.1.

## Scanner and evidence boundaries

Inspect authenticated and hidden states explicitly. Verify what a flagged URL
actually serves, including redirects, trailing-slash variants, proxy errors,
HTTP status, loaded CSS, and the rendered DOM.

Do not mark missing/blocked pages or timeouts as passes. Do not add `aria-hidden`
or exclude pages simply to suppress Freego findings. Use
[verification-and-reporting.md](references/verification-and-reporting.md) for the
final evidence format and the distinction between code coverage and runtime results.
