// generate-posts.mjs
// Runs inside GitHub Actions once per day.
// It asks Claude for 5 short blog posts, then appends them to posts.json.
// If anything goes wrong, it exits WITHOUT changing posts.json, so a bad
// run can never break your live blog.

import { readFileSync, writeFileSync } from 'fs';

const KEY = process.env.ANTHROPIC_API_KEY;
if (!KEY) {
  console.error('No ANTHROPIC_API_KEY found. Add it as a repository secret.');
  process.exit(1);
}

// Each category gets a self-contained brand thumbnail (SVG embedded as a data URI),
// so new posts never depend on uploaded files or external image hosts.
const CAT_STYLE = {
  'AI Models':        ['AI MODELS',        '#C9A84C'],
  'Tools & Apps':     ['TOOLS & APPS',     '#6BA3D4'],
  'Business':         ['BUSINESS',         '#5FD48A'],
  'Tutorials':        ['TUTORIALS',        '#D4956B'],
  'Industry':         ['INDUSTRY',         '#C47AD4'],
  'Nigeria & Africa': ['NIGERIA & AFRICA', '#4CC9B4']
};
const VALID_CATS = Object.keys(CAT_STYLE);

function thumbFor(cat){
  const [label, accent] = CAT_STYLE[cat] || CAT_STYLE['Tools & Apps'];
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 675"><rect width="1200" height="675" fill="#0E0E10"/><rect width="1200" height="6" fill="#C9A84C"/><rect x="10" y="10" width="1180" height="655" fill="none" stroke="#C9A84C" stroke-opacity="0.18" stroke-width="1"/><text x="80" y="300" font-family="Georgia,serif" font-style="italic" font-weight="700" font-size="150" fill="#C9A84C">AI</text><rect x="84" y="345" width="180" height="3" fill="${accent}"/><text x="84" y="410" font-family="Arial,sans-serif" font-weight="700" font-size="40" letter-spacing="2" fill="#F0EDE6">${label}</text><text x="84" y="610" font-family="Arial,sans-serif" font-weight="700" font-size="26" letter-spacing="3" fill="#7A7870">AI MADE SIMPLE</text></svg>`;
  return 'data:image/svg+xml;base64,' + Buffer.from(svg).toString('base64');
}

const prompt = `Write 5 short blog posts about recent global AI news and practical AI use,
for an audience of Nigerian professionals, entrepreneurs and creators.

Brand voice: practical, encouraging, clear, no hype, no exclamation-mark overload.
Like a premium but down-to-earth business publication called "AI Made Simple".

Across the 5 posts, include a MIX of:
- at least one AI news / industry update,
- at least one self-help / productivity tip post,
- at least one post that contains a copy-and-paste sample prompt (inside the body),
- topics relevant to using AI for business, tools, and the African / Nigerian context.

Return ONLY valid JSON: an array of exactly 5 objects. Each object must have these
exact fields and nothing else:
  "cat": one of ${VALID_CATS.map(c => '"'+c+'"').join(', ')}
  "rt": estimated read time, e.g. "4 min"
  "title": a clear headline (no surrounding quotes inside the string)
  "excerpt": one sentence summary
  "body": the article as HTML using only <p>, <h3>, <ul>, <li>, <strong> tags

Do NOT include markdown, do NOT wrap the JSON in backticks, and do NOT add any
text before or after the JSON array.`;

let res;
try {
  res = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'content-type': 'application/json',
      'x-api-key': KEY,
      'anthropic-version': '2023-06-01'
    },
    body: JSON.stringify({
      model: 'claude-opus-4-8',
      max_tokens: 4000,
      messages: [{ role: 'user', content: prompt }]
    })
  });
} catch (e) {
  console.error('Network error calling the API:', e.message);
  process.exit(1);
}

if (!res.ok) {
  console.error('API returned status', res.status, await res.text());
  process.exit(1);
}

const data = await res.json();
let text = (data.content || []).map(b => b.text || '').join('').trim();
text = text.replace(/^```(?:json)?\s*/i, '').replace(/\s*```$/i, '').trim();

let newPosts;
try {
  newPosts = JSON.parse(text);
  if (!Array.isArray(newPosts)) throw new Error('Response was not a JSON array');
} catch (e) {
  console.error('Could not parse AI response as JSON. Leaving posts.json unchanged.');
  console.error('Raw response was:\n', text.slice(0, 500));
  process.exit(1);
}

// Load existing posts so we can continue ids and prepend new ones.
let existing = [];
try {
  existing = JSON.parse(readFileSync('posts.json', 'utf8'));
  if (!Array.isArray(existing)) existing = [];
} catch {
  existing = [];
}

let nextId = existing.reduce((max, p) => Math.max(max, p.id || 0), 0) + 1;
const today = new Date().toLocaleString('en-US', { month: 'long', year: 'numeric' });

const prepared = newPosts.slice(0, 5).map(p => {
  const cat = VALID_CATS.includes(p.cat) ? p.cat : 'Tools & Apps';
  return {
    id: nextId++,
    cat,
    date: today,
    rt: typeof p.rt === 'string' ? p.rt : '4 min',
    feat: false,                       // new posts are not featured by default
    thumb: thumbFor(cat),
    title: String(p.title || 'Untitled'),
    excerpt: String(p.excerpt || ''),
    body: String(p.body || '')
  };
}).filter(p => p.title && p.body);     // drop any malformed entries

if (prepared.length === 0) {
  console.error('No valid posts produced. Leaving posts.json unchanged.');
  process.exit(1);
}

// Newest posts first.
const combined = [...prepared, ...existing];
writeFileSync('posts.json', JSON.stringify(combined, null, 2));
console.log(`Added ${prepared.length} new posts. Total is now ${combined.length}.`);
