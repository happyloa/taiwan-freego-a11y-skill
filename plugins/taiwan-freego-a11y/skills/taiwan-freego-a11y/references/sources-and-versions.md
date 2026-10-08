# Sources, scope, and version selection

## Contents

- Authority and provenance
- Coverage and level selection
- Changes from the former skill
- Freego compatibility
- Updating the inventory

## Authority and provenance

Use the Taiwan document for Taiwan-specific requirements and identifiers. Use W3C
for supporting explanations and implementation techniques. Do not replace Taiwan's
annex with an axe rule list or a generic WCAG checklist.

| Source | Purpose |
| --- | --- |
| [MODA legal record, GL000192](https://law.moda.gov.tw/LawContent.aspx?id=GL000192) | 2026-05-29 publication, order 11540006711, effective 2026-11-30 |
| [Official revised PDF](https://law.moda.gov.tw/Download.ashx?FileID=11455&id=GL000192&type=LAW) | 115 May standard and Appendix 1 C/E tables |
| [MODA download page](https://accessibility.moda.gov.tw/Download/Detail/2783?Category=36) | Revised document and publication order |
| [Certification transition announcement](https://accessibility.moda.gov.tw/News/Detail/5608?Category=43) | 115.11 certification starts 2026-11-30 |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | International success criteria, exceptions, conformance, and terminology |
| [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/) | Component keyboard and focus implementation guidance |
| [Freego release page](https://accessibility.moda.gov.tw/Download/Detail/2763?Category=70) | Tool version and historical operational changes |

Verified on **2026-10-08**. The official download endpoints returned content types
unsupported by the retrieval service. Read the published 115 May government PDF
through [this public mirror](https://github.com/HSU-YU-MING/ramp-a11y/blob/main/docs/tw-web-accessibility-spec-115.pdf),
not through the mirror project's interpretation of it. Its Git blob SHA is
`a156b31b40aac843f6131cc910297a04a2facc3e`; the downloaded PDF SHA-256 is
`0ad5838a149420f834cb15dd74748c2ba34a63880c1c0cfe2196b9b90633e228`.
Byte equality with an independently downloaded official copy was not established.
The legal record and official announcement independently confirm the version and date.

`coverage.json` records the official appendix messages and source PDF page indices.
The C table occupies PDF pages 49–51; E tables occupy pages 53–64. Extracted table
identifiers were cross-checked against an independent plain-text extraction.
The skill's implementation advice is separate from these normative messages.

## Coverage and level selection

The document describes 87 numbered criterion entries. **4.1.1 is explicitly deleted**,
leaving **86 active criteria**. Retain the deleted entry for migration bookkeeping,
but never count it as an active requirement.

| Selected level | Active criteria, cumulative | C codes, cumulative | E codes, cumulative |
| --- | ---: | ---: | ---: |
| A | 31 | 21 | 103 |
| AA (default) | 55 | 23 | 161 |
| AAA | 86 | 28 | 216 |

Use all lower-level requirements when targeting AA or AAA. The inventory contains
all 244 appendix codes, including techniques and common failures. The code count is
an **index coverage count**, not a website conformance score or a statement that a
particular Freego version executes every C code. Some criteria have no dedicated
code; still test them using `criteria-checklist.md`.

Preserve the annex's code classification even where it differs from its linked
criterion: for example, GN1240500E is listed in the A-code table while 2.4.5 is an
AA criterion. Code level and criterion level are separate source fields; do not
silently rename the identifier or change either classification.

Evaluate complete pages and complete processes. Keep justifiable criterion-specific
exceptions and alternative techniques distinct from inaccessible or untested content.
Do not require every alternative sufficient technique simultaneously. Do not mark
a criterion passed solely because one associated technique was used.

## Changes from the former skill

Use the revised appendix to interpret **115.11** codes:

| Code | Revised meaning |
| --- | --- |
| HM1130101C | Table scope associations |
| HM1130102C | Table id/headers associations |
| HM1130103C | Select option grouping |
| HM1130104C | Visible form-control labels/title |
| HM1130105C | Fieldset/legend grouping |

The former skill called HM1130103C a legend check. This is incorrect for 115.11.
The [110.07 web index](https://accessibility.moda.gov.tw/Accessible/Guide/68) and its
linked detail pages also differ in some numbering. Preserve the report's **version,
code, full message, URL, and element** when handling an older report; never silently
reinterpret a code with a different edition's meaning.

Do not carry forward obsolete requirements as new 115.11 C codes:

- HM1110102C (legacy longdesc): absent from the revised C table. Provide accessible
  detailed descriptions using the active non-text-content requirements.
- HM1410100C / 4.1.1 (legacy parsing validation): absent/deleted. Broken IDs or markup
  can still fail active relationships, accessible names, or behavior requirements.
- HM3330500C (legacy contextual-help C code): absent. Evaluate contextual help using
  the active 3.3.5 criterion and its E codes when targeting AAA.
- CS2140400C and CS2140402C: historical Freego codes removed in the 2022 tool update.

The nine newly numbered criteria are 2.4.11–2.4.13, 2.5.7–2.5.8, 3.2.6, and
3.3.7–3.3.9. Of these, **six apply to AA** through its cumulative A/AA scope.

## Freego compatibility

As of verification, the official release page announces **Freego Dec 19 2025** for
110.07. Do not invent a new Freego version or claim that its older report verifies
115.11. Before a certification run, check the official download page for the edition
accepted for the target application date and record the actual tool version.

The historical release notes suspended HM1110103C and excluded some aria-hidden
elements from machine inspection. The **115.11 annex nevertheless lists HM1110103C**.
Keep its normative coverage; independently check meaningful symbols and emoji and
document the actual runtime result. Never extrapolate an old tool suspension to a
removal from the new standard.

If the selected scanner cannot assess a new criterion or state, perform the manual
check and leave missing machine evidence pending. Never use a scanner limitation
to declare the requirement not applicable.

## Updating the inventory

When official documents or tool versions change, re-read the publication record,
the full appendix, and the tool release notes. Keep the source edition and date with
the inventory. Validate counts, identifier-to-criterion relationships, changed
messages, and the criterion checklist together; then run the repository checks.
Do not update only a version string or reuse a third-party rule inventory as authority.
