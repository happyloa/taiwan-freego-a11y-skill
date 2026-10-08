# Complete 115.11 criterion checklist

## Contents

- Perceivable: 1.1–1.4
- Operable: 2.1–2.5
- Understandable: 3.1–3.3
- Robust: 4.1

Use all A requirements for AA and all A/AA requirements for AAA. The document has
87 numbered entries, including removed 4.1.1; test **86 active criteria**, or **55**
for default AA. These are practical checks; read the official text for full
definitions and exceptions. Record Pass / Fail / Pending / Not applicable with
evidence. Evaluate every selected-level C/E message in `coverage.json` alongside
these criterion checks. A technique may be an alternative; a FA code is a failure
condition. Neither a missing dedicated code nor a tool limitation exempts a criterion.

## Perceivable

| Criterion | Level | Check |
| --- | --- | --- |
| 1.1.1 非文字內容 | A | Review images, image maps, SVG/canvas/charts, objects, symbols, sensory content, and CAPTCHA for meaningful equivalents; decorative content must be ignorable. |
| 1.2.1 純音訊與純視訊(預錄) | A | For prerecorded audio-only/video-only, verify equivalent transcripts, descriptions, or a qualifying alternative audio track; assess the explicitly labelled text-alternative exception. |
| 1.2.2 字幕(預錄) | A | Watch prerecorded synchronized media and verify accurate, synchronized captions including relevant speech and sounds; assess the labelled text-alternative exception. |
| 1.2.3 音訊描述或替代媒體 | A | Verify prerecorded synchronized media has audio description or a complete time-based media alternative, unless the specified text-alternative exception applies. |
| 1.2.4 字幕(現場直播) | AA | Verify live synchronized media includes usable captions for the audio content. |
| 1.2.5 音訊描述(預錄) | AA | Verify audio description of important visual information in prerecorded synchronized video; a transcript alone is insufficient at AA. |
| 1.2.6 手語(預錄) | AAA | Verify prerecorded synchronized audio has sign-language interpretation. |
| 1.2.7 延伸音訊描述 | AAA | Provide extended audio descriptions when pauses cannot accommodate necessary visual information. |
| 1.2.8 替代媒體(預錄) | AAA | Verify complete time-based alternatives for all prerecorded synchronized media and prerecorded video-only. |
| 1.2.9 純音訊(現場直播) | AAA | Verify an equivalent alternative for live audio-only, such as live text/captions. |
| 1.3.1 資訊與關連性 | A | Inspect real headings, lists, emphasis, data-table associations, form labels/groups, and options; ensure structure and relationships survive nonvisual reading. |
| 1.3.2 有意義的序列 | A | Compare visual, DOM, screen-reader, and linearized reading sequences; inspect mixed text direction and layout tables. |
| 1.3.3 知覺特徵 | A | Ensure instructions identify actions using text rather than only shape, color, position, orientation, size, or sound. |
| 1.3.4 螢幕方向 | AA | Operate in portrait and landscape; accept a lock only when that orientation is essential. |
| 1.3.5 識別輸入目的 | AA | Check correct autocomplete/input-purpose tokens for fields collecting recognized user information. |
| 1.3.6 識別目的 | AAA | Verify regions, icons, and component purposes can be determined programmatically using supported semantics. |
| 1.4.1 色彩使用 | A | Inspect errors, required fields, links, charts, selection, and status without color; retain an equivalent text/shape/pattern cue. |
| 1.4.2 音訊控制 | A | If automatic audio lasts more than 3 seconds, verify pause/stop or independent volume control. |
| 1.4.3 對比值(最小) | AA | Measure actual normal-text contrast >=4.5:1 and large-text contrast >=3:1 in relevant states; assess logo/incidental/inactive exceptions. |
| 1.4.4 調整文字尺寸 | AA | Resize text to 200% without losing content/functions, including text in controls; apply the caption/image-text exceptions and relative-font C check. |
| 1.4.5 影像文字 | AA | Use real text instead of images of text unless customizable or essential (including logotypes). |
| 1.4.6 對比值(增強) | AAA | Measure enhanced normal-text contrast >=7:1 and large-text contrast >=4.5:1, observing the stated exceptions. |
| 1.4.7 低或無背景音訊 | AAA | For applicable prerecorded speech audio, remove/disable background sound or keep it at least 20 dB below speech, except occasional short sounds. |
| 1.4.8 視覺呈現 | AAA | Verify selectable foreground/background; line lengths <=80 characters or 40 CJK; no full justification; line spacing >=1.5 and paragraph spacing >=1.5 times line spacing; 200% resizing without horizontal line scrolling. |
| 1.4.9 影像文字(無例外) | AAA | Allow images of text only when purely decorative or when the particular presentation is essential. |
| 1.4.10 流動排版 | AA | Test vertical content at 320 CSS px width or horizontal content at 256 CSS px height without lost information/functions or two-dimensional page scrolling; confine legitimate 2D exceptions locally. |
| 1.4.11 非文字對比 | AA | Measure >=3:1 contrast for necessary control/state and graphic information against adjacent colors; assess inactive/default-agent/essential exceptions. |
| 1.4.12 文字間距 | AA | Override line height to 1.5, paragraph spacing to 2em, letters to .12em (.14em Chinese), and words to .16em; retain content/functions and apply the Taiwan language notes. |
| 1.4.13 懸浮或焦點內容 | AA | Test added hover/focus content for dismissal without pointer/focus movement, pointer movement into it, and persistence; assess user-agent/essential exceptions. |

