/**
 * AI Made Simple — Blog Subscriber Sheet
 * ═══════════════════════════════════════════════════════════
 * DEPLOYMENT STEPS:
 *
 * 1. Go to https://script.google.com
 * 2. Click "New project"
 * 3. Delete any existing code and paste this entire file
 * 4. Click "Save" (name it e.g. "AMS Blog Subscribers")
 *
 * 5. Click "Deploy" → "New deployment"
 *    - Type: Web app
 *    - Execute as: Me (your Google account)
 *    - Who has access: Anyone
 *    Click "Deploy" → copy the /exec URL
 *
 * 6. In blog.html, find this line:
 *      const ENDPOINT = 'https://script.google.com/macros/s/AKfycbxPLACEHOLDER_REPLACE_ME/exec';
 *    Replace the URL with your actual /exec URL from step 5.
 *
 * 7. Upload the updated blog.html to your GitHub repo.
 * ═══════════════════════════════════════════════════════════
 */

var SHEET_ID = '157udafPnTILbRYp9TbgD6FQgPOTuCo5iL4jeDg4Suwg';

/**
 * Handles GET requests from the blog subscribe form.
 * Writes email + metadata to the Google Sheet.
 */
function doGet(e) {
  try {
    var email  = (e.parameter.email  || '').trim().toLowerCase();
    var source = (e.parameter.source || 'Blog - Stay Ahead of AI');

    // Basic email validation
    if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      return respond({ status: 'error', message: 'Invalid email' });
    }

    var sheet = SpreadsheetApp.openById(SHEET_ID).getActiveSheet();

    // Create header row on first run
    if (sheet.getLastRow() === 0) {
      sheet.appendRow([
        'Timestamp (WAT)',
        'Email Address',
        'Source',
        'Status'
      ]);
      // Style header
      var headerRange = sheet.getRange(1, 1, 1, 4);
      headerRange.setBackground('#C9A84C');
      headerRange.setFontColor('#0E0E10');
      headerRange.setFontWeight('bold');
    }

    // Check for duplicate email
    var existing = sheet.getDataRange().getValues();
    for (var i = 1; i < existing.length; i++) {
      if (existing[i][1] === email) {
        return respond({ status: 'duplicate', message: 'Already subscribed' });
      }
    }

    // Write subscriber row
    var timestamp = Utilities.formatDate(
      new Date(),
      'Africa/Lagos',
      'dd/MM/yyyy HH:mm:ss'
    );
    sheet.appendRow([timestamp, email, source, 'Active']);

    // Auto-resize columns
    sheet.autoResizeColumns(1, 4);

    return respond({ status: 'success', message: 'Subscribed!' });

  } catch (err) {
    return respond({ status: 'error', message: err.toString() });
  }
}

/**
 * Handles POST requests (fallback).
 */
function doPost(e) {
  try {
    var data   = JSON.parse(e.postData.contents || '{}');
    var email  = (data.email  || '').trim().toLowerCase();
    var source = (data.source || 'Blog - Stay Ahead of AI');
    var fakeE  = { parameter: { email: email, source: source } };
    return doGet(fakeE);
  } catch (err) {
    return respond({ status: 'error', message: err.toString() });
  }
}

function respond(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

/**
 * TEST FUNCTION — run this manually in Apps Script editor to verify.
 * Go to Run → testSubscribe
 */
function testSubscribe() {
  var result = doGet({ parameter: { email: 'test@aimadesimpleschool.com', source: 'Test' } });
  Logger.log(result.getContent());
}
