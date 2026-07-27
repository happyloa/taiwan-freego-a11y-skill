---
name: taiwan-freego-a11y
description: >-
  Apply Taiwan 網站無障礙規範 2.0 / WCAG 2.0 AA accessibility patterns when writing,
  editing, or reviewing web UI (HTML/JSX/Vue/Svelte/etc.). Use whenever building or
  changing forms, tables, buttons, navigation, or styling. Enforces relative font-size,
  labelled form controls, table header scope, AA colour contrast, and ARIA patterns that
  the Taiwan government Freego scanner checks.
---

# Taiwan Web Accessibility (WCAG 2.0 AA / Freego)

Use this whenever you write, edit, or review web UI that must conform to Taiwan's
**《網站無障礙規範 2.0》** (equivalent to **WCAG 2.0 AA**) — the standard verified by the
government **Freego** scanner. Apply the checklist **proactively**; do not wait for a scan
report.

## Checklist

### 1. Font size must use relative units — Freego `CS2140401C`
Never set `font-size` in `px`. Use `rem`, `em`, `%`, or a named size (`small`/`medium`/`large`…).
A root font-size set in `rem` is relative to the browser default (16px), so `1.125rem` == 18px
with **no visual change** but it passes.

```css
/* ❌ */ html { font-size: 18px; }        /* ❌ */ style="font-size: 18px"
/* ✅ */ html { font-size: 1.125rem; }     /* ✅ */ class="text-sm"  /* Tailwind text-* are rem */
```

### 2. Every form control needs an accessible name — Freego `HM1130104C`
`input`, `select`, and `textarea` must have a programmatic label.

- Prefer a visible `<label for="x">` paired with the control's `id="x"`.
- Otherwise use `aria-label` (or `title`).
- Watch dynamically generated fields (`.map()`/loops) — give each a **unique** `id`.
- Icon-only buttons and bare search inputs need `aria-label`.

```html
<label for="dept">部會</label>
<select id="dept">…</select>

<select aria-label="依狀態篩選">…</select>   <!-- no visible label -->
<button aria-label="關閉選單">✕</button>
```

### 3. `<fieldset>` needs a `<legend>` as its first child — Freego `HM1130103C`
Any `<fieldset>` (a related-controls group — radio/checkbox groups, but also a compact
button-row toolbar) must have a `<legend>` as its literal **first child element**.
`aria-label` on the `<fieldset>` is ARIA-equivalent for the accessible name, but does
**not** satisfy this rule — Freego checks the DOM structure directly, not the computed
accessible name. If a visible legend would break a compact layout, keep it but hide it
visually with `sr-only`; never omit it.

```html
<!-- ❌ aria-label alone — fails HM1130103C even though it's accessible to AT -->
<fieldset aria-label="調整文字大小">…</fieldset>

<!-- ✅ -->
<fieldset aria-label="調整文字大小">
  <legend class="sr-only">調整文字大小</legend>
  …
</fieldset>
```

> **Common trap**: converting a `<div role="group">` to a native `<fieldset>` (e.g. to
> satisfy a linter's "prefer native element over ARIA role" rule, such as SonarQube
> `typescript:S6819`) silently drops this requirement — the linter doesn't check for a
> legend, only Freego does. Whenever `role="group"` becomes `<fieldset>`, add the legend
> in the same change.

### 4. Data tables need header scope — Freego `HM1130101C`
- `<th scope="col">` for column headers, `<th scope="row">` for row headers.
- An empty corner cell must be `<td>`, **not** a scope-less `<th>`.
- Add a `<caption>` (a visually-hidden one is fine) describing the table.

```html
<table>
  <caption class="sr-only">各部會專案數量</caption>
  <thead><tr>
    <td></td>                     <!-- empty corner: td, not th -->
    <th scope="col">技術</th>
  </tr></thead>
  <tbody><tr><th scope="row">應用</th><td>3</td></tr></tbody>
</table>
```

### 5. Colour contrast ≥ 4.5:1 (WCAG AA, normal text)
Light-grey muted text on white commonly fails — verify it.

