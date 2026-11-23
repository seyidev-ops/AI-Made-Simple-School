/**
 * AI Made Simple School: one Google Apps Script for
 *   1. newsletter signups ("Stay ahead of AI") + welcome email
 *   2. one-click unsubscribe
 *   3. the weekly AI brief email (sent from updates@ your domain)
 *   4. first-use access codes: starts a code's 30 days the first time it is used, and stops sharing
 *
 * GENERATED FILE: google-apps-script-ams.js is built from tools/codes/apps-script-template.js by
 * tools/codes/generate.py (it injects the list of valid code hashes). Edit the template, not the output.
 *
 * ── SET-UP (about 10 minutes, once) ───────────────────────────────────────────────
 *  1. Sign in to the Google account that should SEND the emails, open https://script.google.com
 *  2. New project → delete the starter code → paste this WHOLE file → Save (name it "AMS Mailer").
 *  3. Project Settings (gear icon) → Time zone → "(GMT+01:00) Lagos". Save.
 *  4. Run → setupSheets   (approve the permissions the first time: Sheets, Gmail, external requests).
 *  5. Run → installTriggers   (sends the weekly brief automatically every morning a new one exists).
 *  6. Deploy → New deployment → type "Web app" → Execute as: Me → Who has access: Anyone → Deploy.
 *     Copy the Web app URL (it ends with /exec).
 *  7. Put that URL into ams-config.js on the website (apiUrl) and publish the site.
 *  8. Run → testWelcome (type your own email in the function first) to check the email arrives.
 *
 * ── SENDING FROM updates@yourdomain ───────────────────────────────────────────────
 *  Gmail → Settings → Accounts → "Send mail as" → Add another email address → updates@yourdomain.
 *  Gmail emails a confirmation to that address; you must be able to read that mailbox (forward it
 *  to your Gmail or use Google Workspace). Until that is done, emails go out from the Gmail address
 *  that owns this script (the script falls back automatically; nothing breaks).
 *  Also add SPF, DKIM and DMARC records for the domain so mail does not land in spam.
 *
 * ── LIMITS ────────────────────────────────────────────────────────────────────────
 *  Free Gmail: about 100 emails a day through a script. Google Workspace: about 1,500 a day.
 *  Over ~80 subscribers on free Gmail, the digest continues the next morning automatically.
 *  Past a few hundred subscribers, move the list to Brevo or MailerLite (free tiers) instead.
 */

var CFG = {
  SHEET_ID:   '157udafPnTILbRYp9TbgD6FQgPOTuCo5iL4jeDg4Suwg',
  SITE:       'https://aimadesimpleschool.com',
  FROM_EMAIL: 'updates@aimadesimpleschool.com',
  FROM_NAME:  'AI Made Simple School',
  REPLY_TO:   'updates@aimadesimpleschool.com',
  POSTAL:     'Ona Services Limited, Abuja, Nigeria',
  BRIEF_CAT:  'Weekly AI Brief',
  CODE_DAYS:  __DAYS__,
  MAX_DEVICES: 3
};

/** Hashes of every valid first-use access code (injected by generate.py). */
var VALID_HASHES = /*__HASHES__*/[];

/* ───────────────────────── web app entry points ───────────────────────── */

function doGet(e) {
  var p = (e && e.parameter) || {};
  var action = String(p.action || '').toLowerCase();
  try {
    if (action === 'redeem')      return out_(redeem_(p));
    if (action === 'unsubscribe') return out_(unsubscribe_(p));
    if (action === 'ping')        return out_({ status: 'ok' });
    return out_(subscribe_(p));                      // default keeps the old blog form working
  } catch (err) {
    return out_({ status: 'error', message: String(err) });
  }
}

function doPost(e) {
  try {
    var data = JSON.parse((e.postData && e.postData.contents) || '{}');
    return doGet({ parameter: data });
  } catch (err) {
    return out_({ status: 'error', message: String(err) });
  }
}

function out_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}

/* ───────────────────────────── helpers ───────────────────────────── */

function ss_() { return SpreadsheetApp.openById(CFG.SHEET_ID); }
function stamp_() { return Utilities.formatDate(new Date(), 'Africa/Lagos', 'dd/MM/yyyy HH:mm:ss'); }
function esc_(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }

