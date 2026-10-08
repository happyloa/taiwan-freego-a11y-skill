# Verification and evidence

## Contents

- Test matrix
- Freego report triage
- Manual checks
- Result format
- Completion rules

## Test matrix

Inventory page templates and complete processes before testing. Include all relevant
routes and states: public/authenticated, dialog closed/open, valid/invalid form,
loading/empty/error, hover/focus, light/dark, desktop/mobile, and each language.
Record pages and states not reached by the scanner. Crawl counts are not state coverage.

Use the project's build, type checking, linting, and automated accessibility tooling
when available. Match automated tags to WCAG 2.2 A/AA (or the user's selected level),
but do not mistake their rule set for the Taiwan appendix. Record tool version,
configuration, URL, state, date, and results. Do not silently install unrelated tools
or pretend an unavailable browser/screen-reader check ran.

## Freego report triage

1. Record standard edition, selected level, actual Freego/browser/driver versions,
   JavaScript settings, scanned URLs/count, exclusions, and authenticated state.
2. Preserve every code, full message, URL, snippet/selector, and status from the
   report. Look up the code in the matching edition, not by its suffix alone.
3. For 115.11, look up the official message and PDF source page in `coverage.json`.
   Flag unknown/legacy codes for investigation; the helper only recognizes codes.
4. Fetch/inspect the exact flagged response and rendered DOM. Check HTTP errors,
   redirects, proxy-generated pages, missing CSS, blocked resources, trailing slashes,
   and login redirects before changing application components.
5. Fix the actual source, re-test the exact URL/state and consuming templates, then
   rerun the actual scanner if available. Keep fixes and observed pass evidence separate.

Do not invent a Freego CLI, reuse a pre-transition report as proof of 115.11, or claim
to have run desktop Freego when only axe/source inspection ran. Check the accepted
tool edition on the official release page before certification.

## Manual checks

- **Keyboard:** follow complete processes with Tab/Shift+Tab, Enter/Space, arrows,
  and Escape as appropriate. Inspect order, traps, shortcuts, skip links, modal
  containment/dismissal/return focus, and closed offscreen controls.
- **Focus:** inspect every focus stop with sticky headers, overlays, and cookie
  banners at zoom and small viewports. AA prohibits complete author-created
  occlusion; AAA prohibits partial occlusion too. Measure AAA indicator area and
  focused/unfocused contrast separately.
- **Screen reader:** use an available NVDA/Firefox or Chrome, or VoiceOver/Safari
  combination and state it. Inspect names, roles, labels, landmarks, heading/table
  navigation, validation errors, changes, live regions, and iframe content.
  An accessibility-tree snapshot is useful evidence but is not a screen-reader run.
- **Visual:** check actual text/control/graphic contrast in all relevant states;
  200% text resizing; 320px reflow/400% zoom where applicable; orientation; and user
  text spacing (including Taiwan's Chinese spacing note). Inspect clipping,
  hidden content, overlap, and horizontal scrolling exceptions.
- **Pointer:** try drag-required tasks with a single pointer without dragging;
  exercise gesture alternatives and cancellation. Measure target bounding boxes
  and spacing exceptions. Keyboard alternatives alone do not prove 2.5.7.
- **Content/media:** judge alternatives for their meaning, caption accuracy,
  audio descriptions, live content, flashing, autoplay controls, time limits,
  open-format downloads, document accessibility, and third-party embeds.
- **Processes:** test repeated-input assistance, help order, review/correction of
  submissions, login/recovery/MFA/CAPTCHA, password-manager completion, copy/paste,
  and code entry assistance through every authentication step.

For every relevant E code, read its official message and apply the appropriate
test. Alternative techniques can be not applicable with an explanation. For a
common-failure code, passing means the described failure was evaluated and absent,
not that the failure technique was implemented.

## Result format

Report in the user's language. Keep a summary followed by an evidence table:

| Criterion / C or E code | Page and state | Status | Evidence / fix / next action |
| --- | --- | --- | --- |
| 2.5.7 / FA2250700E | Board, card selected | Fail | Drag-only move; add click-select/click-place and verify with one pointer. |
| 3.3.8 / HM2330800E | Login and MFA | Pending | Labels inspected; password-manager and assisted-code flows still require testing. |

Use only these statuses:

- **Pass:** observed evidence satisfies the applicable requirement in this scope.
- **Fail:** observed evidence demonstrates a violation; explain how to reproduce it.
- **Pending:** not tested, blocked, unavailable, or evidence insufficient.
- **Not applicable:** explain the actual absence, exception, or alternative technique.

Record measured values and reproducible steps rather than a bare assertion. Include
scope, target edition/level, tool versions, unresolved external content, and the
remaining tests. Associate related codes with the criterion, but do not multiply
one defect into unrelated findings.

## Completion rules

Conclude that code coverage is complete only for the documented inventory/version.
Conclude that tested content passes only for the pages, states, criteria, and methods
actually verified. Leave a full-site 115.11 claim pending if required pages/processes
or manual tests remain unverified. Do not present a build, lint, axe score, or a
generated worksheet as official Freego approval or a government certification.

Never suppress findings by adding misleading alt/title, hiding meaningful elements
with aria-hidden, disabling features, or excluding pages without a legitimate reason.
