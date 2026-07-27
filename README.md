# taiwan-freego-a11y

這是一個 [Claude Code](https://code.claude.com) **Skill**，讓 Claude 在撰寫、編輯或審查網頁 UI 時，自動套用台灣**《網站無障礙規範 2.0》**（等同 **WCAG 2.0 AA**）——即政府 **Freego** 檢測器所驗查的規則。

預設強制執行以下規範：

- **相對字型大小**（rem / em / % / 具名值，禁用 px）— Freego `CS2140401C`
- **表單控制項標籤**（`<label for>` + `id`，或 `aria-label`）— Freego `HM1130104C`
- **`<fieldset>` 第一個子元素須為 `<legend>`**（`aria-label` 不能取代）— Freego `HM1130103C`
- **表格標頭 `scope`** + `<caption>`（空角格使用 `<td>`）— Freego `HM1130101C`
- **AA 色彩對比度 ≥ 4.5:1**（例如：避免以 Tailwind `gray-400` 顯示輔助文字）
- **標題層級**（唯一 `<h1>`、不跳級、視覺上的標題須標記為對應層級的 `<h1>`–`<h6>`）— WCAG 2.0 AA
- ARIA 模式：錯誤訊息用 `role="alert"`、裝飾性元素用 `aria-hidden`、`aria-pressed` / `aria-expanded`、離屏選單用 `inert`、`lang` 屬性與可縮放的 viewport

完整規則詳見：[`plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/SKILL.md`](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/SKILL.md)。

---

## 安裝方式 A：以 Plugin 安裝（推薦，可自動更新）

在 Claude Code 中，將此 repo 加入 marketplace，再安裝 plugin：

```text
/plugin marketplace add happyloa/taiwan-freego-a11y-skill
/plugin install taiwan-freego-a11y@happyloa-skills
```

（若您已 fork 此 repo，請將 `happyloa/taiwan-freego-a11y-skill` 替換為您的 `owner/repo`。）

日後更新：

```text
/plugin marketplace update
/plugin update taiwan-freego-a11y@happyloa-skills
```

## 安裝方式 B：複製 Skill 資料夾（最簡單，無需 Plugin）

```bash
git clone https://github.com/happyloa/taiwan-freego-a11y-skill.git
# 個人全域（所有專案適用）：
cp -r taiwan-freego-a11y-skill/plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y ~/.claude/skills/
# 或僅限單一專案：cp -r ... <your-project>/.claude/skills/
```

## 使用方式

Claude 會根據 Skill 的 `description` **自動啟用**此技能——只要您正在處理網頁 UI（表單、表格、按鈕、樣式）即會觸發。也可手動呼叫：

- Plugin 安裝：`/taiwan-freego-a11y:taiwan-freego-a11y`
- 方式 B（資料夾複製）：`/taiwan-freego-a11y`

---

## 儲存庫結構

```text
taiwan-freego-a11y-skill/
├── .claude-plugin/
│   └── marketplace.json                 # marketplace 目錄（方式 A）
├── plugins/
│   └── taiwan-freego-a11y/
│       ├── .claude-plugin/
│       │   └── plugin.json              # plugin 設定檔
│       ├── skills/
│       │   └── taiwan-freego-a11y/
│       │       └── SKILL.md             # Skill 本體
│       └── README.md
├── README.md
└── LICENSE
```

## 授權

MIT — 詳見 [LICENSE](LICENSE)。

---

# English

A [Claude Code](https://code.claude.com) **skill** that makes Claude apply Taiwan's
**《網站無障礙規範 2.0》**（≡ **WCAG 2.0 AA**）accessibility patterns — the rules the
government **Freego** scanner checks — whenever it writes, edits, or reviews web UI.

It enforces, by default:

- **Relative `font-size`** (rem/em/%/named, never px) — Freego `CS2140401C`
- **Labelled form controls** (`<label for>`+`id`, or `aria-label`) — Freego `HM1130104C`
- **`<fieldset>` first child must be `<legend>`** (`aria-label` alone doesn't satisfy it) — Freego `HM1130103C`
- **Table header `scope`** + `<caption>` (empty corner = `<td>`) — Freego `HM1130101C`
- **AA colour contrast ≥ 4.5:1** (e.g. avoid Tailwind `gray-400` for muted text)
- **Heading hierarchy** (one `<h1>`, no skipped levels, visual titles marked up as real `<h1>`–`<h6>`) — WCAG 2.0 AA
- ARIA patterns: `role="alert"` errors, `aria-hidden` decor, `aria-pressed` /
  `aria-expanded`, `inert` off-canvas, `lang` + zoomable viewport

Full rules: [`plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/SKILL.md`](plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y/SKILL.md).

---

## Install — Option A: as a plugin (recommended, auto-updates)

In Claude Code, add this repo as a marketplace, then install the plugin:

```text
/plugin marketplace add happyloa/taiwan-freego-a11y-skill
/plugin install taiwan-freego-a11y@happyloa-skills
```

(Replace `happyloa/taiwan-freego-a11y-skill` with your `owner/repo` if you fork it.)

Update later with:

```text
/plugin marketplace update
/plugin update taiwan-freego-a11y@happyloa-skills
```

## Install — Option B: copy the skill folder (simplest, no plugin)

```bash
git clone https://github.com/happyloa/taiwan-freego-a11y-skill.git
# personal (all projects):
cp -r taiwan-freego-a11y-skill/plugins/taiwan-freego-a11y/skills/taiwan-freego-a11y ~/.claude/skills/
# or project-only: cp -r ... <your-project>/.claude/skills/
```

## Usage

Claude **auto-invokes** the skill based on its `description` whenever you work on web UI
(forms, tables, buttons, styling). You can also call it explicitly:

- Plugin install: `/taiwan-freego-a11y:taiwan-freego-a11y`
- Folder copy (Option B): `/taiwan-freego-a11y`

---

## Repository layout

```text
taiwan-freego-a11y-skill/
├── .claude-plugin/
│   └── marketplace.json                 # marketplace catalog (Option A)
├── plugins/
│   └── taiwan-freego-a11y/
│       ├── .claude-plugin/
│       │   └── plugin.json              # plugin manifest
│       ├── skills/
│       │   └── taiwan-freego-a11y/
│       │       └── SKILL.md             # the skill itself
│       └── README.md
├── README.md
└── LICENSE
```

## License

MIT — see [LICENSE](LICENSE).
