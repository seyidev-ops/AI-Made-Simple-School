#!/usr/bin/env python3
"""
build-previews.py — regenerate all social-media link-preview files.

WHAT IT DOES
  Reads posts.json and, for every post, creates two files in the ./p/ folder:
    p/<id>.jpg   — a 1200x630 thumbnail (what WhatsApp/Telegram show)
    p/<id>.html  — a tiny page with that post's preview tags that redirects
                   a human reader to the full article.

HOW TO USE
  1. Edit posts.json (add or change posts) as usual.
  2. From the same folder as posts.json, run:
         python3 build-previews.py
  3. Upload the updated posts.json AND the whole p/ folder to your site.

  If your domain ever changes, edit the BASE_URL line just below.

REQUIREMENTS
  Python 3, plus two libraries:  pip install cairosvg pillow
  (On Windows, if cairosvg complains about missing 'cairo', install the
   GTK runtime, or ask for the no-cairo version of this script.)
"""

import json
import os
import sys
import base64
import html

# ──────────────────────────────────────────────────────────────────────────
# EDIT THIS if your live domain ever changes. No trailing slash.
BASE_URL = "https://aimadesimpleschool.com"
# ──────────────────────────────────────────────────────────────────────────

HERE = os.path.dirname(os.path.abspath(__file__))
POSTS_PATH = os.path.join(HERE, "posts.json")
OUT_DIR = os.path.join(HERE, "p")

# A plain fallback thumbnail (used only if a post somehow has no usable thumb).
FALLBACK_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 675">'
    '<rect width="1200" height="675" fill="#0E0E10"/>'
    '<rect width="1200" height="6" fill="#C9A84C"/>'
    '<text x="600" y="360" text-anchor="middle" font-family="Georgia,serif" '
    'font-style="italic" font-weight="700" font-size="140" fill="#C9A84C">AI</text>'
    '<text x="600" y="470" text-anchor="middle" font-family="Arial,sans-serif" '
    'font-weight="700" font-size="34" letter-spacing="4" fill="#7A7870">AI MADE SIMPLE</text>'
    '</svg>'
)


def need_libraries():
    """Import the imaging libraries, or explain clearly how to install them."""
    try:
        import cairosvg  # noqa: F401
        from PIL import Image  # noqa: F401
        return True
    except ImportError:
        print("\nMissing a required library.")
        print("Please run this once, then run this script again:\n")
        print("    pip install cairosvg pillow\n")
        print("(On Windows, if it mentions 'cairo', install the GTK3 runtime,")
        print(" or ask for the no-cairo version of this script.)")
        return False


def svg_from_thumb(thumb):
    """Extract raw SVG text from a data:image/svg+xml;base64,... string."""
    if isinstance(thumb, str) and thumb.startswith("data:image/svg+xml;base64,"):
        b64 = thumb.split(",", 1)[1]
        try:
            return base64.b64decode(b64).decode("utf-8")
        except Exception:
            return None
    return None


def esc(s):
    return html.escape(str(s), quote=True)


def make_html(post):
    pid = post["id"]
    title = esc(post.get("title", "AI Made Simple"))
    desc = esc(post.get("excerpt", ""))
    img = f"{BASE_URL}/p/{pid}.jpg"
    article_url = f"{BASE_URL}/blog.html#post-{pid}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — AI Made Simple</title>
<meta name="description" content="{desc}">

<!-- Open Graph (WhatsApp, Telegram, Facebook, LinkedIn) -->
<meta property="og:type" content="article">
<meta property="og:site_name" content="AI Made Simple">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:url" content="{BASE_URL}/p/{pid}.html">

<!-- Twitter / X -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{img}">

<!-- Send humans to the real article; crawlers read the tags above and ignore this -->
<meta http-equiv="refresh" content="0; url={article_url}">
<link rel="canonical" href="{article_url}">
<script>location.replace({json.dumps(article_url)});</script>
</head>
<body style="background:#0E0E10;color:#F0EDE6;font-family:Arial,sans-serif;text-align:center;padding:3rem;">
<p>Loading article… If you are not redirected,
<a href="{article_url}" style="color:#C9A84C;">tap here to read it</a>.</p>
</body>
</html>"""


def main():
    if not need_libraries():
        sys.exit(1)
    import cairosvg
    from PIL import Image
    import io

    if not os.path.exists(POSTS_PATH):
        print(f"Could not find posts.json next to this script ({POSTS_PATH}).")
        print("Run the script from the same folder as posts.json.")
        sys.exit(1)

    with open(POSTS_PATH, "r", encoding="utf-8") as f:
        try:
            posts = json.load(f)
        except json.JSONDecodeError as e:
            print("posts.json is not valid JSON. Fix it and try again.")
            print("Details:", e)
            sys.exit(1)

    if not isinstance(posts, list) or not posts:
        print("posts.json should be a non-empty list of posts.")
        sys.exit(1)

    os.makedirs(OUT_DIR, exist_ok=True)

    valid_ids = set()
    made_jpg = 0
    made_html = 0

    for post in posts:
        pid = post.get("id")
        if pid is None:
            print("Skipping a post with no 'id'.")
            continue
        valid_ids.add(str(pid))

        # 1) JPG thumbnail
        svg = svg_from_thumb(post.get("thumb")) or FALLBACK_SVG
        try:
            png_bytes = cairosvg.svg2png(
                bytestring=svg.encode("utf-8"),
                output_width=1200,
                output_height=630,
            )
            Image.open(io.BytesIO(png_bytes)).convert("RGB").save(
                os.path.join(OUT_DIR, f"{pid}.jpg"), "JPEG", quality=85, optimize=True
            )
            made_jpg += 1
        except Exception as e:
            print(f"  Warning: could not build image for post {pid}: {e}")

        # 2) HTML preview page
        try:
            with open(os.path.join(OUT_DIR, f"{pid}.html"), "w", encoding="utf-8") as out:
                out.write(make_html(post))
            made_html += 1
        except Exception as e:
            print(f"  Warning: could not write page for post {pid}: {e}")

    # 3) Clean up files for posts that no longer exist (deleted posts)
    removed = 0
    for name in os.listdir(OUT_DIR):
        base, ext = os.path.splitext(name)
        if ext.lower() in (".jpg", ".html") and base not in valid_ids:
            try:
                os.remove(os.path.join(OUT_DIR, name))
                removed += 1
            except OSError:
                pass

    print(f"\nDone. Built {made_jpg} images and {made_html} preview pages in p/")
    if removed:
        print(f"Removed {removed} leftover files for deleted posts.")
    print(f"Base URL is set to: {BASE_URL}")
    print("Next: upload posts.json and the whole p/ folder to your site.")


if __name__ == "__main__":
    main()
