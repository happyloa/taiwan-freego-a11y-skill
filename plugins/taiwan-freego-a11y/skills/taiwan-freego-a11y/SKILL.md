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

### 3. Data tables need header scope — Freego `HM1130101C`
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

### 4. Colour contrast ≥ 4.5:1 (WCAG AA, normal text)
Light-grey muted text on white commonly fails — verify it.

- Tailwind: `text-gray-400` (#9ca3af ≈ 2.5:1) **fails**; use `text-gray-500` (#6b7280 ≈ 4.8:1).
- Dark mode: pair with `dark:text-slate-400` (not `slate-500`).
- Colour-coded label text: use the `-700` shade, not `-600`, and add a dark variant.

### 5. ARIA / structural patterns (apply by default)
- One `<h1>` per page (a visually-hidden `sr-only` one is fine).
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
