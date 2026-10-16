# რეზიდენტურის ტესტები

შინაგანი მედიცინის რეზიდენტურის საგამოცდო ტესტები (შედგენილი ს. ტატიშვილის მიერ, 3521 კითხვა).
მობილურზე მორგებული სტატიკური ვებ-აპი: კითხვა პასუხებით, ტესტი, შეცდომების სია, სტატისტიკა, ფილტრი წლისა და თემის მიხედვით.

Static, dependency-free web app. Progress is kept in the browser (`localStorage`). Works offline after the first load and can be added to the phone's home screen.

## Files

| File | Purpose |
|---|---|
| `index.html` | the whole app (markup, styles, script) |
| `bank.json` | the question bank: `n` number, `q` text, `opts` options, `ans` index of the correct option, `t` topic, `y` year (0 = none), `k` kind, `p` question pattern |
| `manifest.json`, `sw.js`, `icon.svg` | installable app and offline cache |

## Run locally

Any static server works. For example:

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000>. Opening `index.html` directly from the file system does not work, because the app loads `bank.json` with `fetch`.

## Host on GitHub Pages

1. Create a repository on GitHub and push this folder to its `main` branch.
2. In the repository go to Settings, then Pages.
3. Under Build and deployment choose Source: Deploy from a branch, Branch: `main`, folder `/ (root)`. Save.
4. After a minute the site is live at `https://<user>.github.io/<repo>/`.

When you change `index.html` or `bank.json`, raise the `CACHE` version in `sw.js` so phones that installed the app pick up the update.

## Updating the question bank

`bank.json` was generated from the original Excel file. Each entry needs exactly one correct option; the index in `ans` is zero-based and matches the order in `opts`.
