const { test, expect } = require('./runtime');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const url = name => pathToFileURL(path.resolve(__dirname, '../fixtures/checkout.' + name + '.html')).href;
const order = page => page.locator('#product-list > li h3').allTextContents();
async function open(page, name) {
  await page.goto(url(name));
  for (const weight of [400, 700]) {
    await page.addStyleTag({ url: pathToFileURL(require.resolve('@fontsource/noto-sans-tc/' + weight + '.css')).href });
  }
  await page.addStyleTag({ content: '*{font-family:"Noto Sans TC",sans-serif!important}' });
  await page.evaluate(() => document.fonts.ready);
  expect(await page.evaluate(() => [...document.fonts].some(font =>
    font.family.includes('Noto Sans TC') && font.status === 'loaded'))).toBe(true);
}
async function scan(page) {
  await page.addScriptTag({ path: require.resolve('axe-core/axe.min.js') });
  return page.evaluate(async () => {
    const result = await axe.run(document, {
      runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'] }
    });
    return result.violations.map(item => ({ id: item.id, targets: item.nodes.map(node => node.target) }));
  });
}

test('baseline retains defects that the repaired fixture addresses', async ({ page }) => {
  await open(page, 'before');
  await expect(page.locator('fieldset legend')).toHaveCount(0);
  expect(await page.locator('[headers]').evaluateAll(nodes => nodes.some(node =>
    node.getAttribute('headers').split(/\s+/).some(id => !document.getElementById(id))))).toBe(true);
  expect(await page.locator('#password').evaluate(node => {
    const event = new ClipboardEvent('paste', { bubbles: true, cancelable: true });
    node.dispatchEvent(event); return event.defaultPrevented;
  })).toBe(true);
  const tiny = await page.locator('.tiny').first().boundingBox();
  expect(tiny.width).toBeLessThan(24);
});

for (const width of [1280, 320]) {
  test('repaired initial and error states pass scoped axe checks at ' + width + 'px', async ({ page }) => {
    await page.setViewportSize({ width, height: 800 });
    await open(page, 'after');
    expect(await scan(page)).toEqual([]);
    await page.getByRole('button', { name: '檢查訂單', exact: true }).click();
    await expect(page.locator('#errors')).toBeVisible();
    expect(await scan(page)).toEqual([]);
  });
}

test('pointer and keyboard alternatives reorder cards without losing focus', async ({ page }) => {
  await open(page, 'after');
  await page.getByRole('button', { name: '下移商品 A', exact: true }).click();
  expect(await order(page)).toEqual(['商品 B', '商品 A']);
  await expect(page.getByRole('button', { name: '下移商品 A', exact: true })).toBeFocused();
  await page.locator('#item-a').focus();
  await page.keyboard.press('ArrowUp');
  expect(await order(page)).toEqual(['商品 A', '商品 B']);
  await expect(page.locator('#item-a')).toBeFocused();
  await page.getByRole('button', { name: '上移商品 B', exact: true }).focus();
  await page.keyboard.press('Enter');
  expect(await order(page)).toEqual(['商品 B', '商品 A']);
  await expect(page.locator('#sort-status')).toContainText('商品 B');
});

test('repeated address is available and authentication fields allow paste events', async ({ page }) => {
  await open(page, 'after');
  await expect(page.locator('#address')).toHaveValue('臺北市中正區示範路 1 號');
  await expect(page.locator('#address')).toHaveAttribute('autocomplete', 'shipping street-address');
  await page.getByLabel('沿用上一步帳單地址', { exact: true }).uncheck();
  await page.locator('#address').fill('新竹縣竹東鎮示範路 2 號');
  await page.getByLabel('沿用上一步帳單地址', { exact: true }).check();
  await expect(page.locator('#address')).toHaveValue('臺北市中正區示範路 1 號');
  await page.getByLabel('沿用上一步帳單地址', { exact: true }).uncheck();
  await expect(page.locator('#address')).toHaveValue('新竹縣竹東鎮示範路 2 號');
  for (const id of ['password', 'otp']) {
    expect(await page.locator('#' + id).evaluate(node => {
      const event = new ClipboardEvent('paste', { bubbles: true, cancelable: true });
      node.dispatchEvent(event); return event.defaultPrevented;
    })).toBe(false);
  }
  await expect(page.locator('#password')).toHaveAttribute('autocomplete', 'current-password');
  await expect(page.locator('#otp')).toHaveAttribute('autocomplete', 'one-time-code');
});

test('errors, review, correction and confirmation form an operable process', async ({ page }) => {
  await open(page, 'after');
  await page.getByRole('button', { name: '檢查訂單', exact: true }).click();
  await expect(page.locator('#errors')).toBeFocused();
  await expect(page.locator('#password')).toHaveAttribute('aria-invalid', 'true');
  await page.locator('#password').fill('test-password');
  await page.locator('#otp').fill('123456');
  await page.getByRole('button', { name: '檢查訂單', exact: true }).click();
  await expect(page.locator('#review-heading')).toBeFocused();
  expect(await scan(page)).toEqual([]);
  await page.getByRole('button', { name: '返回更正訂單', exact: true }).click();
  await expect(page.locator('#otp')).toHaveValue('123456');
  await page.getByRole('button', { name: '檢查訂單', exact: true }).click();
  await page.getByRole('button', { name: '確認送出示範訂單', exact: true }).click();
  await expect(page.locator('#completion-heading')).toBeFocused();
  await expect(page.locator('#checkout-status')).toContainText('示範訂單已完成');
  expect(await scan(page)).toEqual([]);
});

test('320px reflow and tab stops retain visible controls after text spacing override', async ({ page }) => {
  await page.setViewportSize({ width: 320, height: 800 });
  await open(page, 'after');
  await page.addStyleTag({ content: '*{line-height:1.5!important;letter-spacing:.14em!important;word-spacing:.16em!important}p{margin-bottom:2em!important}' });
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
  for (const button of await page.locator('button:visible').all()) {
    const rect = await button.boundingBox();
    expect(rect.width).toBeGreaterThanOrEqual(24);
    expect(rect.height).toBeGreaterThanOrEqual(24);
  }
  for (let index = 0; index < 25; index++) {
    await page.keyboard.press('Tab');
    expect(await page.evaluate(() => {
      const node = document.activeElement;
      if (node === document.body) return true;
      const r = node.getBoundingClientRect();
      const x = Math.min(innerWidth - 1, Math.max(0, r.left + r.width / 2));
      const y = Math.min(innerHeight - 1, Math.max(0, r.top + r.height / 2));
      const top = document.elementFromPoint(x, y);
      return r.right > 0 && r.left < innerWidth && r.bottom > 0 && r.top < innerHeight &&
        top && (node === top || node.contains(top));
    })).toBe(true);
  }
});
