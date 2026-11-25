# Changelog

## 2.3.0 — 2026-11-25

- Read references by task instead of all five on every run, and tighten SKILL.md (1,849 to 1,673 words). Eval scores matched 2.2.0 within judge noise, and a run of the suite cost about 6% less.
- Record a Freego Dec 19 2025 test scan: 110.07 reports use HM1130103C for fieldset/legend, which 115.11 numbers HM1130105C. List what that scan did not report.
- Add four `claude plugin eval` cases (checkout repair, 110.07 report triage, audit-only page, edition and date questions) and document how to run them.
- Move the inventory-update procedure from the skill to CONTRIBUTING.

## 2.2.0 — 2026-11-25

- Record the 115.11 transition: 110.07 badge applications stop on 2026-11-30, badges issued through 2026-11-29 stay valid for three years, and no 115.11 Freego had been published as of 2026-11-25.
- Add `--output` to the checklist tool, and keep redirected output UTF-8 on Windows consoles.
- Fix four Windows test failures (locale-encoded reads), the install test's Python lookup, and cp950 console output.
- Document and test the one-step `plugin install --marketplace` command.
- Update Claude Code 2.1.332, Playwright 1.65.1, @sparticuz/chromium 158.0.0, axe-core 4.14.1, and Noto Sans TC 5.3.1.
- Shorten the README, plugin README, contribution guide, and verification notes.

## 2.1.0 — 2026-10-08

- Clarify installation, usage, Freego remediation, evidence, and verification limits.
- Add repository/homepage/author metadata and synchronize marketplace/plugin versions.
- Verify real Claude Code installation and discovery with complete bundled resources.
- Add isolated installation smoke checks, a before/after checkout fixture, browser regression checks, and CI.
- Add issue/PR templates and contribution instructions.

## 2.0.0 — 2026-10-08

- Adopt Taiwan 115.11 / WCAG 2.2, default AA, with 86 active criteria and all 244 C/E codes.
- Correct table/form mappings, include new criteria, and retain deleted 4.1.1 only for migration.
- Add pending-checklist generation, report-code recognition, source provenance, and manual verification guidance.

## 1.1.0 — 2026-07-27

- Add heading-structure guidance to the original skill.
