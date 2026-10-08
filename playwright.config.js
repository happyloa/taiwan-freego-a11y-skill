const { defineConfig } = require('@playwright/test');
module.exports = defineConfig({
  testDir: './tests/browser',
  globalSetup: require.resolve('./tests/browser/setup.js'),
  fullyParallel: true,
  workers: 2,
  retries: 0,
  reporter: 'list',
  use: { viewport: { width: 1280, height: 800 } }
});
