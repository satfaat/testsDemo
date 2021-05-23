const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://status.ecwid.com/');
  await page.screenshot({ path: 'status.png' });

  await browser.close();
})();