function sheet_(name, header) {
  var ss = ss_(), sh = ss.getSheetByName(name);
  if (!sh) {
    // the very first tab already holds your subscribers from the old script: reuse it
    sh = (name === 'Subscribers' && ss.getSheets().length && ss.getSheets()[0].getLastRow() > 0 && !ss.getSheetByName('Subscribers'))
      ? ss.getSheets()[0].setName('Subscribers') : ss.insertSheet(name);
  }
  if (sh.getLastRow() === 0) {
    sh.appendRow(header);
    sh.getRange(1, 1, 1, header.length).setBackground('#C9A84C').setFontColor('#0E0E10').setFontWeight('bold');
    sh.setFrozenRows(1);
  }
  return sh;
}
function subSheet_() { return sheet_('Subscribers', ['Timestamp (WAT)', 'Email Address', 'Source', 'Status', 'Track', 'Unsubscribed at']); }
function redSheet_() { return sheet_('Redemptions', ['Code No', 'Code hash (first 12)', 'Name', 'Name key', 'Devices', 'First login (ISO)', 'Expires (ISO)', 'Last seen', 'Hash']); }

function setupSheets() { subSheet_(); redSheet_(); SpreadsheetApp.flush(); Logger.log('Sheets ready.'); }

function secret_() {
  var props = PropertiesService.getScriptProperties(), s = props.getProperty('UNSUB_SECRET');
  if (!s) { s = Utilities.getUuid() + Utilities.getUuid(); props.setProperty('UNSUB_SECRET', s); }
  return s;
}
function token_(email) {
  var raw = Utilities.computeHmacSha256Signature(email, secret_());
  return raw.map(function (b) { return ('0' + (b & 0xff).toString(16)).slice(-2); }).join('').slice(0, 32);
}
function unsubUrl_(email) { return CFG.SITE + '/unsubscribe.html?e=' + encodeURIComponent(email) + '&t=' + token_(email); }

function mail_(to, subject, text, html, listUnsub) {
  var opts = { name: CFG.FROM_NAME, replyTo: CFG.REPLY_TO, htmlBody: html };
  if (listUnsub) opts.headers = { 'List-Unsubscribe': '<' + listUnsub + '>' };
  try {
    var withFrom = {}; for (var k in opts) withFrom[k] = opts[k]; withFrom.from = CFG.FROM_EMAIL;
    GmailApp.sendEmail(to, subject, text, withFrom);      // works once updates@ is a verified "Send mail as" alias
  } catch (e) {
    delete opts.headers;                                  // MailApp does not accept custom headers
    MailApp.sendEmail(to, subject, text, opts);           // falls back to the script owner's own address
  }
}

function shell_(inner, email) {
  return '<div style="background:#0E0E10;padding:24px 12px;font-family:Arial,Helvetica,sans-serif">'
    + '<div style="max-width:560px;margin:0 auto;background:#16161A;border:1px solid #2a2a2e;border-radius:14px;padding:26px;color:#F0EDE6">'
    + '<div style="font-size:12px;letter-spacing:.12em;color:#C9A84C;font-weight:700;text-transform:uppercase;margin-bottom:14px">AI Made Simple School</div>'
    + inner
    + '<hr style="border:none;border-top:1px solid #2a2a2e;margin:22px 0 12px">'
    + '<div style="font-size:12px;color:#8A877F;line-height:1.6">You get this because you subscribed on aimadesimpleschool.com. '
    + '<a href="' + unsubUrl_(email) + '" style="color:#C9A84C">Unsubscribe</a> any time.<br>' + esc_(CFG.POSTAL) + '</div>'
    + '</div></div>';
}
function btn_(href, label) {
  return '<a href="' + href + '" style="display:inline-block;background:#C9A84C;color:#141210;text-decoration:none;font-weight:700;padding:12px 20px;border-radius:8px">' + label + '</a>';
}

/* ───────────────────────── 1. newsletter signup ───────────────────────── */

function subscribe_(p) {
  if (p.website) return { status: 'success' };           // honeypot: real people never fill this hidden field
  var email = String(p.email || '').trim().toLowerCase();
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) || email.length > 120) return { status: 'error', message: 'Invalid email' };
  var lock = LockService.getScriptLock(); lock.waitLock(15000);
  var result = 'new';
  try {
    var sh = subSheet_(), data = sh.getDataRange().getValues();
    for (var i = 1; i < data.length; i++) {
      if (String(data[i][1]).toLowerCase() === email) {
        if (data[i][3] === 'Unsubscribed') { sh.getRange(i + 1, 4).setValue('Active'); sh.getRange(i + 1, 6).setValue(''); result = 'back'; break; }
        return { status: 'duplicate', message: 'Already subscribed' };
      }
    }
    if (result === 'new') sh.appendRow([stamp_(), email, String(p.source || 'Blog - Stay Ahead of AI').slice(0, 60), 'Active', String(p.track || '').slice(0, 30), '']);
  } finally { lock.releaseLock(); }
  try { sendWelcome_(email); } catch (e) { Logger.log('welcome failed: ' + e); }
  return { status: 'success', message: result === 'back' ? 'Welcome back' : 'Subscribed' };
}

