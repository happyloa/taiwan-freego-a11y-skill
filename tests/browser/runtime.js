const { test: base, expect, chromium } = require('@playwright/test');
const test = base.extend({
  browser: [async ({}, use) => {
    const bundled = (await import('@sparticuz/chromium')).default;
    const executablePath = process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH || await bundled.executablePath();
    // Chromium's single-process mode cannot reliably recycle Playwright contexts.
    const args = bundled.args.filter(argument => argument !== '--single-process');
    const browser = await chromium.launch({ executablePath, args, headless: true });
    await use(browser);
    await browser.close();
  }, { scope: 'worker' }]
});
module.exports = { test, expect };
