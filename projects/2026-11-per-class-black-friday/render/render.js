// usage: node render.js <out.mp4> [seconds] [stillFrame]
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');
const out = process.argv[2]; const SECS = +(process.argv[3] || 9); const still = process.argv[4];
const FPS = 24;
(async () => {
  const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(__dirname, 'index.html'));
  await page.evaluate(() => window.ready);
  if (still !== undefined) {
    await page.evaluate(([f, fps]) => window.setFrame(f, fps), [+still, FPS]);
    await page.screenshot({ path: out }); await browser.close(); return;
  }
  const ff = spawn('ffmpeg', ['-y', '-v', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
    '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo', '-shortest',
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '16', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-movflags', '+faststart', out],
    { stdio: ['pipe', 'inherit', 'inherit'] });
  for (let f = 0; f < SECS * FPS; f++) {
    await page.evaluate(([f, fps]) => window.setFrame(f, fps), [f, FPS]);
    const buf = await page.screenshot({ type: 'png' });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  }
  ff.stdin.end(); await new Promise(r => ff.on('close', r)); await browser.close();
})();
