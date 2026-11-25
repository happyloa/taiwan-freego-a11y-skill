# 驗證紀錄

最近一次：2026-11-25，版本 2.2.0。

## 檢查項目

| 指令                   | 檢查內容                                                                                              |
| ---------------------- | ----------------------------------------------------------------------------------------------------- |
| `npm run validate`     | Claude Code CLI 嚴格驗證 marketplace 與 plugin，並檢查清單資料                                        |
| `npm test`             | 11 項 Python 測試：等級累計、代碼完整性、已刪除的 4.1.1、報告代碼辨識、UTF-8 輸出、文件連結           |
| `npm run test:install` | 在臨時 Claude 設定中用一步指令安裝，確認已啟用、版本一致、7 個 Skill 檔案與原始檔相同；不送出模型請求 |
| `npm run test:browser` | 7 項 Playwright 測試，用 axe-core 與實際操作檢查修正範例                                              |

CI 在每次 main 更新與 PR 時執行這四項，Linux 上使用 @sparticuz/chromium。結果見 [Actions](https://github.com/happyloa/taiwan-freego-a11y-skill/actions/workflows/validate.yml)。

## 2026-11-25 結果

Windows 11、Node.js 26、Python 3.14 上四項全部通過，使用 Claude Code 2.1.332、Playwright 1.65.1、axe-core 4.14.1。瀏覽器測試以 `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH` 指定 Playwright 的 Chromium 159。另外確認：

- `claude plugin install taiwan-freego-a11y --marketplace happyloa/taiwan-freego-a11y-skill` 能從 GitHub 安裝當時公開的 2.1.0。
- npm 10.9（Node.js 22 內建）能用新的 lockfile 執行 `npm ci`。

2.1.0 發布時（2026-10-08）已從公開 GitHub 來源安裝，並實測 2.0.0 升級到 2.1.0 的更新流程。

## 修正範例

[原始結帳頁](../tests/fixtures/checkout.before.html)、[修正版](../tests/fixtures/checkout.after.html)、[代理的修正報告](../tests/fixtures/checkout-audit.md)、[瀏覽器測試](../tests/browser/checkout.spec.js)。

原始頁面有缺少 legend、headers 參照錯誤、只能拖曳排序、目標過小、地址要重填、密碼與驗證碼禁止貼上等問題。修正版由新對話中的獨立 Codex 代理產生（2026-10-08），代理只拿到已安裝的 Skill 與原始 HTML，沒有拿到缺失清單或預期修法。

瀏覽器測試先確認原始頁面的缺失仍在，再檢查修正版：

- 1280px 與 320px 下，初始與錯誤狀態通過選定的 WCAG A／AA axe 規則
- 點擊與鍵盤排序、焦點保留與狀態訊息
- 地址沿用、切換與自訂資料保留
- 密碼與 OTP 不阻擋貼上事件，autocomplete 正確
- 錯誤辨識、檢查、返回更正、確認送出與完成狀態
- 320px 重排、中文文字間距覆寫、按鈕尺寸與 Tab 焦點可見

測試會載入 Noto Sans TC 400／700 並等字型載入完成，避免中文缺字影響版面判斷。CI 不會重新產生 AI 修正版；固定的修正版只是回歸樣本，不能證明 AI 每次都答對。貼上測試只確認事件沒有被取消，沒有測作業系統剪貼簿或密碼管理員。

## 尚未驗證

- 登入後的 Claude 模型流程。曾直接執行 slash command，環境回覆 `Not logged in`；修正範例改用 Codex 代理，模型、工具權限與結果可能和 Claude 不同。
- 桌面版 Freego 實測與官方檢測通過報告。
- NVDA／VoiceOver 實際操作。accessibility tree 檢查不能取代螢幕閱讀器。
- 真實後端驗證、第三方內容、多路由、完整媒體與所有規範情境。
- 政府無障礙標章。

完整網站仍要依[驗證流程](../plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/references/verification-and-reporting.md)完成 Freego 與人工檢查。
