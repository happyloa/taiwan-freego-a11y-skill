module.exports = async () => {
  // Extract once before workers start; concurrent extraction can expose a partial binary.
  if (!process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH) {
    const bundled = (await import('@sparticuz/chromium')).default;
    process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH = await bundled.executablePath();
  }
};
