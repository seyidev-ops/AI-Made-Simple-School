# AI Made Simple School
### Nigeria's Premier AI Learning School — [aimadesimpleschool.com](https://aimadesimpleschool.com)

> Master AI in 30 Minutes a Day. From beginner to AI-proficient in 90 days.  
> Built and coded by **Oluwaseyi Ashiru** · Ona Services Ltd © 2026

---

## Overview

A fully static Progressive Web App (PWA) hosted on **GitHub Pages** at `aimadesimpleschool.com`. No backend, no server — all student access, content gating, and admin management run in the browser via `localStorage`.

**Three programmes:**
- **AI Expert User** — 90-day daily lesson programme (Months 1–3)
- **AI Mastery to Money** — Self-Study / Standard / VIP cohort tracks
- **AI Masterclass** — 9 intensive specialist classes (always visible, access-code gated)

---

## File Structure

```
/
├── index.html          ← Public landing page (Programs · Pricing · Blog · FAQ)
├── login.html          ← Student portal — Access Code login + Demo
├── register.html       ← Standalone registration (redirects to dashboard)
├── dashboard.html      ← Student learning dashboard (PWA app shell)
├── admin-login.html    ← Admin-only portal (restricted)
├── blog.html           ← "Everything AI" blog — 22 articles, 6 categories
├── og-image.html       ← Open Graph image template (screenshot → og-image.png)
├── logo.svg            ← Brand logomark (white bg · gold italic AI · Cormorant Garamond)
├── manifest.json       ← PWA manifest (shortcuts · icons · theme colour #C9A84C)
├── sw.js               ← Service worker — cache-first PWA with offline fallback
└── CNAME               ← aimadesimpleschool.com
```

---

## Access System

Students log in with a **Name + Access Code** — no password needed.

### How It Works
1. Admin generates a monthly code in the Admin Portal → **🔑 Codes** tab
2. Admin shares the code with the student (WhatsApp / email)
3. Student enters their name + code on `login.html`
4. System validates the code (active · not expired) and grants dashboard access
5. Admin revokes or extends codes at any time

### Code Format
```
AMS-SEP26-K3X7
│    │      └── 4-char random (uppercase alphanumeric, no ambiguous chars)
│    └── Month + Year (SEP26)
└── AMS prefix
```

### Code Properties
| Field | Description |
|-------|-------------|
| `code` | Unique token e.g. `AMS-SEP26-K3X7` |
| `programme` | `expert` / `m2m` / `mc` / `all` |
| `access` | Full access object — months/phases/classes unlocked |
| `label` | Human label e.g. "Cohort 8 — Seun Akinlade" |
| `expiresAt` | ISO date string — first day of month after duration |
| `active` | `true` / `false` — admin can revoke instantly |
| `usedBy` | Array of `{name, timestamp}` — tracks who used the code |

### Demo Access
Available without a code — grants Month 1 only across all programmes for preview.

---

## Admin Portal

**URL:** `admin-login.html`  
**Credentials:**
```
Username:  onaservices_admin
Password:  ONA@AMS2026#Secure
```
> ⚠ Change these in the `ADMIN_CREDENTIALS` object inside `admin-login.html`.  
> For production security use Supabase Auth or Firebase Authentication.

### Admin Tabs

| Tab | Function |
|-----|----------|
| **Grant Access** | Legacy: grant specific months/phases/classes to a student email |
| **Students** | View all registered accounts · Delete individual students · Export to Excel |
| **Overview** | Total / paid / pending stats · programme breakdown |
| **🔑 Codes** | Generate monthly access codes · Copy · Revoke · Extend by 1 month |
| **📝 Blog** | 10 draft blog posts · Publish / Edit status · Admin login reference |
| **Credentials** | Admin login details · Clear all access · Delete all accounts |

### Excel Export
Admin → Students tab → **"Export to Excel"** downloads `AMS_Students_YYYY-MM-DD.xlsx` with:
`Full Name · Email · Username · Password (hashed) · Programme · Access Level · Payment Status · Admin Granted · Registered · Access Granted`

---

## Dashboard Features

| Feature | Detail |
|---------|--------|
| **Learning sidebar** | All 90 lessons listed with phase grouping and progress dots |
| **Programme tabs** | AI Expert User · AI Mastery to Money · AI Masterclass · 📰 AI News |
| **AI Masterclass** | All 9 classes visible; content locked — upgrade CTA shown |
| **AI News tab** | 8 curated articles with category filter, article detail, share |
| **Schedule bell 🔔** | Nav bell with upcoming live class list and browser notification opt-in |
| **Stats bar** | Current day · lessons completed · streak · progress % |
| **Week tracker** | M T W T F S S engagement rings |
| **Progress rings** | Phase 1 · 2 · 3 completion circles |
| **Timer** | 30-minute focus session countdown |
| **Notes** | Per-lesson participant notes panel |
| **Mark Complete** | Advances lesson, increments streak |
| **Footer** | Home · Account links |

---

## Blog — Everything AI

**URL:** `blog.html`  
**Posts:** 22 articles across 6 categories

| Category | Count |
|----------|-------|
| AI Models | 3 |
| Tools & Apps | 4 |
| Business | 4 |
| Tutorials | 3 |
| Industry | 3 |
| Nigeria & Africa | 3 |
| (+ more drafts in admin) | 10 drafts |

