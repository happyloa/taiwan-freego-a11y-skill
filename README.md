# taiwan-freego-a11y

[Claude Code](https://code.claude.com/docs/en/skills) Skill，讓 Claude 在建立、修改及稽核網頁 UI 時，套用台灣 **《網站無障礙規範 (115.11)》／WCAG 2.2**，預設目標 **AA**。

**2.0.0** 已改用新版完整清單，包含 A／AA／AAA 的 **86 項有效成功準則、28 個機器檢測碼（C）、216 個人工稽核碼（E）**。4.1.1 已刪除，保留歷史紀錄但不算有效要求。

新版於 2026-05-29 公布，**2026-11-30** 起用於新版標章認證；目前可先依新版開發。參考 [官方公告](https://accessibility.moda.gov.tw/News/Detail/5608?Category=43)及 [來源、版本與文件取得說明](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/references/sources-and-versions.md)。

## 覆蓋範圍

| 目標等級 | 有效成功準則（累計） | C 碼（累計） | E 碼（累計） |
| --- | ---: | ---: | ---: |
| A | 31 | 21 | 103 |
| AA（預設） | 55 | 23 | 161 |
| AAA | 86 | 28 | 216 |

- 補齊媒體替代、結構、表格、表單、對比、縮放、重排、鍵盤、讀屏、指標操作及完整流程檢查。
- 納入新版 AA 範圍的六項要求：焦點不遮蔽、拖曳替代、最小目標尺寸、一致性幫助、冗餘輸入、無障礙認證；另外保留 AAA 的更嚴格要求。
- 修正表單／表格代碼：`HM1130103C` 是選項群組，`HM1130105C` 才是 fieldset／legend。
- 附上每個 C／E 碼的官方訊息、對應準則及 PDF 頁碼，並區分規範要求、替代技術與常見失敗。
- 稽核結果須區分 Pass／Fail／Pending／Not applicable，附實際證據；未執行的人工檢查保持 Pending。

這是完整的規範對照與修正工作流。**不代表單靠 Skill 或機器掃描就能證明網站全部通過**；鍵盤、讀屏、媒體及登入流程等仍需實測。各版 Freego 的實際執行能力，也須另外確認。

## 安裝

在 Claude Code 中加入 marketplace，再安裝 plugin：

```text
/plugin marketplace add happyloa/taiwan-freego-a11y-skill
/plugin install taiwan-freego-a11y@happyloa-skills
```

已安裝者可在終端機更新：

```bash
claude plugin marketplace update happyloa-skills
claude plugin update taiwan-freego-a11y@happyloa-skills
```

也可複製**完整 Skill 資料夾**，包含 references 與 scripts：

```bash
git clone https://github.com/happyloa/taiwan-freego-a11y-skill.git
mkdir -p ~/.claude/skills
cp -r taiwan-freego-a11y-skill/plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y ~/.claude/skills/
```

單一專案可改放 `<project>/.claude/skills/`。Fork 使用者請將 marketplace 來源改成自己的 `owner/repo`。

## 使用

Claude 可依 description 選用此 Skill，也可明確呼叫：

- Plugin：`/taiwan-freego-a11y:taiwan-freego-a11y`
- 複製資料夾：`/taiwan-freego-a11y`

例如：「依台灣 115.11 AA 檢查這個結帳流程，修正問題並列出還需要人工驗證的項目。」

產生完整 AA 待檢清單（需要 Python 3，僅使用標準函式庫）：

```bash
python plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/scripts/audit_checklist.py --level AA > a11y-audit.md
```

可使用 `--level A`／`AAA`、`--format json`，或 `--report freego-report.html` 辨識報告代碼。**這個工具產生待檢清單，不會掃描網站，也不會由代碼出現與否推斷通過。**

## 內容與驗證

- [SKILL.md](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/SKILL.md)：核心開發與稽核流程。
- [完整成功準則](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/references/criteria-checklist.md)：各等級檢查方法。
- [C 碼修正指引](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/references/machine-checks.md)及 [C／E 完整清單](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/references/coverage.json)。
- [人工驗證與報告](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/references/verification-and-reporting.md)：測試範圍、證據與完成條件。
- [來源與版本](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/references/sources-and-versions.md)：官方資料、取得方式及舊版差異。

在儲存庫根目錄執行：

```bash
python plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/scripts/audit_checklist.py --validate
python -m unittest discover -s tests -v
```

## English

A Claude Code skill for Taiwan **網站無障礙規範 (115.11) / WCAG 2.2**, targeting **AA by default**. Version **2.0.0** includes all **86 active criteria**, **28 C codes**, and **216 E codes**, with official appendix messages and source pages. Default AA covers **55 criteria, 23 C codes, and 161 E codes** cumulatively. Deleted 4.1.1 is retained only as a historical entry.

The revision was published on May 29, 2026; revised certification starts November 30, 2026. The skill distinguishes normative coverage from a specific Freego version's runtime behavior. It includes the new focus, dragging, target-size, consistent-help, redundant-entry, and accessible-authentication requirements, plus stricter AAA checks.

Install using the marketplace commands above, or copy the entire skill directory, including its references and scripts. Invoke `/taiwan-freego-a11y:taiwan-freego-a11y` for the plugin or `/taiwan-freego-a11y` for a folder installation. Use the Python helper to generate a pending worksheet or recognize report codes; it does not scan a website or infer pass results.

Assess complete pages and processes. Record Pass / Fail / Pending / Not applicable with evidence. Keyboard, screen-reader, visual, media, and authentication checks still require actual testing; the skill does not guarantee government certification. See [sources and version notes](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/references/sources-and-versions.md) for provenance and migration details.

## 授權 / License

MIT — see [LICENSE](LICENSE). Official standard excerpts are attributed to MODA; the MIT license applies to this repository's original implementation and guidance.
