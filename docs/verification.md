# 可用性驗證

驗證日期：2026-10-08。目標版本：2.1.0。

## 驗證方式

| 層次 | 做法 | 證據範圍 |
| --- | --- | --- |
| 封裝 | 官方 Claude Code 2.1.293 的嚴格驗證 | marketplace、plugin 與 Skill 能被解析 |
| 安裝 | 隔離 Claude 設定，新增 marketplace、安裝、列出與檢查元件 | 可安裝、已啟用、技能可被辨識，7 個 Skill 資源與來源內容一致 |
| 規範清單 | Python 目錄驗證與單元測試 | 等級累計、完整代碼、刪除項目、報告代碼識別、輸出與文件一致性 |
| AI 修正 | 新對話的獨立 Codex 代理，只提供已安裝的 Skill 與原始結帳頁 | 代理讀取 Skill 後產生修正版；未提供預期診斷或修法 |
| 實際操作 | Playwright 1.64.0、Chromium 153.0.8010.0、axe-core 4.14.0 | 本機範例的語意、排序、地址沿用、貼上事件、錯誤／確認流程與窄版面 |

本機結果：官方嚴格驗證與隔離安裝成功、10 項 Python 測試通過、7 項
瀏覽器回歸檢查通過。瀏覽器測試載入 Noto Sans TC 5.3.0 的 400／700
字型並等待載入完成，避免把中文字型缺字方塊當成實際文字排版證據。

首次 GitHub 安裝使用 README 的公開 repository 來源，成功安裝 2.0.0。
2.1.0 通過本機 marketplace 的隔離安裝測試，發布後亦從公開 GitHub 來源
重新安裝成功，確認版本為 2.1.0、已啟用，7 個 Skill 資源與來源內容一致。
官方 CLI 的 `plugin details` 可辨識一個 taiwan-freego-a11y Skill。
安裝與元件檢查不需要發送模型 API 請求。

更新流程也經過實測：在隔離設定中，將公開 marketplace 快取還原至
2.0.0 發布 commit 並安裝舊版，再依 README 執行 marketplace update 與
plugin update。結果成功更新為 2.1.0、維持啟用，7 個 Skill 資源與新版來源一致。

[2.1.0 的 GitHub CI 執行紀錄](https://github.com/happyloa/taiwan-freego-a11y-skill/actions/runs/37782055753)
已通過嚴格驗證、10 項 Python 測試、隔離安裝及 7 項瀏覽器測試，
使用乾淨的 Ubuntu runner 與預設 Chromium 解壓流程。

## 修正範例

- [原始結帳頁](../tests/fixtures/checkout.before.html)
- [使用 Skill 產生的修正版](../tests/fixtures/checkout.after.html)
- [代理的修正與驗證報告](../tests/fixtures/checkout-audit.md)
- [瀏覽器回歸檢查](../tests/browser/checkout.spec.js)

原始頁面包含缺少 legend、破損 headers 參照、拖曳與鍵盤排序問題、
過小目標、地址重填、密碼／驗證碼禁止貼上等情境。驗證代理只收到原始
HTML 與任務，沒有收到這份缺失清單或預先寫好的修正版。

回歸檢查包含原始缺失基線，並驗證修正版：

- 初始與錯誤狀態在 1280px、320px 的選定 WCAG A／AA axe 規則。
- 點擊與鍵盤排序、焦點保留及狀態訊息。
- 地址沿用、切換與自訂資料保留。
- 密碼與 OTP 不阻擋貼上事件，以及適當 autocomplete。
- 錯誤辨識、檢查、返回更正、確認送出與完成狀態。
- 320px 重排、中文文字間距覆寫、可見按鈕尺寸及 Tab 焦點可見性。

已固定修正版作為回歸樣本。CI 不會重新產生 AI 修正版，亦不測試模型
每次回答的一致性；AI 輸出仍需審查與重新測試。貼上事件測試只確認
事件未被取消，不等於測過作業系統剪貼簿或所有密碼管理員。

## 可重現的檢查

```bash
npm ci
npm run validate
npm test
npm run test:install
npm run test:browser
```

Node.js 22+、Python 3.10+。開發依賴包含固定版本的 Claude CLI、Playwright、
axe-core 與 Linux headless Chromium；這些不是 Skill 使用者的必備安裝。
預設瀏覽器回歸環境為 Linux x64。其他環境可設定
`PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH` 指向相容的 Chromium；正式網站仍須
依使用者平台另外驗證。CI 對每次 main 更新與 PR 執行以上檢查。

## 尚未證明的範圍

- 曾直接執行 Claude 的 slash-command 稽核請求；環境回覆
  `Not logged in · Please run /login`，模型 API 執行時間與費用均為 0。
  因此尚未完成登入後的 Claude 模型流程。AI 行為驗證使用獨立 Codex 代理，
  與 Claude 的模型、工具權限及執行結果可能不同。
- 未啟動 Windows／macOS 桌面 Freego，也沒有取得官方檢測通過報告。
- 未實際執行 NVDA／VoiceOver；瀏覽器與 accessibility tree 檢查不能取代讀屏。
- 範例沒有真實驗證後端、第三方內容、多路由、完整媒體或所有規範情境。
- 尚未取得政府無障礙標章；清單完整與範例通過不代表任何專案自動認證通過。

因此可確認封裝、安裝、資源與已測範例的修正效果；完整網站仍須按
[驗證流程](../plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/references/verification-and-reporting.md)
完成相應 Freego 與人工檢查。