## Operable

| Criterion | Level | Check |
| --- | --- | --- |
| 2.1.1 鍵盤 | A | Complete all functions by keyboard without specific keystroke timing, except functions inherently dependent on the path of movement. |
| 2.1.2 無鍵盤操作陷阱 | A | Enter and leave every component using the keyboard; disclose any nonstandard exit method. |
| 2.1.3 鍵盤(無例外) | AAA | Complete every function by keyboard with no path-dependent exception. |
| 2.1.4 快捷鍵 | A | For single-character shortcuts, verify disable/remap capability or activation only while the relevant component has focus. |
| 2.2.1 計時調整 | A | For content time limits, verify off/adjust/extend: adjustment >=10x default or >=20-second warning with at least 10 simple extensions; assess real-time/essential/>20-hour exceptions. |
| 2.2.2 暫停、停止和隱藏 | A | Provide pause/stop/hide for applicable automatic moving/blinking/scrolling lasting >5 seconds, and pause/stop/hide/update-frequency control for applicable auto-updates. |
| 2.2.3 無計時 | AAA | Remove nonessential time limits except noninteractive synchronized media and real-time events. |
| 2.2.4 中斷 | AAA | Let users postpone or suppress interruptions unless they involve an emergency. |
| 2.2.5 重新認證 | AAA | Expire and reauthenticate a session; preserve the activity and entered data. |
| 2.2.6 逾時 | AAA | Warn about inactivity timeouts causing data loss unless data is preserved for more than 20 hours without user action. |
| 2.3.1 閃爍三次或低於閾值 | A | Check no more than three flashes in one second or compliance with both general/red flash thresholds; use measurement when uncertain. |
| 2.3.2 閃爍三次 | AAA | Verify no content flashes more than three times in any one-second period. |
| 2.3.3 來自互動的動畫 | AAA | Disable interaction-triggered nonessential motion, including through prefers-reduced-motion where suitable. |
| 2.4.1 跳過區塊 | A | Use a working keyboard bypass for repeated blocks and meaningful landmarks/headings; test the skip-link destination and focus. |
| 2.4.2 網頁標題 | A | Review each page/SPA route title for its specific topic or purpose, not only non-emptiness. |
| 2.4.3 焦點順序 | A | Tab through content and complete processes; ensure focus order preserves meaning and operation. |
| 2.4.4 鏈結目的(脈絡) | A | Determine each link purpose from its name and programmatically determinable context; inspect icon links and vague repeated labels. |
| 2.4.5 多種方式 | AA | Offer multiple ways to locate pages in a set, such as navigation plus search/site map; assess process/result-page exceptions. |
| 2.4.6 標題和標籤 | AA | Review headings and labels for descriptive topic/purpose, not merely their existence. |
| 2.4.7 焦點可視 | AA | Keep the keyboard focus indicator visible for every relevant interactive component. |
| 2.4.8 位置 | AAA | Expose the page location within its set/site, such as accessible breadcrumbs. |
| 2.4.9 鏈結目的(僅鏈結) | AAA | Determine each link purpose from link content alone, subject to the genuinely ambiguous-to-everyone exception. |
| 2.4.10 區段標題 | AAA | Organize content with descriptive section headings. |
| 2.4.11 焦點不遮蔽(最小) | AA | Tab at zoom/small viewports with author-created sticky bars/overlays; the focused component must not be completely hidden. |
| 2.4.12 焦點不遮蔽(加強) | AAA | Tab with author-created overlays; no part of the focused component may be hidden. |
| 2.4.13 焦點外觀 | AAA | Measure focus-indicator area >= a 2 CSS px perimeter and focused/unfocused same-pixel contrast >=3:1, subject to the unmodifiable user-agent exceptions. |
| 2.5.1 指標手勢 | A | Provide single-pointer, non-path alternatives to multipoint/path gestures unless essential. |
| 2.5.2 指標取消 | A | Verify no down-event activation, or abort/undo/up-event reversal, unless down-event completion is essential. |
| 2.5.3 標籤名稱 | A | Ensure the accessible name includes the visible text label, preferably beginning with that text. |
| 2.5.4 動作啟動 | A | Provide controls equivalent to motion actuation and a way to disable motion response; assess supported-interface/essential exceptions. |
| 2.5.5 目標尺寸(加強) | AAA | Measure pointer targets >=44x44 CSS px or document equivalent/inline/default-agent/essential exceptions. |
| 2.5.6 並行輸入機制 | AAA | Permit platform input mechanisms concurrently unless restrictions are essential, security-related, or needed to respect user settings. |
| 2.5.7 拖曳動作 | AA | Complete dragging functionality with a single pointer without dragging; keyboard-only alternatives are insufficient. Assess essential/default-agent exceptions. |
| 2.5.8 目標尺寸(最小) | AA | Measure targets >=24x24 CSS px or verify undersized-target 24px-diameter-circle spacing, equivalent, inline, default-agent, or essential exceptions. |

