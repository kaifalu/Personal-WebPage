# Kaifa Lu — Personal Academic Website

https://kaifalu.github.io/Personal-WebPage/

A polished, responsive, no-build academic website designed for GitHub Pages.

## Public URL

After deployment to the existing `kaifalu/kaifalu_page` repository, the website is available at:

https://kaifalu.github.io/kaifalu_page/

## Files

- `index.html` — complete webpage structure and content
- `assets/css/styles.css` — visual system, responsive layout, dark mode
- `assets/js/main.js` — navigation, dark mode, publication filtering, scroll effects
- `assets/img/` — optimized website images
- `assets/Kaifa-Lu-CV.pdf` — downloadable CV
- `.nojekyll` — prevents GitHub Pages from applying Jekyll processing
- `404.html`, `robots.txt`, `sitemap.xml` — publishing support files
- `preview_server.py` — optional local preview helper

## Publish on GitHub Pages

1. Open the GitHub repository `kaifalu/kaifalu_page`.
2. Back up the existing repository if desired.
3. Upload the **contents of this folder** to the repository root and replace the older website files.
4. Commit the changes to the publishing branch (currently `master` in the original site package; use the branch configured for Pages in your repository).
5. In GitHub: **Settings → Pages → Build and deployment → Deploy from a branch**.
6. Select the publishing branch and `/(root)`, then save.
7. Wait for GitHub Pages to finish deployment and refresh the public URL.

## Local preview

From this folder:

```bash
python preview_server.py
```

Then open `http://localhost:8000`.

Alternatively:

```bash
python -m http.server 8000
```

## Updating content

### Biography or section text
Edit `index.html`.

### Publications
Each publication is an `<article class="publication">` in `index.html`. Set `data-category` to one or more of:

- `ai`
- `resilience`
- `environment`
- `review`

### Research projects
Edit the cards in the `#research` section and replace images in `assets/img/` if needed.

### CV
Replace `assets/Kaifa-Lu-CV.pdf` with a newer PDF while preserving the same filename. All CV buttons will continue working automatically.

### Colors and typography
The main design variables are at the top of `assets/css/styles.css` under `:root`.

## Design notes

The site intentionally uses a lightweight static architecture: no Jekyll, Node, npm, database, or framework is required. The only external presentation dependency is Google Fonts; system-font fallbacks are included.
