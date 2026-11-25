# 台灣 Freego 無障礙 Skill

讓 Claude Code 依台灣《網站無障礙規範 (115.11)》／WCAG 2.2 開發、修正與稽核網站，處理 Freego 報告，並列出仍需人工驗證的項目。預設 AA。

[![Validate skill](https://github.com/happyloa/taiwan-freego-a11y-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/happyloa/taiwan-freego-a11y-skill/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![WCAG 2.2](https://img.shields.io/badge/WCAG-2.2%20AA-166534.svg)](https://www.w3.org/TR/WCAG22/)

版本 2.3.0。適用 HTML、JSX、Vue、Svelte、CSS 與既有網站審查。

## 安裝

需要 [Claude Code](https://code.claude.com/docs/en/setup) 2.1.275 以上。在 Claude Code 內執行：

```text
/plugin install taiwan-freego-a11y --marketplace happyloa/taiwan-freego-a11y-skill
```

或在終端機執行：

```bash
claude plugin install taiwan-freego-a11y --marketplace happyloa/taiwan-freego-a11y-skill
```

較舊的 Claude Code 先執行 `claude plugin marketplace add happyloa/taiwan-freego-a11y-skill`，再執行 `claude plugin install taiwan-freego-a11y@happyloa-skills`。

用 `claude plugin list` 確認 `taiwan-freego-a11y@happyloa-skills` 已啟用、版本為 2.3.0。目前的工作階段還沒載入時，執行 `/reload-plugins`。

一般使用不需要 Node.js 或 npm。附帶的清單工具需要 Python 3.10 以上，沒有 Python 時 Claude 仍能使用規範與修正指引。

## 使用

在專案目錄啟動 Claude Code，輸入 `/taiwan-freego-a11y:taiwan-freego-a11y`，後面接要做的事：

```text
/taiwan-freego-a11y:taiwan-freego-a11y 依115.11 AA檢查並修正結帳頁與共用元件，保留原有功能與視覺。列出仍需人工驗證的項目。
```

```text
/taiwan-freego-a11y:taiwan-freego-a11y 讀取 reports/freego.html，先確認規範與工具版本，再依每筆完整訊息修正專案。版本不符或無法確認的項目標示 Pending。
```

```text
/taiwan-freego-a11y:taiwan-freego-a11y 為這個專案建立115.11 AA稽核清單，涵蓋所有路由、登入狀態、表單錯誤與完整流程，依實際證據標示 Pass、Fail、Pending、Not applicable。
```

Claude 也會依任務自動選用這個 Skill，明確呼叫可以確保這次一定載入。

## 涵蓋範圍

| 目標等級       | 有效成功準則（累計） | 機器檢測碼 C（累計） | 人工稽核碼 E（累計） |
| -------------- | -------------------: | -------------------: | -------------------: |
| A              |                   31 |                   21 |                  103 |
| **AA（預設）** |               **55** |               **23** |              **161** |
| AAA            |                   86 |                   28 |                  216 |

每個 C／E 碼都附官方訊息、對應準則、等級與 PDF 頁碼。4.1.1 在新版已刪除，只保留歷史紀錄。115.11 新增的準則包括焦點不遮蔽、拖曳替代、最小目標尺寸、一致性幫助、冗餘輸入與無障礙認證。

## 認證時程與 Freego 版本

- 115.11 標章認證自 2026-11-30 開始，同一天起不再受理 110.07 申請；2026-11-29 以前取得的標章效期仍為 3 年。
- 截至 2026-11-25，官方只提供適用 110.07 的 Freego Dec 19 2025，還沒有 115.11 版。送驗前先到[官方下載專區](https://accessibility.moda.gov.tw/Download)確認可用版本。
- 110.07 的掃描結果不能證明網站符合 115.11。同一個代碼在兩版的意思可能不同：110.07 報告的 HM1130103C 是 fieldset 缺 legend，到 115.11 改編為 HM1130105C。

來源與日期見[版本與官方來源](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/references/sources-and-versions.md)。

## 送驗前要做的事

Skill 處理專案修正與稽核準備，本身不執行 Freego 檢測，也不能代替標章。送驗前：

1. 用官方接受版本的 Freego 檢測可存取的測試網站，保留報告與設定。
2. 把完整報告交給 Claude 修正，再用 Freego 重測相同的 URL 與狀態。
3. 完成適用的鍵盤、螢幕閱讀器、版面、媒體與登入檢查，記錄例外理由，處理完所有 Fail 與 Pending。

## 待檢清單工具

Claude 需要時會自己執行。手動執行時，在本 repo 根目錄：

```bash
python plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/scripts/audit_checklist.py --level AA --output a11y-audit.md
```

可用 `--level A|AA|AAA`、`--format json`、`--report freego-report.html`（只辨識報告裡的代碼）。工具只產生 Pending 清單，不掃描網站，也不判定通過。Windows 沒有 `python` 指令時改用 `py`。

## 更新

```bash
claude plugin marketplace update happyloa-skills
claude plugin update taiwan-freego-a11y@happyloa-skills
```

再到工作階段執行 `/reload-plugins`。第三方 marketplace 預設不會自動更新，可在 `/plugin` → Marketplaces 開啟。

## 不使用 Plugin

把 `plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/` 整個資料夾複製到 `~/.claude/skills/` 或專案的 `.claude/skills/`，再用 `/taiwan-freego-a11y` 呼叫。references 與 scripts 要一起複製。

## 文件

- [Skill 流程](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/SKILL.md)
- [成功準則清單](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/references/criteria-checklist.md)／[C 碼修正指引](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/references/machine-checks.md)／[C、E 完整清單](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/references/coverage.json)
- [人工驗證與報告格式](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/references/verification-and-reporting.md)
- [驗證紀錄](docs/verification.md)
- [更新紀錄](CHANGELOG.md)／[貢獻與本機測試](CONTRIBUTING.md)／[回報問題](https://github.com/happyloa/taiwan-freego-a11y-skill/issues/new/choose)

## English

A Claude Code plugin for building, fixing, and auditing websites against Taiwan's web accessibility standard 115.11 (aligned with WCAG 2.2), AA by default. It covers 86 active criteria, 28 C codes, and 216 E codes, and keeps automated evidence separate from manual checks.

Install with `claude plugin install taiwan-freego-a11y --marketplace happyloa/taiwan-freego-a11y-skill` (Claude Code 2.1.275 or later), then run `/taiwan-freego-a11y:taiwan-freego-a11y` followed by your task or Freego report.

115.11 certification starts on 2026-11-30, the day 110.07 applications stop. As of 2026-11-25 the only official Freego release (Dec 19 2025) targets 110.07, so its reports do not show 115.11 conformance. The skill does not replace Freego, screen-reader testing, or certification.

## License

[MIT](LICENSE) 適用於本 repo 自行撰寫的程式與指引。官方規範摘錄的出處為數位發展部，見來源說明。