## Understandable

| Criterion | Level | Check |
| --- | --- | --- |
| 3.1.1 網頁語言 | A | Inspect valid html lang matching the primary human language, including error/login pages. |
| 3.1.2 局部語言 | AA | Mark language changes with valid lang; assess proper-name/technical-term/indeterminate/assimilated-word exceptions. |
| 3.1.3 特殊詞彙 | AAA | Offer meanings for unusual/restricted terms, idioms, and jargon. |
| 3.1.4 縮寫 | AAA | Offer expansions or meanings of abbreviations. |
| 3.1.5 閱讀程度 | AAA | When text requires above-lower-secondary reading ability after names/titles are removed, provide suitable supplemental content or a simpler version. |
| 3.1.6 發音 | AAA | Provide pronunciation information when meaning is ambiguous without it. |
| 3.2.1 焦點 | A | Focus a component without activating it; verify focus alone does not change context. |
| 3.2.2 輸入 | A | Change input/settings; avoid unexpected context changes unless the user was advised beforehand. Also inspect Taiwan open-format download requirements. |
| 3.2.3 一致的導覽 | AA | Compare repeated navigation across pages; preserve relative order unless the user changes it. |
| 3.2.4 一致的識別 | AA | Compare components with the same function; preserve consistent names/identification. |
| 3.2.5 依請求變更 | AAA | Change context only on user request or provide a mechanism to disable automatic changes. |
| 3.2.6 一致性幫助 | A | When repeated help/contact/self-help mechanisms exist, keep their relative order across pages unless the user changes it; adding help everywhere is not required. |
| 3.3.1 識別錯誤 | A | Trigger invalid/missing inputs; identify the field and describe the error in text. |
| 3.3.2 標籤或說明 | A | Provide visible labels, required-field instructions, and necessary format guidance before input. |
| 3.3.3 錯誤建議 | AA | For detected errors with known corrections, provide useful suggestions unless they compromise security or purpose. |
| 3.3.4 錯誤預防(法律、財務、個人資料) | AA | For legal/financial/data-changing/test submissions, provide reversal, validation with correction opportunity, or review/confirmation/correction before final submission. |
| 3.3.5 協助 | AAA | Provide contextual help that users can access when needed. |
| 3.3.6 錯誤預防(全部) | AAA | For all information submissions, provide reversal, validation/correction, or review/confirmation/correction. |
| 3.3.7 冗餘輸入 | A | Within one process, auto-fill or let users select previously supplied information; assess essential/security/no-longer-valid exceptions. |
| 3.3.8 無障礙認證(最小) | AA | Test every login/recovery/MFA step for supported cognitive-test alternatives/assistance; permit password managers and paste. Assess object-recognition/personal-content exceptions only at this minimum level. |
| 3.3.9 無障礙認證(加強) | AAA | Require cognitive-test alternatives or assistance at every authentication step; do not use object-recognition or personal-content exceptions. |

## Robust

| Criterion | Level | Check |
| --- | --- | --- |
| 4.1.1 語法分析 | Removed | Removed as obsolete in 115.11; retain only as a historical entry. Attribute actual broken relationships/behavior to active criteria. |
| 4.1.2 名稱、角色和值 | A | Inspect names, roles, states, values, properties, user-settable changes, notifications, and iframe titles in the accessibility tree and actual operation. |
| 4.1.3 狀態訊息 | AA | Verify status, error, and sequential-update announcements through suitable roles/live regions without requiring focus to move. |

## Supporting references

- [Taiwan publication record and revised PDF](https://law.moda.gov.tw/LawContent.aspx?id=GL000192)
- [WCAG 2.2 normative requirements and definitions](https://www.w3.org/TR/WCAG22/)
- [W3C Understanding WCAG 2.2](https://www.w3.org/WAI/WCAG22/Understanding/)
- [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
- See `sources-and-versions.md` for PDF provenance, dates, and code differences.