function latestBrief_() {
  var res = UrlFetchApp.fetch(CFG.SITE + '/posts.json?cb=' + Date.now(), { muteHttpExceptions: true });
  if (res.getResponseCode() !== 200) return null;
  var posts = JSON.parse(res.getContentText()).filter(function (p) { return p.cat === CFG.BRIEF_CAT; });
  posts.sort(function (a, b) { return b.id - a.id; });
  return posts[0] || null;
}

function sendWelcome_(email) {
  var b = null; try { b = latestBrief_(); } catch (e) {}
  var inner = '<h1 style="font-size:24px;line-height:1.25;margin:0 0 10px;color:#fff">You\'re in. Welcome.</h1>'
    + '<p style="font-size:15px;line-height:1.7;color:#B8B5AE;margin:0 0 14px">Every Monday we send one short brief: what happened in AI this week, what it means for your work, and one thing to try.</p>'
    + (b ? '<p style="font-size:15px;line-height:1.7;color:#B8B5AE;margin:0 0 16px">Here is the latest one to start with:</p>' + btn_(CFG.SITE + '/blog.html?post=' + b.id, 'Read this week\'s brief') + '<br><br>' : '')
    + '<p style="font-size:15px;line-height:1.7;color:#B8B5AE;margin:0 0 16px">Want to use AI on your real work? Try Day 1 of the 30-Day AI Sprint free:</p>'
    + btn_(CFG.SITE + '/sprint-day1.html', 'Try Day 1 free');
  mail_(email, 'You\'re in: your weekly AI brief', 'Welcome to the AI Made Simple weekly brief. Read the latest: ' + CFG.SITE + '/blog.html', shell_(inner, email), unsubUrl_(email));
}

/* ───────────────────────────── 2. unsubscribe ───────────────────────────── */

function unsubscribe_(p) {
  var email = String(p.e || p.email || '').trim().toLowerCase();
  if (!email || String(p.t || '') !== token_(email)) return { status: 'error', message: 'Invalid link' };
  var sh = subSheet_(), data = sh.getDataRange().getValues();
  for (var i = 1; i < data.length; i++) {
    if (String(data[i][1]).toLowerCase() === email) {
      sh.getRange(i + 1, 4).setValue('Unsubscribed'); sh.getRange(i + 1, 6).setValue(stamp_());
      return { status: 'ok' };
    }
  }
  return { status: 'ok' };
}

/* ───────────────────────────── 3. weekly brief ───────────────────────────── */

/** Runs every morning (see installTriggers). Sends a new brief once, and resumes next day if the daily email quota ran out. */
function sendWeeklyDigest() {
  var props = PropertiesService.getScriptProperties();
  var b = latestBrief_(); if (!b) return;
  var id = String(b.id);
  if (props.getProperty('LAST_DIGEST_ID') === id) return;                 // already finished
  if (props.getProperty('CUR_DIGEST_ID') !== id) { props.setProperty('CUR_DIGEST_ID', id); props.setProperty('CUR_ROW', '2'); }
  var sh = subSheet_(), data = sh.getDataRange().getValues();
  var row = parseInt(props.getProperty('CUR_ROW') || '2', 10);
  var url = CFG.SITE + '/blog.html?post=' + b.id;
  var plain = b.title + '\n\n' + (b.excerpt || '') + '\n\nRead it: ' + url;
  for (; row <= data.length; row++) {
    var r = data[row - 1], email = String(r[1] || '').toLowerCase();
    if (!email || r[3] !== 'Active') continue;
    if (MailApp.getRemainingDailyQuota() < 2) { props.setProperty('CUR_ROW', String(row)); Logger.log('Quota used up; will resume tomorrow at row ' + row); return; }
    var inner = '<div style="font-size:12px;color:#8A877F;margin-bottom:6px">' + esc_(b.date || '') + ' · ' + esc_(b.rt || '') + ' read</div>'
      + '<h1 style="font-size:24px;line-height:1.25;margin:0 0 12px;color:#fff">' + esc_(b.title) + '</h1>'
      + '<p style="font-size:15px;line-height:1.7;color:#B8B5AE;margin:0 0 18px">' + esc_(b.excerpt || '') + '</p>'
      + btn_(url, 'Read the full brief')
      + '<p style="font-size:14px;line-height:1.7;color:#8A877F;margin:22px 0 0">Want to use AI on real work? <a href="' + CFG.SITE + '/sprint-day1.html" style="color:#C9A84C">Try Day 1 of the 30-Day AI Sprint free</a>.</p>';
    try { mail_(email, b.title, plain, shell_(inner, email), unsubUrl_(email)); } catch (e) { Logger.log('send failed for row ' + row + ': ' + e); }
  }
  props.setProperty('LAST_DIGEST_ID', id); props.deleteProperty('CUR_ROW'); props.deleteProperty('CUR_DIGEST_ID');
  Logger.log('Digest ' + id + ' sent.');
}

