# 驗證紀錄

最近一次：2026-11-25，版本 2.3.0。

## 自動檢查

| 指令                   | 檢查內容                                                                                              |
| ---------------------- | ----------------------------------------------------------------------------------------------------- |
| `npm run validate`     | Claude Code CLI 嚴格驗證 marketplace 與 plugin，並檢查清單資料                                        |
| `npm test`             | 11 項 Python 測試：等級累計、代碼完整性、已刪除的 4.1.1、報告代碼辨識、UTF-8 輸出、文件連結           |
| `npm run test:install` | 在臨時 Claude 設定中用一步指令安裝，確認已啟用、版本一致、7 個 Skill 檔案與原始檔相同；不送出模型請求 |
| `npm run test:browser` | 7 項 Playwright 測試，用 axe-core 與實際操作檢查修正範例                                              |

CI 在每次 main 更新與 PR 時執行這四項，Linux 上使用 @sparticuz/chromium。結果見 [Actions](https://github.com/happyloa/taiwan-freego-a11y-skill/actions/workflows/validate.yml)。

2026-11-25 在 Windows 11、Node.js 26、Python 3.14 上四項全部通過，使用 Claude Code 2.1.332、Playwright 1.65.1、axe-core 4.14.1；瀏覽器測試以 `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH` 指定 Playwright 的 Chromium 159。`claude plugin install taiwan-freego-a11y --marketplace happyloa/taiwan-freego-a11y-skill` 能從 GitHub 安裝，2.1.0 升級到 2.2.0 的更新流程也實測過。

## Claude 行為 eval

[`evals/`](../plugins/taiwan-freego-a11y/evals/) 有 4 個 `claude plugin eval` 案例，提示用一般使用者的口吻寫，不點名 Skill：

- 修正結帳頁，寫出 `checkout.html`
- 判讀一份 110.07 Freego 報告（代碼與訊息取自實際輸出）
- 只稽核登入頁、不改檔
- 回答目標尺寸、4.1.1、Freego 版本與標章效期

2026-11-25 用 Claude Code 2.1.332 執行。Skill 在每次執行都會觸發。

**有無 Skill 的差距**（2.2.0，每題 2 次，Haiku 評分）：載入 Skill 四題都是 1.00。不載入時，稽核 0.80、規範問答 0.38、報告判讀 0.63，常見錯誤是不知道 110.07 申請截止與標章效期，以及 4.1.1 與 HM1130103C 的版本差異。修正結帳頁不載入也是 1.00，表示這題的評分標準對 Claude 偏簡單。

**2.2.0 與 2.3.0 比較**（每題 3 次，Sonnet 評分）：

| 案例         | 2.2.0 | 2.3.0 |
| ------------ | ----: | ----: |
| 修正結帳頁   |  1.00 |  1.00 |
| 只稽核登入頁 |  0.94 |  0.89 |
| 規範問答     |  1.00 |  0.93 |
| 報告判讀     |  1.00 |  1.00 |

2.3.0 依任務讀取參考檔：修正題不讀參考檔，問答題只讀 `sources-and-versions.md`。整套每次約便宜 6%，修正題約 16%。2.3.0 失分的回答都人工讀過，內容正確，失分來自評分器不穩定；「狀態只用四種」這條評分標準在兩版都有約一半判失敗。比較過程中發現 Skill 的一段實測紀錄會讓 Claude 說成是自己跑過 Freego，已改寫並重測，沒有再出現。

## Freego 實測

2026-11-25 用 Freego Dec 19 2025（110.07，搭配 ChromeDriver 158），以 AA 掃描本機示範頁：

| 頁面                                                  | 結果   | 回報的代碼                                                                |
| ----------------------------------------------------- | ------ | ------------------------------------------------------------------------- |
| [原始結帳頁](../tests/fixtures/checkout.before.html)  | 不通過 | HM1130102C（headers 指向不存在的 id）、HM1130103C（fieldset 沒有 legend） |
| [Codex 修正版](../tests/fixtures/checkout.after.html) | 通過   |                                                                           |
| 2.3.0 eval 中 Claude 寫出的兩份修正版                 | 通過   |                                                                           |
| eval 用的登入頁                                       | 不通過 | HM1110100C、HM1130104C、HM1310100C、HM1410200C                            |

110.07 報告的 HM1130103C 是 fieldset/legend 檢查，115.11 把這項編為 HM1130105C，115.11 的 HM1130103C 則是 select/optgroup。登入頁上 Freego 沒有回報：沒有 label 的 select、當按鈕用的 `div`、對比不足、密碼欄禁止貼上、沒有替代方案的文字驗證碼、16px 圖示按鈕的尺寸、可能遮住焦點的固定橫幅。這些要人工檢查。

這次掃描只能證明 110.07 引擎的結果。官方推出 115.11 版 Freego 後，要用同一組頁面重掃，對照代碼與 `coverage.json`。

## 修正範例

[原始結帳頁](../tests/fixtures/checkout.before.html)有缺少 legend、headers 參照錯誤、只能拖曳排序、目標過小、地址要重填、密碼與驗證碼禁止貼上等問題。[修正版](../tests/fixtures/checkout.after.html)由新對話中的獨立 Codex 代理產生（2026-10-08），代理只拿到已安裝的 Skill 與原始 HTML，[修正報告](../tests/fixtures/checkout-audit.md)也一併保留。2026-11-26 手動把地址欄位的 `autocomplete` 改為 `shipping address-line1`（原本的 `street-address` 是多行欄位用的值）。上面的 Freego 結果是改動前的版本，改動後沒有重掃。

[瀏覽器測試](../tests/browser/checkout.spec.js)先確認原始頁面的缺失仍在，再檢查修正版：

- 1280px 與 320px 下，初始與錯誤狀態通過選定的 WCAG A／AA axe 規則
- 點擊與鍵盤排序、焦點保留與狀態訊息
- 地址沿用、切換與自訂資料保留
- 密碼與 OTP 不阻擋貼上事件，autocomplete 正確
- 錯誤辨識、檢查、返回更正、確認送出與完成狀態
- 320px 重排、中文文字間距覆寫、按鈕尺寸與 Tab 焦點可見

測試會載入 Noto Sans TC 400／700 並等字型載入完成，避免中文缺字影響版面判斷。固定的修正版只是回歸樣本，不能證明 AI 每次都答對。貼上測試只確認事件沒有被取消，沒有測作業系統剪貼簿或密碼管理員。

## 尚未驗證

- 115.11 版 Freego（尚未發布）與官方檢測通過報告。
- NVDA／VoiceOver 實際操作。accessibility tree 檢查不能取代螢幕閱讀器。
- 真實後端驗證、第三方內容、多路由、完整媒體與所有規範情境。
- 政府無障礙標章。

完整網站仍要依[驗證流程](../plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/references/verification-and-reporting.md)完成 Freego 與人工檢查。