- Tailwind: `text-gray-400` (#9ca3af ≈ 2.5:1) **fails**; use `text-gray-500` (#6b7280 ≈ 4.8:1).
- Dark mode: pair with `dark:text-slate-400` (not `slate-500`).
- Colour-coded label text: use the `-700` shade, not `-600`, and add a dark variant.

### 6. Heading hierarchy must match the visual title structure — WCAG 2.0 AA (1.3.1 / 2.4.6)
Freego's heading-structure view (標題檢視) lists the page's `<h1>`–`<h6>` outline; a user reporting
that「標題沒有按照層級」means that outline is broken. Three failure modes, most common first:

- **A visual title not marked up as a heading** (the usual culprit). A section / card / list-item
  title rendered with prominent styling — `font-bold`, `font-semibold`, `text-lg`, `text-xl` — inside
  a `<p>`, `<div>`, or `<span>` *looks* like a heading but is **absent from the outline**, so screen-reader
  users can't jump to it. Promote it to the `<h1>`–`<h6>` level that matches its nesting depth.
- **A skipped level.** Never jump a level going down — `<h1>` then `<h3>` with no `<h2>` between, or a
  card title hard-coded as `<h3>` directly under the `<h1>` page title. Each step down is +1 at most.
- **Missing or duplicate `<h1>`.** Exactly one `<h1>` per page (a visually-hidden `sr-only` one is fine).

```html
<!-- ❌ a card/section title that reads as a heading but isn't one → missing from the outline -->
<p class="text-lg font-semibold">評估風險</p>
<!-- ✅ marked at the level that fits its place in the outline (h1 → h2 → h3) -->
<h3 class="text-lg font-semibold">評估風險</h3>
```

> **The visual stays identical.** Tailwind's Preflight resets `<h1>`–`<h6>` to `font-size: inherit;
> font-weight: inherit; margin: 0`, so changing `<p>`→`<h3>` while keeping the same utility classes
> renders pixel-for-pixel the same — you gain the semantics for free. (Without Preflight, add the
> matching `text-*`/`font-*` classes so the heading doesn't jump to the browser default size.)

**Don't over-promote** — these are *not* missing headings, and marking them up is wrong:
- Body-weight text (`font-medium` or lighter, `text-sm`/`text-xs`) that isn't visually prominent —
  it's usually a field label or helper text, not a title.
- Items already inside a semantic `<ul>`/`<li>` — the list conveys the grouping.
- A one-field prompt sitting above a single input → that's a `<label for>`, not a heading.

**Accordion / disclosure titles**: put the heading *outside* the trigger, never a heading inside a
button — `<h2><button aria-expanded aria-controls="p1">部會名稱</button></h2>` (WAI-ARIA APG pattern).

> **Common trap — one fix, many rows.** A title inside a `.map()` is one JSX expression, so a single
> `<p>`→`<h3>` covers every rendered row. But a title coming from a **shared component** (a `<Card>`
> wrapper, a `RiskItemHeader`) renders on *many* pages — fix it once there, then check it doesn't
> create a skipped level on any page that consumes it (you may need to promote that page's own title
> in tandem so the shared one sits exactly one level below it).

### 7. ARIA / structural patterns (apply by default)
- Form error messages: `role="alert" aria-live="assertive"`; link the field via `aria-describedby`.
- Decorative icons/emoji: `aria-hidden="true"`.
- Toggle buttons: `aria-pressed`. Disclosure/accordion: `aria-expanded` + `aria-controls`.
- Off-canvas/drawer parked offscreen: `inert` (and/or `aria-hidden`) when closed, so it leaves the keyboard tab order.
- `<html lang="zh-TW">`; viewport must allow zoom (no `user-scalable=no` / `maximum-scale=1`).

## Freego scanning notes
Freego is a desktop crawler. It **cannot reliably**:
- crawl past SPA logins that use JWT/localStorage (not cookies), or
- open collapsed/hidden create or edit forms.

So for login-gated pages and hidden forms, **audit the source directly** against this checklist
rather than trusting the scan alone. Re-scan after fixes, and verify a build
(`tsc` / your bundler) before committing.

### A flagged page may not be your app at all
If a single finding looks structurally different from the rest (e.g. "root element missing
`lang`" on only one URL out of many, or a snippet that doesn't match your actual
`index.html`), don't assume it's a bug in your app before checking what was actually served.
A bare URL missing a trailing slash can hit a shared/outer reverse proxy in front of your
container (a colleague's own nginx, a CDN, a load balancer) and get back that proxy's own
default error/redirect page instead of your SPA — which naturally has no `lang`, no your CSP
headers, etc. `curl -i` the exact flagged URL (with and without the trailing slash) and
compare the response body/headers against what your own server actually returns before
"fixing" code that isn't the real cause; the real fix may belong to whoever owns that outer
proxy, not this repo.
