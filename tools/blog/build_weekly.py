#!/usr/bin/env python3
"""
Builds the "Weekly AI Brief" blog posts from tools/blog/weeks/*.json into posts.json.

  python3 tools/blog/build_weekly.py            # rebuild posts.json (+ share previews for new posts)
  python3 tools/blog/build_weekly.py --check    # validate the weekly files only

One JSON file per week, named by its Monday publish date, e.g. weeks/2026-11-30.json:
  {
   "pub": "2026-11-30", "covers": "23 to 29 November 2026",
   "title": "Short headline of the week (max ~85 characters)",
   "excerpt": "1-2 sentences, max ~220 characters.",
   "items":  [ {"h": "headline", "t": "2-3 sentences, attributed", "s": "Source name", "u": "https://real-url"} ],   # 4 items
   "water":  {"h": "...", "t": "...", "s": "...", "u": "..."},       # industry chatter, clearly attributed (or null)
   "means":  [ {"who": "Small business owners", "t": "one practical sentence or two"} ],       # 3 items
   "prompt": "A copy-paste prompt with [brackets] to fill in.",
   "reads":  [ {"h": "title", "s": "source", "u": "https://real-url"} ]                           # optional, up to 3
  }
Rules (the weekly routine follows them too): every u must be a real URL you actually opened or saw in search
results; attribute every claim ("X reported"); no unverified rumours about named people.
"""
import base64, datetime, html, json, os, re, subprocess, sys, textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
WEEKS = os.path.join(HERE, 'weeks')
POSTS = os.path.join(ROOT, 'posts.json')
CAT = 'Weekly AI Brief'
BASE_ID = 31                       # id of the 8 June 2026 brief
BASE_DATE = datetime.date(2026, 6, 8)


def esc(s): return html.escape(str(s), quote=True)


def post_id(pub):
    d = datetime.date.fromisoformat(pub)
    if d.weekday() != 0: raise SystemExit(f'{pub} is not a Monday')
    n = (d - BASE_DATE).days
    if n < 0 or n % 7: raise SystemExit(f'{pub} is before the first brief')
    return BASE_ID + n // 7


def pretty(pub):
    d = datetime.date.fromisoformat(pub)
    return f'{d.day} {d.strftime("%B %Y")}'


def link(u, s): return f'<a href="{esc(u)}" target="_blank" rel="noopener noreferrer">{esc(s)}</a>'


def validate(w, fn):
    for k in ('pub', 'covers', 'title', 'excerpt', 'items', 'means', 'prompt'):
        if not w.get(k): raise SystemExit(f'{fn}: missing "{k}"')
    if len(w['title']) > 92: raise SystemExit(f'{fn}: title too long ({len(w["title"])})')
    if not (3 <= len(w['items']) <= 6): raise SystemExit(f'{fn}: need 3-6 items')
    for it in w['items'] + ([w['water']] if w.get('water') else []) + w.get('reads', []):
        if not str(it.get('u', '')).startswith('https://'): raise SystemExit(f'{fn}: bad url {it}')
    if w['pub'] != os.path.basename(fn)[:-5]: raise SystemExit(f'{fn}: pub does not match file name')


def body(w):
    h = [f'<p>Your week in AI, <strong>{esc(w["covers"])}</strong>. A five-minute read: what happened, what it means for your work, and one thing to try.</p>',
         '<h3>The headlines</h3>']
    for it in w['items']:
        h.append(f'<p><strong>{esc(it["h"])}</strong><br>{esc(it["t"])} <em>Source: {link(it["u"], it["s"])}</em></p>')
    if w.get('water'):
        x = w['water']
        h += ['<h3>Water-cooler</h3>', f'<p><strong>{esc(x["h"])}</strong><br>{esc(x["t"])} <em>Source: {link(x["u"], x["s"])}</em></p>']
    h.append('<h3>What this means for you</h3><ul>' + ''.join(f'<li><strong>{esc(m["who"])}:</strong> {esc(m["t"])}</li>' for m in w['means']) + '</ul>')
    h += ['<h3>Try this week</h3>', '<p>Copy this prompt into ChatGPT, Claude or Gemini and fill in the [brackets]:</p>',
          f'<blockquote>{esc(w["prompt"])}</blockquote>']
    if w.get('reads'):
        h.append('<h3>Worth reading</h3><ul>' + ''.join(f'<li>{link(r["u"], r["h"])} <em>({esc(r["s"])})</em></li>' for r in w['reads']) + '</ul>')
    h.append('<p><em>Every item links to its original source. Reports are attributed to the outlet that made them, and unconfirmed claims are labelled as reports, not facts.</em></p>')
    h.append('<p>Want to use AI on your real work? <a href="sprint-day1.html">Try Day 1 of the 30-Day AI Sprint free</a>, or <a href="index.html#start">take the 1-minute quiz</a>.</p>')
    return '\n'.join(h)


