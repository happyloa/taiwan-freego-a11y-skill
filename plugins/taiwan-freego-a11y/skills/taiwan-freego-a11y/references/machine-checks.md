# Complete 115.11 C-code implementation guide

## Contents

- A-level checks (21)
- Additional AA checks (2)
- Additional AAA checks (5)
- Interpretation boundaries

Read the precise official messages in `coverage.json`. The following instructions
are implementation guidance. Test applicability and any alternative technique;
do not claim these prose checks reproduce the Freego binary.

## A-level checks (21)

| Code | Criterion | Inspect and repair |
| --- | --- | --- |
| HM1110100C | 1.1.1 | Check every rendered img for alt. Describe informative images; use empty alt only when decorative or already adequately described. |
| HM1110101C | 1.1.1 | Give actionable map/area regions non-empty descriptions of their destination or function. |
| HM1110103C | 1.1.1 | Give meaningful character art, symbols, and emoji equivalent text; follow the appendix title condition where relevant. Keep decorative/redundant symbols ignorable. Check actual scanner-version behavior. |
| HM1110104C | 1.1.1 | Name input type=image with non-empty alt describing the action, rather than its appearance. |
| HM1110105C | 1.1.1 | Supply equivalent fallback content for embedded objects. Replace obsolete applets/plugins when possible; do not introduce them merely because the annex mentions them. |
| HM1110106C | 1.1.1 | For decorative img with alt="", omit title; ensure linked/functional images still have an appropriate accessible purpose elsewhere. |
| HM1130100C | 1.3.1 | Inspect heading nesting in every state and route. Make genuine section titles headings at the correct level; keep reusable headings configurable. |
| HM1130101C | 1.3.1 | Associate suitable row/column/group headers through scope; inspect span and grouping semantics. |
| HM1130102C | 1.3.1 | Associate complex data cells with the correct unique header IDs through headers. Check references exist and reflect all relevant headers. |
| HM1130103C | 1.3.1 | Group related select options using optgroup with meaningful labels. Do not invent groups when there is no meaningful grouping. |
| HM1130104C | 1.3.1 | Give visible form controls non-empty, correctly associated labels; use title only in the specified exceptional cases. Verify labels remain in rendered output and unique IDs survive loops. ARIA-only naming is not proof of this structural check. |
| HM1130105C | 1.3.1 | Group related form controls with fieldset and a meaningful legend. Put legend first and preserve each individual control's name. |
| HM1130200C | 1.3.2 | Inspect mixed RTL/LTR text. Set appropriate dir/bidi isolation or direction marks without corrupting reading order. |
| HM1240102C | 2.4.1 | Group related navigation links in nav and distinguish multiple navigation regions. Also test the actual bypass mechanism under 2.4.1. |
| HM1240200C | 2.4.2 | Provide a non-empty descriptive document title; update it for SPA routes and relevant state changes. |
| HM1240400C | 2.4.4 | Combine adjacent image/text links to the same destination where appropriate. Avoid duplicate names; retain meaningful image information not supplied by the text. |
| HM1240401C | 2.4.4 | Give links non-empty purpose-bearing text/alternatives; apply the annex's contextual title condition and inspect the report's exact message. Title must supplement, not substitute for usable link content. |
| HM1310100C | 3.1.1 | Set a valid non-empty html lang matching the page's actual primary language, such as zh-TW. Inspect error, redirect, and login pages too. |
| ME1320200C | 3.2.2 | Offer downloads in open formats such as ODF, accessible PDF, or HTML. Inspect the document's headings, reading order, alternatives, and controls; its file extension is not proof. |
| HM1410200C | 4.1.2 | Expose usable names, roles, values, states, and notifications for all interactive components. Inspect the accessibility tree and actual operation. |
| HM1410201C | 4.1.2 | Give iframe a non-empty descriptive title and inspect the accessibility of the embedded content and controls. |

## Additional AA checks (2)

| Code | Criterion | Inspect and repair |
| --- | --- | --- |
| CS2140401C | 1.4.4 | Use named or relative font-size units in authored/imported/inline/generated CSS. Check actual 200% resizing independently; avoid assuming all utility classes are relative. |
| HM2310200C | 3.1.2 | Mark meaningful passages in another language with a valid lang, observing exceptions for names, technical terms, indeterminate language, and assimilated words. |

## Additional AAA checks (5)

| Code | Criterion | Inspect and repair |
| --- | --- | --- |
| CS3140800C | 1.4.8 | Provide the required foreground/background customization; inspect the annex condition for a single stylesheet without an alternative. Do not remove all colors from an AA design. |
| CS3140801C | 1.4.8 | Use relative column sizing and satisfy the 80-character/40-CJK-character line-length requirement; inspect actual rendered text rather than assuming ch equals a Chinese glyph. |
| CS3140802C | 1.4.8 | Specify appropriate line spacing and inspect the complete AAA visual-presentation requirements, including paragraph spacing and alignment. |
| HM3240900C | 2.4.9 | Give stand-alone links purpose-bearing link content and the appendix's non-empty title. Verify purpose without relying on surrounding context. |
| HM3241000C | 2.4.10 | Use meaningful section headings to organize the page; verify all relevant sections, not simply that one heading exists. |

## Interpretation boundaries

Use **23 cumulative C codes for AA**, not only its two additional codes. Keep all
216 E codes and the active criteria in scope alongside the C checks.

The revised table/header/form identifiers differ from the old skill. Do not remap
codes based solely on a familiar number. Use the report edition and full message,
and record unknown or edition-mismatched codes as unresolved.

Freego reports may use syntactic conditions stricter or narrower than general
accessible-name checks. Keep semantic accessibility and scanner compatibility
evidence separate, satisfy both where applicable, and avoid hacks that hide content
or destroy its meaning.
