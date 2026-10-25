#!/usr/bin/env python3
"""Build index.html for GitHub Pages from the app page source.

    python3 build.py <source.html>

The source is the page as written for the claude.ai artifact (title and styles
first, no document skeleton). This script wraps it in a standalone document,
turns off the AI features (there is no AI service outside claude.ai), links the
manifest and icons, and registers the offline service worker.
Remember to raise CACHE in sw.js after every build so installed phones update.
"""
import sys
from pathlib import Path

src = Path(sys.argv[1]).read_text(encoding='utf-8')
src = src.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')

head = '''<!doctype html>
<html lang="ka">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#1e5a8a" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#182230" media="(prefers-color-scheme: dark)">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="description" content="შინაგანი მედიცინის რეზიდენტურის საგამოცდო ტესტები: კითხვა, ტესტი, ჯგუფები, ჩანაწერები, შეცდომები, სტატისტიკა.">
<link rel="manifest" href="manifest.json">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icon-192.png">
<style>
:root { color-scheme: light; padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px) }
body { margin: 0; font: 14px system-ui, sans-serif }
img { max-width: 100% }
[hidden] { display: none !important }
</style>
<script>window.__NO_AI = true;</script>
'''
ts = src.index('<title>')
te = src.index('</title>') + len('</title>')
title, rest = src[ts:te], (src[:ts] + src[te:]).strip()
tail = '''
<script>
if ('serviceWorker' in navigator && (location.protocol === 'https:' || location.hostname === 'localhost')) {
  window.addEventListener('load', () => { navigator.serviceWorker.register('sw.js').catch(() => {}) });
}
</script>
</body>
</html>
'''
out = head + title + '\n</head>\n<body>\n' + rest + '\n' + tail
Path(__file__).with_name('index.html').write_text(out, encoding='utf-8')
print('index.html written,', len(out), 'bytes')