def thumb(w):
    title = w['title']
    size, width, maxl = (60, 29, 3)
    lines = textwrap.wrap(title, width)
    if len(lines) > maxl: size, width, maxl = (50, 35, 4); lines = textwrap.wrap(title, width)[:maxl]
    y0 = 300 if len(lines) <= 3 else 270
    tx = ''.join(f'<text x="70" y="{y0 + i * (size + 16)}" font-family="Georgia,DejaVu Serif,serif" font-weight="700" font-size="{size}" fill="#F0EDE6">{esc(l)}</text>' for i, l in enumerate(lines))
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 675">'
           '<rect width="1200" height="675" fill="#0E0E10"/><rect width="1200" height="6" fill="#C9A84C"/>'
           '<rect x="10" y="10" width="1180" height="655" fill="none" stroke="#C9A84C" stroke-opacity="0.18"/>'
           '<path d="M70 70v-34h34M1130 639v34h-34" fill="none" stroke="#C9A84C" stroke-width="3"/>'
           '<text x="70" y="120" font-family="Courier New,DejaVu Sans Mono,monospace" font-weight="700" font-size="28" letter-spacing="3" fill="#C9A84C">// WEEKLY AI BRIEF</text>'
           f'<text x="70" y="170" font-family="Arial,DejaVu Sans,sans-serif" font-size="26" fill="#8A877F">{esc(pretty(w["pub"]).upper())}</text>'
           f'{tx}'
           '<text x="70" y="610" font-family="Georgia,DejaVu Serif,serif" font-style="italic" font-weight="700" font-size="34" fill="#C9A84C">AI Made Simple</text>'
           '<text x="1130" y="610" text-anchor="end" font-family="Arial,DejaVu Sans,sans-serif" font-size="22" fill="#6A6860">aimadesimpleschool.com</text></svg>')
    return 'data:image/svg+xml;base64,' + base64.b64encode(svg.encode()).decode()


def main():
    files = sorted(f for f in os.listdir(WEEKS) if f.endswith('.json'))
    weeks = []
    for f in files:
        w = json.load(open(os.path.join(WEEKS, f), encoding='utf-8')); validate(w, f); weeks.append(w)
    if '--check' in sys.argv:
        print(f'{len(weeks)} weekly files OK'); return
    posts = json.load(open(POSTS, encoding='utf-8'))
    ids = {post_id(w['pub']) for w in weeks}
    posts = [p for p in posts if p['id'] not in ids]
    for p in posts: p['feat'] = False
    newest = max(weeks, key=lambda w: w['pub'])['pub']
    for w in weeks:
        b = body(w); words = len(re.sub(r'<[^>]+>', ' ', b).split())
        posts.append({'id': post_id(w['pub']), 'cat': CAT, 'date': pretty(w['pub']), 'rt': f'{max(3, round(words / 200))} min',
                      'feat': w['pub'] == newest, 'thumb': thumb(w), 'title': 'Weekly AI Brief: ' + w['title'],
                      'excerpt': w['excerpt'], 'body': b})
    posts.sort(key=lambda p: -p['id'])
    json.dump(posts, open(POSTS, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'posts.json: {len(posts)} posts ({len(weeks)} weekly briefs, latest {newest})')
    if '--no-previews' not in sys.argv:
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'build-previews.py')], cwd=ROOT, capture_output=True, text=True)
        print((r.stdout or r.stderr).strip().splitlines()[-1] if (r.stdout or r.stderr) else 'previews done')
        # keep the commit small: restore preview files of posts that did not change
        try:
            mod = subprocess.run(['git', 'ls-files', '--modified', 'assets/p'], cwd=ROOT, capture_output=True, text=True).stdout.split()
            keep = {str(i) for i in ids}
            old = [m for m in mod if os.path.splitext(os.path.basename(m))[0] not in keep]
            if old: subprocess.run(['git', 'checkout', '--'] + old, cwd=ROOT, check=False)
        except Exception:
            pass


if __name__ == '__main__':
    main()
