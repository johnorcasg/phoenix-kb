# Phoenix Inbound KB (Static Site)

This folder contains a crawler-friendly microsite for Go High Level's Web Crawler knowledge ingestion.

## Deploy (GitHub Pages)
1. Create a public repo named `phoenix-kb`.
2. Add these files and commit.
3. In Repo Settings → Pages: Deploy from `main` branch → `/root`.
4. Your site will be at `ttps://github.com/johnorcasg/phoenix-kb.git`.

## Deploy (Netlify/Vercel/S3)
- Upload this folder as a static site. Root path should contain `index.html`.

## IMPORTANT
- Find & replace `https://YOUR-DOMAIN/phoenix-kb/` with your actual hostname in:
  - `sitemap.xml`
  - `robots.txt`
  - the `<link rel="canonical">` in each HTML file's `<head>`
- After publishing, verify:
  - `https://github.com/johnorcasg/phoenix-kb.git/index.html`
  - `ttps://github.com/johnorcasg/phoenix-kb.git/sitemap.xml`
  - `ttps://github.com/johnorcasg/phoenix-kb.git/robots.txt`

## Add to GHL Web Crawler
- Start URL: your root (e.g., `ttps://github.com/johnorcasg/phoenix-kb.git`).
- Also add your `sitemap.xml` URL to ensure full coverage.

## Content
- 7 topic pages + index, styled for readability and clean crawling.
- Keep pages public, stable, and text-first.
- Update the "Updated" date in the header when you change content.
