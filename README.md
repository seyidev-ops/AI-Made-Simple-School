AI MADE SIMPLE — REPO FILE MAP
================================

Upload these to your GitHub repo, keeping this exact structure:

  index.html            (updated: logo path -> /assets/logo.svg)
  blog.html             (updated: logo + share links -> /assets/...)
  dashboard.html        (updated: logo + share links -> /assets/...)
  register.html         (updated: logo path)
  login.html            (updated: logo path)
  admin-login.html      (updated: logo path)
  manifest.json         (updated: icon paths -> /assets/logo.svg)
  sw.js                 (updated: cache path + version bumped to ams-v3)
  posts.json            (your 30 posts)
  build-previews.py     (manual backup: regenerates assets/p/)

  assets/
    logo.svg            (NEW — this file was referenced everywhere but
                         did not exist before; your favicon was broken)
    p/                  (60 files: 30 .jpg thumbnails + 30 .html preview pages)

  .github/
    workflows/
      build-previews.yml  (auto-rebuilds assets/p/ when posts.json changes)

HOW THE TWO REGENERATION METHODS WORK
-------------------------------------
Automatic (no install): edit posts.json, commit & push. The GitHub Action
runs, rebuilds assets/p/, and commits the new previews for you.

Manual backup (on your computer): run `pip install cairosvg pillow` once,
then `python3 build-previews.py` whenever you like.

If your domain ever changes, edit BASE_URL at the top of build-previews.py.
