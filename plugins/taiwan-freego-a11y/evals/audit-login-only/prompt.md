---
description: Audit-only request; no files are written and results use evidence statuses.
tags: [audit]
runs: 2
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---

下面是會員登入頁。請依台灣 115.11 AA 幫我做無障礙稽核，只要稽核結果，先不要改檔案、不要產生修正版。

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>頁面</title>
    <style>
      body {
        font-family: sans-serif;
        margin: 0;
        color: #999;
        background: #fff;
      }
      .cookie {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        height: 140px;
        background: #222;
        color: #fff;
        padding: 1rem;
      }
      .icon {
        width: 16px;
        height: 16px;
        padding: 0;
        border: 0;
        background: none;
      }
      .error {
        color: red;
      }
    </style>
  </head>
  <body>
    <main>
      <h2>會員登入</h2>
      <form>
        <label for="account">帳號</label><input id="account" />
        <input
          id="pw"
          type="password"
          placeholder="密碼"
          onpaste="return false;"
        />
        <img src="captcha.png" />
        <input id="captcha" placeholder="請輸入圖中文字" />
        <button class="icon" type="button"><img src="refresh.svg" /></button>
        <select id="region">
          <option>台北</option>
          <option>新北</option>
        </select>
        <p class="error">紅色欄位有誤</p>
        <div onclick="login()">登入</div>
      </form>
    </main>
    <div class="cookie">本站使用 Cookie。<button>同意</button></div>
  </body>
</html>
```