### Blog Features
- Category filter pills (All / AI Models / Tools & Apps / Business / Tutorials / Industry / Nigeria & Africa)
- Featured article (full-width gold card)
- Article grid (auto-fill, responsive)
- **Social sharing** per article: WhatsApp · X/Twitter · LinkedIn · Facebook · Copy Link · Native Share (mobile)
- **Deep-link URLs** — `blog.html?post=13` auto-opens that article
- Google Sheets subscriber integration (set up via `google-apps-script-subscribers.js`)

---

## PWA — Progressive Web App

**Installable** on Android (Chrome) and iOS (Safari) from every public page.

### Install Prompt
A branded banner slides up from the bottom after 2.5 seconds:
- **Android/Chrome:** "Install App" button triggers native install
- **iOS/Safari:** Banner shows "Tap Share ⎋ then Add to Home Screen" guide
- Banner dismisses permanently once installed or explicitly dismissed

### Manifest Shortcuts
From the installed app icon long-press:
1. Student Dashboard
2. AI Blog
3. Sign In

### Service Worker (`sw.js`)
- Cache-first strategy for HTML, JS, CSS, images
- Offline fallback to cached index.html
- Auto-updates cache on activate (purges old versions)

---

## Open Graph / Social Sharing

All OG and Twitter Card meta tags are set on `index.html`:

```html
og:title       → "AI Made Simple — Master AI in 30 Minutes a Day"
og:description → "Nigeria's Premier AI Learning School. Go from beginner to AI-proficient in 90 days..."
og:image       → https://aimadesimpleschool.com/og-image.png  (1200×630)
og:url         → https://aimadesimpleschool.com
twitter:card   → summary_large_image
```

### Creating `og-image.png`
1. Open `og-image.html` in Chrome at exactly 1200×630 viewport
2. Take a full-page screenshot
3. Save as `og-image.png` in the repo root
4. After uploading, re-scrape at [developers.facebook.com/tools/debug](https://developers.facebook.com/tools/debug)

---

## Google Sheets — Blog Subscribers

`blog.html` → "Stay Ahead of AI" subscribe form sends emails to Google Sheets.

**Setup (one-time):**
1. Go to [script.google.com](https://script.google.com) → New project
2. Paste contents of `google-apps-script-subscribers.js`
3. Deploy → New deployment → Web app → Anyone → Deploy
4. Copy the `/exec` URL
5. In `blog.html`, find `AKfycbxPLACEHOLDER_REPLACE_ME` and replace with your URL
6. Set `configured: true` in `login.html` and `register.html` for welcome emails

**Target Sheet:** [Stay Ahead of AI (Subscribers)](https://docs.google.com/spreadsheets/d/157udafPnTILbRYp9TbgD6FQgPOTuCo5iL4jeDg4Suwg/edit)

---

## EmailJS — Welcome Emails

On registration, a welcome email is sent with the student's name, access code, and programme details.

**Configure in `login.html` and `register.html`:**
```javascript
const EJS = {
  serviceId:  'YOUR_SERVICE_ID',
  templateId: 'YOUR_TEMPLATE_ID',
  publicKey:  'YOUR_PUBLIC_KEY',
  from:       'admin@aimadesimpleschool.com',
  cc:         'seyi@aimadesimpleschool.com',
  configured: false   ← set to true after setup
};
```

**Template variables:** `{{to_name}}` · `{{username}}` · `{{password}}` · `{{programme}}` · `{{login_url}}`

---

## Design System

| Token | Value |
|-------|-------|
| Primary gold | `#C9A84C` |
| Gold dim (tint) | `rgba(201,168,76,0.14)` |
| Dark background | `#0E0E10` |
| Dark card | `#16161A` |
| Light background | `#F8F6F1` |
| Heading font | Cormorant Garamond (italic gold for accent) |
| Body font | DM Sans |
| Mono font | Space Mono |
| Brand logo | White square · gold `AI` italic · Cormorant Garamond |

---

## Deployment

All files deploy directly to the GitHub Pages repo root. No build step.

```bash
git add .
git commit -m "Update: [description]"
git push origin main
```

GitHub Pages serves from `main` branch root → live at `aimadesimpleschool.com` via CNAME.

**After each deploy:** Clear browser cache or force-refresh (`Cmd+Shift+R`) to bypass the service worker cache.

---

## localStorage Keys

| Key | Contents |
|-----|----------|
| `ams-session` | Current student session: `{name, code, access, paid, adminSession, validUntil}` |
| `ams-codes` | Array of access code objects (generated by admin) |
| `ams-users` | Legacy email/password accounts (if any remain) |
| `ams-st` | Dashboard state: current day, completed days, streak |
| `ams-theme` | User theme preference: `dark` / `light` / `system` |
| `ams-notifs` | `'1'` if browser notifications enabled |
| `ams-blog-drafts` | Admin-modified draft blog post statuses |
| `pwa-dismissed` | `'1'` if user dismissed the install banner |
| `ams-admin-auth` | `'1'` if admin is authenticated in this session |

---

## Upcoming / Known Items

- [ ] Replace `localStorage` with Supabase for real multi-device persistence
- [ ] Set up SMTP / Zoho for `admin@aimadesimpleschool.com` and configure EmailJS
- [ ] Create and upload `og-image.png` (use `og-image.html` as template)
- [ ] Configure Google Apps Script for blog subscriber sheet
- [ ] Add WhatsApp link to "Contact us" in `login.html` (replace placeholder number)
- [ ] Add actual video/audio content to lesson cards

---

*Built with 🖤 by Oluwaseyi Ashiru for AI Made Simple School — Ona Services Ltd*
