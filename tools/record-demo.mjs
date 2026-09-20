import { chromium } from 'playwright-core';

const targetMs = Math.max(90000, Number(process.env.TARGET_MS || 150000));
const startedAt = Date.now();

const browser = await chromium.launch({
  headless: false,
  executablePath: process.env.CHROME_PATH || '/usr/bin/google-chrome',
  args: ['--no-sandbox', '--disable-dev-shm-usage', '--start-maximized', '--autoplay-policy=no-user-gesture-required']
});

const context = await browser.newContext({
  viewport: null,
  locale: 'en-GB'
});

const page = await context.newPage();
await page.goto(process.env.DEMO_URL || 'http://127.0.0.1:3000', { waitUntil: 'networkidle' });

await page.evaluate(() => localStorage.clear());
await page.reload({ waitUntil: 'networkidle' });

const voiceToggle = page.locator('#voiceToggle');
if (await voiceToggle.isChecked()) await voiceToggle.uncheck();

await page.screenshot({ path: 'media/01-opening.png', fullPage: true });
await page.waitForTimeout(1200);

await page.click('#judgeDemoBtn');
await page.waitForTimeout(6000);
await page.screenshot({ path: 'media/02-yasmin-presents.png', fullPage: true });

await page.waitForFunction(() => document.querySelector('#strategy')?.textContent?.toLowerCase().includes('visual')
  || document.querySelector('#strategy')?.textContent?.toLowerCase().includes('number')
  || document.querySelector('#strategy')?.textContent?.toLowerCase().includes('everyday'),
  { timeout: 60000 }).catch(() => {});
await page.screenshot({ path: 'media/03-adaptation.png', fullPage: true });

await page.waitForFunction(() => document.querySelector('#presenterText')?.textContent?.includes('“Okay”')
  || document.querySelector('#decision')?.textContent?.toLowerCase().includes('false')
  || document.querySelector('#strategy')?.textContent?.toLowerCase().includes('evidence'),
  { timeout: 90000 }).catch(() => {});
await page.screenshot({ path: 'media/04-no-false-mastery.png', fullPage: true });

await page.waitForFunction(() => document.querySelector('#phase')?.textContent?.toLowerCase().includes('complete'),
  { timeout: 120000 }).catch(() => {});
await page.screenshot({ path: 'media/05-rubric-complete.png', fullPage: true });

await page.waitForFunction(() => document.querySelector('#demoProgressText')?.textContent?.includes('Demo complete'),
  { timeout: 140000 }).catch(() => {});

await page.screenshot({ path: 'media/06-memory.png', fullPage: true });

await page.click('#smartSessionBtn').catch(() => {});
await page.waitForTimeout(5000);
await page.screenshot({ path: 'media/07-next-session.png', fullPage: true });

const remaining = targetMs - (Date.now() - startedAt);
if (remaining > 0) await page.waitForTimeout(remaining);

await browser.close();