function installTriggers() {
  ScriptApp.getProjectTriggers().forEach(function (t) { if (t.getHandlerFunction() === 'sendWeeklyDigest') ScriptApp.deleteTrigger(t); });
  ScriptApp.newTrigger('sendWeeklyDigest').timeBased().everyDays(1).atHour(9).create();   // 9am Lagos (set the project time zone!)
  Logger.log('Daily 9am check installed. A new brief is emailed the first morning it appears on the site.');
}

/* ───────────────────── 4. first-use access codes ───────────────────── */

function nameKey_(n) { return String(n || '').toLowerCase().replace(/[^a-z\s]/g, '').trim().split(/\s+/)[0] || ''; }

/** Starts the code's clock on first use. Same first name + up to MAX_DEVICES devices may keep using it. */
function redeem_(p) {
  var h = String(p.h || '').toLowerCase();
  if (!/^[0-9a-f]{64}$/.test(h)) return { status: 'unknown' };
  var no = VALID_HASHES.indexOf(h) + 1;
  if (no < 1) return { status: 'unknown' };
  var name = String(p.name || '').trim().slice(0, 60), key = nameKey_(name), dev = String(p.dev || '').replace(/[^a-z0-9]/gi, '').slice(0, 24);
  var lock = LockService.getScriptLock(); lock.waitLock(15000);
  try {
    var sh = redSheet_(), data = sh.getDataRange().getValues(), now = new Date();
    for (var i = 1; i < data.length; i++) {
      if (data[i][8] !== h) continue;
      var until = new Date(data[i][6]);
      if (data[i][3] && key && data[i][3] !== key) return { status: 'taken' };
      var devs = String(data[i][4] || '').split(',').filter(Boolean);
      if (dev && devs.indexOf(dev) < 0) { if (devs.length >= CFG.MAX_DEVICES) return { status: 'device_limit' }; devs.push(dev); sh.getRange(i + 1, 5).setValue(devs.join(',')); }
      sh.getRange(i + 1, 8).setValue(stamp_());
      if (now > until) return { status: 'expired', startedAt: new Date(data[i][5]).toISOString(), until: until.toISOString() };
      return { status: 'ok', startedAt: new Date(data[i][5]).toISOString(), until: until.toISOString() };
    }
    var end = new Date(now.getTime() + CFG.CODE_DAYS * 86400000);
    sh.appendRow([no, h.slice(0, 12), name, key, dev, now.toISOString(), end.toISOString(), stamp_(), h]);
    return { status: 'ok', startedAt: now.toISOString(), until: end.toISOString(), first: true };
  } finally { lock.releaseLock(); }
}

/** Refund or mix-up? Free the code so it can start again, e.g. resetRedemption(17). */
function resetRedemption(codeNo) {
  var sh = redSheet_(), data = sh.getDataRange().getValues();
  for (var i = data.length - 1; i >= 1; i--) if (Number(data[i][0]) === Number(codeNo)) sh.deleteRow(i + 1);
}
/** After a refund: end access today, e.g. revokeNow(17). */
function revokeNow(codeNo) {
  var sh = redSheet_(), data = sh.getDataRange().getValues();
  for (var i = 1; i < data.length; i++) if (Number(data[i][0]) === Number(codeNo)) sh.getRange(i + 1, 7).setValue(new Date(Date.now() - 1000).toISOString());
}

/* ───────────────────────────── tests ───────────────────────────── */

function testWelcome() { sendWelcome_('PUT-YOUR-EMAIL-HERE@gmail.com'); }
function testSubscribe() { Logger.log(doGet({ parameter: { email: 'test@example.com', source: 'Test' } }).getContent()); }
