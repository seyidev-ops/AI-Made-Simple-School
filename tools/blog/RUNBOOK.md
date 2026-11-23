# Weekly AI Brief: Monday runbook

Goal: publish one "Weekly AI Brief" every Monday covering the previous Monday to Sunday.

1. Work out dates. `pub` = today (a Monday, YYYY-MM-DD). `covers` = the 7 days before, e.g. "16 to 22 November 2026".
2. Research with Firecrawl `firecrawl_search`: short company-name queries (OpenAI, Anthropic, Google Gemini, Microsoft Copilot, Meta AI, Nigeria AI) with `tbs=cdr:1,cd_min:M/D/YYYY,cd_max:M/D/YYYY`, `highlights:false`. Use the date in each URL, not relative dates.
3. Verify any big claim with a limit-1 search for the original report. Only use URLs you actually saw. Attribute everything ("X reported"). No unverified rumours about named people. Label opinion as opinion.
4. Write `tools/blog/weeks/<pub>.json` (format in the header of `build_weekly.py`): 4 items, 1 water-cooler item, 3 "what this means for you" lines, 1 copy-paste prompt, optional reads. Title max 92 characters.
5. Run `python3 tools/blog/build_weekly.py --check`, then `python3 tools/blog/build_weekly.py`.
6. Commit `posts.json`, the new week file and the new `assets/p/<id>.*` files. Push the branch and merge to `main` (fast-forward) so GitHub Pages publishes.
7. If the Apps Script digest is installed, subscribers get the email automatically on Monday (see the `sendWeeklyDigest` trigger). Nothing to do here.
8. Report: the title, the sources used, and anything you could not verify.
