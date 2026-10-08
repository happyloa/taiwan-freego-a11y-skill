# 台灣 Freego 無障礙 Skill

讓 Claude Code 協助你**開發、修正與稽核台灣無障礙網站**：把規範轉成專案修改、整理 Freego 報告，並追蹤需要人工驗證的項目。

[![Validate skill](https://github.com/happyloa/taiwan-freego-a11y-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/happyloa/taiwan-freego-a11y-skill/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![WCAG 2.2](https://img.shields.io/badge/WCAG-2.2%20AA-166534.svg)](https://www.w3.org/TR/WCAG22/)

**規範：台灣《網站無障礙規範 (115.11)》／WCAG 2.2 · 預設 AA · 版本 2.1.0**

支援 HTML、JSX、Vue、Svelte、CSS，以及現有網站的無障礙審查。適合在實作 UI 時直接使用，也適合將檢測報告轉成可驗證的修正工作。

## 快速安裝

先安裝並完成 [Claude Code](https://code.claude.com/docs/en/setup) 的帳號設定。在 Claude Code 內執行：

```text
/plugin marketplace add happyloa/taiwan-freego-a11y-skill
/plugin install taiwan-freego-a11y@happyloa-skills
```

依安裝介面選擇使用者或專案範圍。也可在終端機直接安裝：

```bash
claude plugin marketplace add happyloa/taiwan-freego-a11y-skill
claude plugin install taiwan-freego-a11y@happyloa-skills --scope user
```

確認安裝：

```bash
claude plugin list
claude plugin details taiwan-freego-a11y@happyloa-skills
```

應看到已啟用的 `taiwan-freego-a11y@happyloa-skills`、版本 `2.1.0`，以及一個 `taiwan-freego-a11y` Skill。若目前工作階段尚未載入，執行 `/reload-plugins`。

**一般使用不需要 npm 開發依賴。** 附帶的待檢清單工具需要 Python 3.10+；未使用工具時，Claude 仍可讀取規範與修正指引。

## 如何用在你的專案

在專案目錄啟動 Claude Code，明確呼叫：

```text
/taiwan-freego-a11y:taiwan-freego-a11y
```

後面接你要完成的工作，例如：

**開發／修正 UI**

```text
/taiwan-freego-a11y:taiwan-freego-a11y 依台灣115.11 AA檢查並直接修正結帳頁與共用元件，保留原本功能與視覺設計。執行可用的檢查，列出仍需人工驗證的項目。
```

**處理 Freego 報告**

```text
/taiwan-freego-a11y:taiwan-freego-a11y 讀取 reports/freego.html。先確認規範與工具版本，再依每筆完整訊息修正專案。保留代碼、URL、元素及重新檢測方式，遇到版本不符或無法確認的項目標示 Pending。
```

**準備檢測交付**

```text
/taiwan-freego-a11y:taiwan-freego-a11y 為這個專案建立115.11 AA稽核清單，涵蓋所有路由、登入狀態、表單錯誤與完整流程。依實際證據列出 Pass、Fail、Pending、Not applicable，並整理下一輪Freego與人工檢查步驟。
```

Claude 也可依任務內容自行選用此 Skill。明確呼叫可確保這次工作載入它。

## 它會幫你完成什麼

1. 確認規範版本、等級、頁面、狀態與完整流程。
2. 檢查原始碼、共用元件及可取得的渲染結果，按規範修正實際檔案。
3. 對應 Freego 完整訊息，避免用不同版本的相同代碼誤判。
4. 執行專案可用的建置、機器檢查及操作測試，重新驗證修正。
5. 提供附證據的結果，以及尚未完成的鍵盤、讀屏、媒體或流程檢查。

涵蓋替代文字、影音、表格、表單、對比、縮放與重排、鍵盤與焦點、手勢與拖曳、狀態訊息，以及登入／驗證／錯誤預防。

新版特別加入焦點不遮蔽、拖曳替代、最小目標尺寸、一致性幫助、冗餘輸入、無障礙認證等要求；也修正舊 Skill 的表單／表格代碼對應。

## 覆蓋範圍與版本

| 目標等級 | 有效成功準則（累計） | 機器檢測碼 C（累計） | 人工稽核碼 E（累計） |
| --- | ---: | ---: | ---: |
| A | 31 | 21 | 103 |
| **AA（預設）** | **55** | **23** | **161** |
| AAA | 86 | 28 | 216 |

完整清單包含每個附錄代碼的官方訊息、對應準則、等級與 PDF 頁碼。4.1.1 在新版已刪除，僅保留歷史紀錄。替代技術與常見失敗須依適用性判斷，不能把所有技術同時視為必做。

**115.11 新版標章認證自 2026-11-30 開始。** 可先依新版開發；實際送驗須使用官方接受的規範與工具版本。目前官方列出的 Freego 仍適用 110.07，不能把舊版掃描結果當成新版全部通過。詳見 [版本、官方來源與文件取得說明](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/references/sources-and-versions.md)。

## 如何完成 Freego 檢測

Skill 協助完成專案修正與稽核準備。實際交付仍需要這個循環：

1. 使用對應版本的官方 Freego 檢測可存取的測試網站，記錄範圍、設定與報告。
2. 將完整報告交給 Claude 修正，再重新執行 Freego 驗證相同 URL／狀態。
3. 完成鍵盤、螢幕閱讀器、版面、媒體與登入等適用的人工檢查。
4. 記錄例外理由，處理所有 Fail，完成所有適用的 Pending，再依官方程序送驗。

**Skill 是 AI 開發與稽核指引，不是 Freego 檢測引擎或標章證書。** 自動掃描與範例測試通過，只能證明已測的範圍；AI 的修正也需要重新驗證。

## 待檢清單工具

在此儲存庫根目錄執行：

```bash
python plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/scripts/audit_checklist.py --level AA > a11y-audit.md
```

支援 `--level A|AA|AAA`、`--format json`、`--report freego-report.html`。工具只產生 **Pending 清單**與辨識報告代碼，不會掃描網站、判讀報告成敗或推斷認證通過。Windows 可依 Python 安裝情況將 `python` 改成 `py`。

## 更新

在終端機執行：

```bash
claude plugin marketplace update happyloa-skills
claude plugin update taiwan-freego-a11y@happyloa-skills
```

目前工作階段可再執行 `/reload-plugins`。第三方 marketplace 的自動更新需在 `/plugin` → Marketplaces 啟用；不能假設預設開啟。

不使用 Plugin 時，也可將 `plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/` **完整資料夾**放入 `~/.claude/skills/` 或專案 `.claude/skills/`，並呼叫 `/taiwan-freego-a11y`。務必保留 references 與 scripts。

## 驗證、文件與回報

- [驗證方法與實際結果](docs/verification.md)：官方 CLI 安裝、獨立修正範例、瀏覽器檢查及未驗證範圍。
- [Skill 核心流程](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/SKILL.md)
- [完整成功準則](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/references/criteria-checklist.md)／[C 碼修正指引](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/references/machine-checks.md)／[C、E 完整清單](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/references/coverage.json)
- [人工驗證與報告格式](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/references/verification-and-reporting.md)
- [更新紀錄](CHANGELOG.md)／[貢獻與本機測試](CONTRIBUTING.md)／[問題回報](https://github.com/happyloa/taiwan-freego-a11y-skill/issues/new/choose)

## English

A Claude Code skill for developing, repairing, and auditing accessible websites in Taiwan. It targets **Taiwan 115.11 / WCAG 2.2 AA** by default, with all **86 active criteria, 28 C codes, and 216 E codes**. Default AA includes 55 criteria, 23 C codes, and 161 E codes cumulatively.

Install through the marketplace commands above, then invoke `/taiwan-freego-a11y:taiwan-freego-a11y` with your project task or full Freego report. The skill guides actual code changes, retesting, and evidence-based manual checks. A Python helper generates pending worksheets and recognizes report codes.

Revised certification starts November 30, 2026. Match the actual scanner and certification edition; current 110.07 reports do not establish 115.11 conformance. See [verification](docs/verification.md) for measured installation and repair results. The skill does not replace desktop Freego, screen-reader testing, or official certification.

## License

[MIT](LICENSE) applies to this repository's original implementation and guidance. Official standard excerpts are attributed to MODA; see the source notes for provenance.
