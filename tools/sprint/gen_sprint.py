# 30-Day Professional AI Sprint (₦10,000) — curriculum data.
# Model: 5-15-10 → concept (5 min) · guided practice (15 min) · real work (10 min).
# Days 8-12 are fully track-specific. On every other day the prompt and real-work task are
# tailored to the learner's track by filling {tokens} from TRACKS below.

# ---------------------------------------------------------------- sources
OA = 'OpenAI · OpenAI Academy'
SPRINT_SRC = {
 'oa_found':   {'t': 'AI Foundations (free course: prompting, context, reviewing output)', 'u': 'https://academy.openai.com/public/courses/ai-foundations-dnq5w', 'by': OA},
 'oa_applied': {'t': 'Applied AI Foundations (turn a recurring task into a workflow)', 'u': 'https://academy.openai.com/public/courses/applied-ai-foundations-szsmv', 'by': OA},
 'oa_agents':  {'t': 'Agents and Workflows (assigning work to AI agents)', 'u': 'https://academy.openai.com/public/courses/agents-and-workflows-y0qoc', 'by': OA},
 'oa_students':{'t': 'AI for College Students (study, group work, applications)', 'u': 'https://academy.openai.com/public/courses/ai-for-college-students-gxgmr', 'by': OA},
 'oa_edu':     {'t': 'AI for Educators (lesson plans, activities, assessments)', 'u': 'https://academy.openai.com/public/courses/ai-for-educators-lc8j1', 'by': OA},
 'oa_smb':     {'t': 'OpenAI Academy Small Business club (free sessions and replays)', 'u': 'https://academy.openai.com/public/clubs/small-business-ipf4m', 'by': OA},
 'oa_lib':     {'t': 'OpenAI Academy content library (videos and guides)', 'u': 'https://academy.openai.com/public/content', 'by': OA},
}
# Anthropic sources (fluency, limits, clear, examples, xml, longdoc, chain, halluc, projects,
# artifacts, personal, skills, agents, cowork, teams, character, claude101, econ) come from
# tools/lessons/gen_src.py and are merged at build time.

# ---------------------------------------------------------------- tracks
TRACKS = {
 'ops': {'name': 'Corporate & Operations', 'icon': '🏢', 'who': 'HR, admin, finance, operations, civil service and executive assistants',
   'role': 'HR/admin officer at a logistics company in Lagos', 'work': 'the monthly operations report', 'people': 'my line manager and department heads',
   'doc': 'the staff handbook', 'data': 'a staff leave and attendance sheet', 'meeting': 'the weekly management meeting',
   'msg': 'a memo announcing new resumption times', 'win': 'reports, memos and minutes done in half the time'},
 'pm': {'name': 'Project & Event Management', 'icon': '📋', 'who': 'project managers, event planners, coordinators and programme officers',
   'role': 'project and event coordinator planning a 300-guest corporate launch in Abuja', 'work': 'the weekly project status update', 'people': 'the client, vendors and my team',
   'doc': 'the client brief and vendor contracts', 'data': 'a task and budget tracker', 'meeting': 'the weekly vendor/stakeholder check-in',
   'msg': 'a vendor briefing for the event day', 'win': 'plans, timelines and status updates that run themselves'},
 'sales': {'name': 'Sales & Customer Service', 'icon': '🤝', 'who': 'sales reps, business developers, account managers and customer service teams',
   'role': 'sales executive selling business software to SMEs', 'work': 'follow-ups and proposals for my pipeline', 'people': 'prospects and existing customers',
   'doc': 'our product brochure and price list', 'data': 'my leads and sales pipeline sheet', 'meeting': 'discovery calls with prospects',
   'msg': 'a follow-up to a prospect who went quiet', 'win': 'more replies, faster proposals and happier customers'},
 'creative': {'name': 'Freelancers & Creatives', 'icon': '🎨', 'who': 'marketers, designers, writers, content creators, social media managers and virtual assistants',
   'role': 'freelance social media manager with 3 retainer clients', 'work': 'a week of client content', 'people': 'my clients and their audiences',
   'doc': 'a client brand guide', 'data': 'a client content performance sheet', 'meeting': 'client feedback calls',
   'msg': 'a reply to a client asking for "one more revision"', 'win': 'client work delivered faster, with room for more clients'},
 'biz': {'name': 'Small Business Owners', 'icon': '🏪', 'who': 'shop owners, online sellers, service businesses and SMEs',
   'role': 'owner of a small fashion and accessories business that sells on Instagram and WhatsApp', 'work': 'this week\'s promos and customer replies', 'people': 'my customers',
   'doc': 'my price list and delivery policy', 'data': 'a sales and stock sheet', 'meeting': 'supplier and staff check-ins',
   'msg': 'a WhatsApp broadcast for a weekend promo', 'win': 'more sales and fewer hours on admin'},
 'student': {'name': 'Students, Researchers & Educators', 'icon': '🎓', 'who': 'undergraduates, postgraduates, researchers, teachers and lecturers',
   'role': 'final-year student writing a project on renewable energy adoption in Nigeria', 'work': 'my project chapter / lesson notes', 'people': 'my supervisor (or my students)',
   'doc': 'a 40-page journal article', 'data': 'my survey results sheet', 'meeting': 'lectures and supervisor meetings',
   'msg': 'an email to my supervisor asking for feedback', 'win': 'faster reading, clearer writing and better grades, with integrity'},
}

# ---------------------------------------------------------------- core days (shared, tokenised)
DAYS = {}
def day(d, w, t, tool, concept, steps, prompt, apply, watch, src):
    DAYS[d] = {'d': d, 'w': w, 't': t, 'tool': tool, 'concept': concept, 'steps': steps,
               'prompt': prompt, 'apply': apply, 'watch': watch, 'src': src}

# ===== WEEK 1 · Foundations =====
day(1, 1, 'Set Up Your AI Power-Stack', 'ChatGPT · Claude · Gemini (free)',
 "You don't need 30 tools. You need one main AI assistant you know well, plus one backup. ChatGPT, Claude and Gemini are all general assistants: they write, summarise, analyse files and images, search the web and talk by voice. Their free plans are enough for this sprint. Today you set up two of them on your phone and laptop, switch on the safety settings, and get your first real win on actual work. Both OpenAI and Anthropic teach the same starting habit: give clear instructions with real context, then review what comes back.",
 ['Install the ChatGPT and Claude apps (or Gemini) on your phone and sign in on your laptop too. Use the same Google account so your chats sync.',
  'Open Settings → Data controls / Privacy. Decide whether your chats may be used to improve the models. For work content, switching that off is the safer default.',
  'Try voice: tap the microphone and describe a task out loud, the way you would to a colleague. Voice is the fastest way to give rich context.',
  'Paste today\'s prompt into BOTH assistants and compare. Which answer is more useful for your work? Make that your main assistant for the sprint.'],
 """I work as a {role}.
Here is one task on my desk this week: [describe a real task, e.g. {work}].

1. Ask me 3 short questions you need answered to do this well.
2. After I answer, give me a first draft or a step-by-step plan.
3. Tell me which parts of the task you should NOT do for me, and why.""",
 "Finish the task from the prompt for real and use the output at work today. Note how long it took compared with doing it alone.",
 "Never paste passwords, BVN, account numbers, customers' phone numbers or confidential company files into an AI tool. If your employer has rules about AI, follow them.",
 ['oa_found', 'claude101', 'fluency'])

day(2, 1, 'The Perfect Prompt: Context, Task, Constraints, Output', 'Your main assistant',
 "Most bad AI answers come from thin prompts. Anthropic's advice is to imagine the AI as a brilliant new employee on day one: clever, but it knows nothing about your company, your audience or your standards. OpenAI's AI Foundations course teaches the same thing as \"give clear instructions and add useful context\". A reliable structure is CTCO. Context is who you are, the situation and why it matters. Task is exactly what you want. Constraints are length, tone, what to avoid and deadlines. Output is the format: table, email, bullet list, slide outline. Explaining WHY a rule matters helps the AI follow it in cases you didn't spell out.",
 ['Write a weak prompt for a real task (one line, no context). Run it and save the answer.',
  'Rewrite the same request with CTCO using today\'s template. Run it.',
  'Compare the two answers side by side. Circle what improved and which part of the prompt caused it.',
  'Save the strong prompt in a note called "My Prompt Library". You will add to it every day of this sprint.'],
 """CONTEXT: I'm a {role}. [Who it's for, the situation, and why it matters.]
TASK: Write {msg}.
CONSTRAINTS: Under 150 words. Tone: professional but warm. Avoid jargon because [reason]. Nigerian context, British English.
OUTPUT: Give 2 versions, then a one-line note on when to use each.""",
 "Use CTCO on the first real message or document you need to write today. Send it after your own edit.",
 "If the AI keeps getting something wrong, the fix is usually more context or a clearer constraint, not a different tool.",
 ['clear', 'oa_found', 'best'])

day(3, 1, 'Make the AI Know You: Instructions, Memory & Projects', 'ChatGPT Projects · Claude Projects · Custom instructions',
 "Re-explaining your job in every chat wastes time. All the major assistants now let you save standing context. Custom instructions or preferences say who you are and how you like answers. Memory lets the assistant remember useful facts across chats, and you can view and delete what it remembers. Projects are workspaces where you upload key files and write instructions once, so every chat inside already knows your work. Set this up once and every answer for the rest of the sprint gets better.",
 ['Open Settings → Personalisation (ChatGPT) or Settings → Profile/Preferences (Claude). Paste the instructions from today\'s prompt after the AI helps you write them.',
  'Create a Project called "My work". Add 2–3 non-confidential files that describe your work: a template, a past report, a price list or a course outline.',
  'Write project instructions: your role, audience, tone, and what the AI should always check or never do.',
  'Test it: in the project, ask for something you do every week. Notice you didn\'t have to explain yourself.'],
 """Help me write my AI custom instructions (under 150 words).
About me: {role}. I mostly work on {work} for {people}.
How I like answers: [short / detailed], British English, Naira for money, Nigerian examples.
Always: ask a clarifying question if my request is vague; flag anything you are unsure about.
Never: invent figures, names, laws or quotes.
Then suggest what files and instructions I should put in a "My work" project.""",
 "Inside your new Project, do one real piece of work: draft part of {work}.",
 "Check what your assistant has saved to memory every few weeks, and delete anything sensitive or out of date.",
 ['projects', 'personal', 'oa_found'])

day(4, 1, 'Professional-Looking Outputs: Format, Export, Share', 'Canvas / Artifacts · Google Docs · Word',
 "AI output often looks AI-made: long dashes, generic headings, \"In today's fast-paced world\". Professionals ask for the exact format they need and then make it their own. Tell the AI the shape: a one-page memo with headings, a table with these columns, a 6-slide outline, a WhatsApp-length message. Use the editing workspaces (ChatGPT Canvas, Claude Artifacts) to refine documents section by section. Then export to Word, Google Docs or PDF and add your final human touch: names, numbers, letterhead.",
 ['Ask for today\'s output in a specific structure (see prompt). Open it in Canvas (ChatGPT) or as an Artifact (Claude) if offered.',
  'Edit one section with a targeted request, e.g. "make section 2 more concise" or "turn this list into a table".',
  'Ask the AI to remove AI tell-tales: clichés, long dashes, filler phrases and repeated triples.',
  'Copy into Google Docs or Word, apply your organisation\'s template, and export as PDF.'],
 """Turn these rough notes into a one-page document for {people}:
<notes>[paste your messy notes about {work}]</notes>

Format: title, 2-line summary at the top, 3-4 headed sections, a table where it helps, and "Next steps" with owners and dates.
Style: plain British English, short paragraphs, no clichés, no long dashes, no hype.""",
 "Produce one real document you will actually send this week, formatted and exported.",
 "Read the final version once as the recipient would, out loud if possible. Your name goes on it, not the AI's.",
 ['artifacts', 'examples'])

day(5, 1, 'Research & Fact-Checking (Avoiding Hallucinations)', 'Web search · Deep research · Perplexity',
 "AI models write the most likely next words. Usually that is right, but sometimes it is confidently wrong. This is called hallucination, and it shows up most with numbers, names, quotes, laws, prices and anything recent or local. The fix is a habit, not a tool. Use web search or deep research mode when facts matter. Ask for citations. Open the sources yourself. Ask the AI to separate what is well-supported from what is uncertain. Anthropic calls this skill Discernment. OpenAI's course calls it reviewing outputs. Either way, you stay the editor.",
 ['Turn on web search (or Deep research) in your assistant, or use Perplexity.',
  'Run today\'s prompt on a real question from your work.',
  'Open at least 3 of the cited sources. Does each one really say what the summary claims? How recent is it?',
  'Ask: "What are the strongest arguments against this conclusion, and what should I verify with an expert?"'],
 """Search the web and answer this for my work as a {role}:
[your question]

Rules:
- Prefer official and established sources from the last 12 months.
- Cite every factual claim.
- Split your answer into "Well supported" and "Uncertain or disputed".
- End with "What I should verify myself before using this".""",
 "Use a verified finding from today in a real decision, message or document, and keep the source links with it.",
 "A neat citation is not proof. Fake or mismatched sources still happen, so open the link.",
 ['halluc', 'limits', 'oa_found'])

day(6, 1, 'Week 1 Project: One Real Deliverable, End to End', 'Everything from Days 1–5',
 "Today you combine the week. Pick one deliverable you genuinely need: {work}. Research what you need (Day 5). Brief the AI with CTCO inside your Project (Days 2–3). Get a formatted draft (Day 4). Check it and finish it yourself. This is the core loop you'll use for the rest of your career: delegate the draft, describe it clearly, check it carefully and own the result.",
 ['Choose the deliverable and write down how long it normally takes you.',
  'Work through: research → brief → draft → edit → format, using your saved prompts.',
  'Time yourself. Stop at 30 minutes and see how far you got.',
  'Write 3 lines: what AI did well, where it needed correcting, what you\'d do differently next time.'],
 """I need to produce {work} for {people}.
Act as my senior colleague. First, ask me for the key facts and figures you need (max 6 questions).
Then draft it in the format we use: [describe or paste a past example].
After the draft, list anything you assumed that I must confirm.""",
 "Submit or send the deliverable for real. This is your first before/after sample for your portfolio.",
 "Keep the AI's list of assumptions. That list is exactly what you must check before sending.",
 ['chain', 'fluency'])

day(7, 1, 'Review Day: Get Feedback & Start Your Prompt Library', 'Your assistant + a colleague',
 "Learning sticks when you reflect and share. Today, get two kinds of feedback on your Week 1 work. First, ask the AI to critique it from the reader's point of view, which is one of the most valuable uses of AI there is. Second, show a colleague, classmate or friend and ask one honest question. Then tidy your prompt library: name each prompt by the task it does, so you can find it in 10 seconds.",
 ['Paste your Week 1 deliverable and run today\'s critique prompt.',
  'Fix the top 2 issues it raises (only if you agree with them).',
  'Share the work with one person and ask: "What\'s one thing that would make this better?"',
  'Organise your prompt library into: Writing · Research · Planning · Data · Communication.'],
 """Act as {people} reading this for the first time:
<draft>[paste your Week 1 deliverable]</draft>
Be honest, not polite:
1. What is clear and useful?
2. What is confusing, missing or unconvincing?
3. The 3 changes that would most improve it.""",
 "Post one tip you learnt this week in your team chat, class group or WhatsApp status. Teaching others makes you the \"AI person\" at work.",
 "If the AI only praises your work, ask it directly for the three weakest points.",
 ['character', 'examples'])

# ===== WEEK 2 · Track days 8-12 come from TRACK_DAYS; 13-14 shared =====
day(13, 2, 'Build Your Track Toolkit', 'Projects + your prompt library',
 "This week you learnt the core workflows for your field. Today you package them so they are instantly reusable: a Project (or custom GPT, Claude Project or Gemini Gem) with your instructions and templates, plus your 5 best prompts with blanks to fill. OpenAI's Applied AI Foundations course describes this move as going from one-off prompts to repeatable workflows. Each time you reuse a tested workflow, you save the thinking as well as the typing.",
 ['List the 5 tasks from this week that you will repeat most often.',
  'For each, save the final, improved prompt with [blanks] in your library.',
  'Add your templates (past examples you liked) to your Project as files.',
  'Update the Project instructions so it knows these are your standard workflows.'],
 """Here are 5 prompts I used this week as a {role}:
[paste them]
Turn each into a reusable template:
- a clear name
- when to use it
- the prompt with [blanks] for the parts that change
- a one-line quality check I should do on the output""",
 "Use one template from your toolkit on a fresh, real task today and time it.",
 "Templates go stale. When a template gives a weak result, fix the template, not just that one chat.",
 ['oa_applied', 'skills', 'projects'])

day(14, 2, 'Show Your Work: Before & After', 'Your assistant + Canva or Docs',
 "Results you can show are worth more than skills you can describe. Today you create 2 before/after samples from your real work: the old way and the AI-assisted way, with time taken and quality differences. These samples go into your Sprint portfolio (Day 29) and are powerful in appraisals, client pitches and job applications. Remove confidential details first.",
 ['Pick 2 tasks you did with AI this week. Anonymise names, figures and client details.',
  'For each, note: task, time before, time with AI, what improved.',
  'Ask the AI to help you write a short case note for each (see prompt).',
  'Save both in a folder called "AI Sprint Portfolio".'],
 """Help me write a short before/after case note for my portfolio as a {role}.
Task: [what]. Before: [how I used to do it, time taken]. With AI: [how I did it, time taken, tools].
Result: [what improved]. Write 5 lines, factual and modest, no hype. Remove anything confidential.""",
 "Share one before/after with your manager, client, supervisor or a friend this week.",
 "Never put real client names, figures or confidential documents in a portfolio without permission.",
 ['fluency'])

# ===== WEEK 3 · Multimodal tools & automation =====
day(15, 3, 'Vision: Photos, Screenshots & Scanned Documents', 'ChatGPT / Claude / Gemini camera + upload',
 "Modern assistants can see. Snap a whiteboard, a handwritten note, a receipt, a printed table, a chart or a screenshot of an error, and the AI can read it, extract the data, explain it or turn it into a document or spreadsheet. This removes hours of retyping. Accuracy is high on clear images, lower on blurry photos, messy handwriting and small text. So check numbers carefully, especially in anything financial.",
 ['Take a clear photo of something you would normally retype: a printed table, handwritten notes, receipts or a whiteboard.',
  'Upload it and run today\'s prompt.',
  'Compare 5 extracted values against the original by eye.',
  'Paste the result into Google Sheets or Docs.'],
 """I've uploaded a photo of [what it is] from my work as a {role}.
1. Extract all the text/data exactly as shown. Use a table if it is tabular.
2. Mark anything you couldn't read clearly with [?] instead of guessing.
3. Then [summarise it / turn it into action points / calculate totals].""",
 "Digitise one real paper document or screenshot you would otherwise have typed out by hand.",
 "Don't photograph other people's IDs, bank details or confidential papers into AI tools.",
 ['limits'])

day(16, 3, 'Voice Notes, Calls & Meetings to Action', 'Voice mode · Transcription · Meeting notes',
 "Nigerians run on voice notes and calls. AI can now turn speech into text and then into decisions, minutes, task lists and follow-up messages. Use voice mode to brainstorm while driving, record a meeting (with permission) using a transcription tool or your assistant's record feature, or transcribe a long WhatsApp voice note. The skill is asking for the right output: not just \"summarise\", but who agreed to do what, by when.",
 ['Record or pick a real recording: {meeting}, a voice note or a 5-minute monologue about a task.',
  'Transcribe it (assistant record mode, Otter, or upload the audio file).',
  'Run today\'s prompt on the transcript.',
  'Send the action list to the people involved after you check it.'],
 """Here is a transcript of {meeting}:
<transcript>[paste]</transcript>
Give me:
1. A 5-line summary
2. Decisions made
3. Action items as a table: task | owner | deadline ("not stated" if missing)
4. A short follow-up message I can send on WhatsApp/email to everyone.""",
 "Use today's workflow on a real meeting or call and send the follow-up within an hour.",
 "Always tell people you are recording, and check names and figures in the transcript. Accents and Pidgin can be misheard.",
 ['xml'])

day(17, 3, 'Spreadsheets & Data Analysis Without Formulas', 'Upload a sheet to ChatGPT / Claude / Gemini',
 "Upload a spreadsheet and ask questions in plain English: totals by month, top 10 customers, overdue tasks, budget variance, survey results. The assistants run real calculations behind the scenes rather than guessing, and they can draw charts and write the formulas for you. Your job is to ask a clear question, check one result by hand and decide what the numbers mean.",
 ['Take {data} (or a copy with sensitive columns removed).',
  'Upload it and ask for a data check first: blanks, duplicates, odd values.',
  'Ask your real question and request one chart.',
  'Ask for the exact Excel/Google Sheets formula so you can rebuild it yourself, and check one number by hand.'],
 """I've uploaded {data}. Columns: [list them].
1. Check the data for problems and tell me how you'd fix them.
2. Answer: [your question, e.g. what changed this month and why it matters].
3. Create one clear chart with a title that states the finding.
4. Give me the Excel/Sheets formulas you used, with one-line explanations.""",
 "Produce one real insight from your own data and share it in a short message or report.",
 "Remove names, phone numbers and salary/financial details unless your organisation has approved the tool for that data.",
 ['oa_applied', 'limits'])

day(18, 3, 'Long Documents: 100 Pages in 10 Minutes', 'File upload · NotebookLM · Projects',
 "Contracts, policies, tender documents, research papers and manuals take hours to read. AI can read them in seconds, but you need a method that keeps it accurate. Anthropic's guidance is to put the document first, ask the AI to quote the exact passages it relies on, then answer. NotebookLM does this by design, with every answer citing the source. Quotes let you check quickly and catch made-up details.",
 ['Upload {doc} (or another long document) to your assistant or NotebookLM.',
  'Run today\'s prompt.',
  'Click or search 3 of the quotes to confirm they are real and in context.',
  'Ask one follow-up question you actually need answered for work.'],
 """Read the attached document fully: {doc}.
1. Summarise it in 8 bullet points for a busy {role}.
2. For each point, quote the exact sentence that supports it.
3. List deadlines, obligations, numbers and risks in a table.
4. If something I'd expect isn't in the document, say "not in the document" instead of guessing.""",
 "Use the summary and risk table in a real decision, meeting or assignment this week.",
 "For legal, financial or contractual decisions, AI summaries help you prepare. They don't replace reading key clauses or getting professional advice.",
 ['longdoc', 'halluc'])

day(19, 3, 'Build Your Own AI Assistant', 'Custom GPTs · Claude Projects · Gemini Gems',
 "A custom assistant is an AI with permanent instructions, knowledge files and a specific job, such as \"proposal writer for my company\", \"vendor email assistant\" or \"study buddy for my course\". You build it by describing it in plain English, no coding. It is the same idea as Day 3's Project, made more specific so that you, or your team, can open it and get consistent results every time.",
 ['Choose ONE repetitive job from your toolkit that would benefit from a dedicated assistant.',
  'Create a custom GPT (ChatGPT → GPTs → Create), a Claude Project, or a Gemini Gem.',
  'Paste the instructions from today\'s prompt and upload 1–3 example files.',
  'Test it with 3 real requests and tweak the instructions after each one.'],
 """Write the instructions for a custom AI assistant I'll build as a {role}.
Its job: [e.g. draft {msg} and similar messages].
Include: its role, who it serves ({people}), the steps it follows, tone, formats it uses, what it must ask before starting, what it must never do, and how it should handle missing information.
Keep it under 300 words.""",
 "Use your assistant for one real task today. If it works well, share it with one colleague or classmate.",
 "Don't upload confidential files to an assistant you share with others. Anyone using it may be able to see that knowledge.",
 ['projects', 'skills', 'oa_applied'])

day(20, 3, 'AI Agents: Assign a Multi-Step Task', 'ChatGPT agent · Claude Cowork · Deep research',
 "A chat answers a question. An agent does a task: it plans steps, searches, opens pages and files, fills in a spreadsheet or drafts a document, then reports back. OpenAI's Agents and Workflows course and Anthropic's material on agents give the same advice. Give the agent a clear job, the context, what \"done\" looks like and firm boundaries, then review its work as you would a new hire's. Start with low-risk tasks like research and compiling information, never payments or sending messages on your behalf.",
 ['Pick a low-risk research or compiling task (see prompt for ideas for your track).',
  'Brief the agent using today\'s template and start it.',
  'Watch what it does. Stop it if it heads somewhere you didn\'t intend.',
  'Check the output: spot-check 3 facts and note where it needed correcting.'],
 """Task for an AI agent (I'm a {role}):
GOAL: [e.g. compile a list of 10 options for X with prices and contacts from public websites].
CONTEXT: [why I need it, for {people}].
DONE LOOKS LIKE: a table with columns [..], with the source link for every row.
BOUNDARIES: public information only. Do NOT buy, sign up, send messages or share my data. Ask me before any action that can't be undone.
When finished: summarise what you did and anything you're unsure about.""",
 "Use the agent's (checked) output in real work this week.",
 "Agents can make many mistakes quickly. Review before you rely on anything, and never give them access to money or your outbox.",
 ['oa_agents', 'agents', 'cowork'])

day(21, 3, 'Applied Workspace Challenge', 'Everything from Week 3',
 "Combine this week's tools on one real job. Examples: photo of handwritten notes → structured plan; meeting recording → minutes and tracker; long document → risk table and email summary; spreadsheet → insight → slide. The goal is a mini-workflow you can repeat, not a one-off trick.",
 ['Choose a job that uses at least 2 of: vision, voice, data, long documents, custom assistant, agent.',
  'Write the steps down before you start (input → AI step → your check → output).',
  'Run it on real work within 30 minutes.',
  'Save the steps as a mini-workflow in your prompt library.'],
 """Help me design a mini-workflow for this recurring job as a {role}: [describe].
Inputs I start with: [photo / recording / sheet / document].
Give me numbered steps showing: the AI tool for each step, the prompt to use, where I must check the output, and the final deliverable.""",
 "Run the workflow on real work and record the time saved.",
 "Every workflow needs a human check before anything leaves your hands.",
 ['oa_applied', 'chain'])

# ===== WEEK 4 · Professional integration =====
day(22, 4, 'Find Your 5 Biggest AI Wins', 'Your assistant + a time audit',
 "Anthropic's Economic Index research shows people get the most from AI on specific, repeatable tasks: writing, editing, analysis and research help. Not \"using AI\" in general. Today you audit your own week to find the 5 tasks where AI will save you the most time or raise your quality the most. These become your SOPs over the next two days.",
 ['List every task you did last week, with rough minutes for each.',
  'Paste the list into today\'s prompt.',
  'Agree or disagree with each AI suggestion. You know your job best.',
  'Pick your top 5 and rank them.'],
 """Here's my task list from last week as a {role}, with minutes per task:
[paste]
For each task, rate: AI can draft it / AI can assist / keep it human (and why).
Estimate minutes saved per week for the top candidates and recommend my 5 biggest AI wins.""",
 "Put your top 5 at the top of your Project instructions so your assistant knows your priorities.",
 "Keep relationship-heavy and judgement-heavy work (negotiations, hard conversations, final decisions) human-led.",
 ['econ', 'fluency'])

day(23, 4, 'Write SOP #1: A Repeatable AI Workflow', 'Docs + your assistant',
 "An SOP (standard operating procedure) is written steps anyone can follow to get the same quality result. An AI-assisted SOP says which steps AI does, with which prompt, and where a human checks. This is what makes your AI skill reliable, and what makes you valuable to employers and clients: you don't just use AI, you build dependable processes with it.",
 ['Take win #1 from Day 22.',
  'Run today\'s prompt to draft the SOP.',
  'Walk through it on a real task and fix any step that was unclear.',
  'Save it as a one-page document with your name and date.'],
 """Write an SOP for this task: [win #1] (I'm a {role}).
Format: Purpose · When to use it · Inputs needed · Numbered steps (mark AI steps with the exact prompt) · Human check points · Final quality checklist · Time it should take.
Write it so a new colleague could follow it without asking me questions.""",
 "Use the SOP on today's real version of the task and correct it where reality differed.",
 "An SOP is only useful if it is used. Keep it short and put it where you'll see it.",
 ['oa_applied', 'skills'])

day(24, 4, 'SOP #2 & Your Reusable Templates', 'Docs + your assistant',
 "Repeat yesterday for your second biggest win, then turn your best outputs into templates: a proposal skeleton, a report format, a message bank, a checklist. Templates plus SOPs plus your prompt library make a personal operating system. Anthropic calls packaged, reusable ways of working \"skills\". Whatever you call it, it is how individuals get 2–3× more done without working longer.",
 ['Draft SOP #2 with yesterday\'s prompt.',
  'Pick your 3 best AI-assisted outputs from the sprint and turn each into a template with [blanks].',
  'Store SOPs and templates together in one folder and link them in your Project.'],
 """Turn this good piece of work into a reusable template for future use as a {role}:
<example>[paste a finished document/message you're proud of]</example>
Keep the structure and tone; replace specific details with [clearly named blanks]; add a 3-line "how to use this template" note at the top.""",
 "Use one of your new templates on a real task before the day ends.",
 "Remove confidential details from templates before sharing them with anyone else.",
 ['skills', 'examples'])

day(25, 4, 'Automate the Hand-offs', 'Email/WhatsApp templates · Calendar · Zapier/Make (optional)',
 "Some of the biggest time drains are the small hand-offs: sending the same reminder, copying form answers into a sheet, chasing updates. You don't need complex systems. Start with saved replies (WhatsApp Business quick replies, Gmail templates), scheduled messages and recurring calendar reminders. If you're ready, one no-code automation (form → sheet → email) in Zapier or Make. Keep a human approval step for anything that goes to customers or managers.",
 ['List 3 repetitive hand-offs in your week.',
  'Set up saved replies or email templates for the most common one (use AI to write them).',
  'Set a recurring reminder or scheduled message for another.',
  'Optional: build one simple Zapier/Make automation for the third.'],
 """These are repetitive messages I send as a {role}:
[paste 3-5 examples]
Write a template for each (with [blanks]), suitable as a WhatsApp quick reply or email template. Keep each under 60 words, friendly and clear.
Then suggest one simple automation that would remove a hand-off completely, with the steps.""",
 "Save the templates in your phone/email today and use one on a real message.",
 "Don't fully automate messages to customers or your boss until you've reviewed many of the drafts and trust them.",
 ['oa_applied', 'agents'])

day(26, 4, 'Privacy, Data Protection & Company Rules', 'Reflection + your assistant',
 "Using AI at work responsibly protects you, your employer and the people whose data you handle. Nigeria's Data Protection Act (NDPA) sets rules for personal data. Many employers now have AI policies, approved tools and banned data types. The practical rules: know which tools are approved, remove personal and confidential details before pasting, use business or enterprise plans for sensitive work where your employer provides them, and never share customers' or colleagues' data without a lawful reason.",
 ['Find out: does your workplace or school have an AI policy or approved tools? Ask HR, IT or your supervisor if unsure.',
  'Review your data settings in each AI tool you use.',
  'Run today\'s prompt to draft your personal data rules.',
  'Remove any sensitive content from past chats, Projects or memory.'],
 """Help me write my personal "AI and data" rules as a {role}.
Cover: tools I may use for work, data I never paste (with examples from my job), how I anonymise documents before using AI, what I do if I make a mistake, and who I ask when unsure.
Make it one page, practical, and in line with Nigeria's data protection principles. Note that I must check my employer's own policy.""",
 "Apply your rules today: anonymise one real document before using AI on it.",
 "This isn't legal advice. For anything formal, check your organisation's policy or a qualified professional.",
 ['fluency', 'oa_found'])

day(27, 4, 'Honesty, Quality & When Not to Use AI', 'Reflection',
 "Trust is your most valuable asset. Responsible AI use means: being open about AI assistance when it matters (to clients, supervisors, examiners, employers), checking facts and figures, watching for bias and unfair outputs, and recognising tasks where AI shouldn't lead: sensitive conversations, performance decisions, legal or medical judgements, anything you can't verify. Anthropic's AI Fluency framework calls this Diligence. OpenAI's courses call it responsible use. Both make the same point: you are accountable for the work.",
 ['Review 3 things you produced with AI this sprint. Was AI use appropriate? Was it checked?',
  'Decide where you will disclose AI use in your work (and how you\'ll phrase it).',
  'Run today\'s prompt to stress-test one of your outputs for bias or unfairness.'],
 """Review this output I created with AI help as a {role}:
<output>[paste]</output>
Check for: factual claims I should verify, assumptions about people (gender, age, ethnicity, religion, location), unfair or exclusionary language, and anything that would embarrass me if the reader knew AI helped.
Suggest fixes, then a one-line disclosure I could use if appropriate.""",
 "Add a \"when I won't use AI\" section to your Day 26 rules.",
 "For students: follow your institution's rules on AI exactly. Submitting AI-written work as your own can be treated as misconduct.",
 ['character', 'fluency', 'oa_found'])

day(28, 4, 'Measure Time Saved & Show Your Value', 'Sheets + Gamma / Canva / Docs',
 "Your manager, clients or supervisor care about results. Today you turn your sprint into evidence: hours saved per week, quality improvements, examples. A one-page \"AI wins\" summary, or 5 slides, can support a promotion, a raise, a client renewal or a job application. Be modest and specific: real numbers beat big claims.",
 ['Collect your notes: tasks, time before vs after, examples (from Days 6, 14, 21-25).',
  'Calculate weekly hours saved and multiply by 4 for a month.',
  'Run today\'s prompt to build the one-pager or slide outline.',
  'Remove anything confidential.'],
 """Help me write a one-page "AI at work" impact summary for {people}.
My data: [tasks, time before/after, examples, quality improvements].
Structure: headline result (hours saved per month), 3 examples with before/after, what I set up (SOPs, templates, assistants), safeguards I use, and what I'd like to do next.
Factual and modest, no hype.""",
 "Share your summary with one person who matters to your career or business.",
 "Don't overclaim. If a number is an estimate, say so.",
 ['oa_applied'])

day(29, 4, 'Graduation: Practical Assessment & Portfolio', 'Your portfolio folder',
 "Graduation is practical, not a memory test. Complete one fresh real task in 30 minutes using your toolkit, and submit a short portfolio: 3 before/after samples, 1 SOP and your AI rules. Send it on WhatsApp to receive your AI Made Simple Sprint certificate. Then run the self-check below. It shows which skills to keep practising.",
 ['Do one brand-new real task end to end with your toolkit (timer on: 30 minutes).',
  'Assemble your portfolio: 3 before/after samples, 1 SOP, your AI rules, your impact summary.',
  'Answer the self-check prompt honestly.',
  'Send your portfolio (PDF or link) on WhatsApp to request your certificate.'],
 """Quiz me on what I learnt in a 30-day AI-at-work sprint as a {role}. Ask 8 practical scenario questions, one at a time, covering: writing good prompts, checking facts, protecting data, using files/images/voice, building assistants, agents, and when not to use AI.
After each answer, tell me if it's strong, OK or risky, and why. At the end, give me my top 2 skills to keep practising.""",
 "Submit your portfolio for your certificate today.",
 "Portfolios must be your real work with confidential details removed.",
 ['fluency', 'limits'])

day(30, 4, 'Your Next Step: Career, Clients & Growth', 'Your assistant + LinkedIn / CV',
 "You can now use AI to do your work faster and better, and you can prove it. Many organisations now list AI skills in job adverts, especially for remote-friendly roles such as virtual assistants, project coordinators, customer success, sales development, operations, content and research. Today you add AI skills to your CV or LinkedIn with real evidence, and plan your next 90 days. If you want to go further, AI Expert User (₦25,000/month) builds deep skills across 30+ tools, and AI Mastery to Money (₦50,000/month) teaches you to earn from AI services.",
 ['Update your CV/LinkedIn with an "AI skills" line backed by one result from your sprint.',
  'Use today\'s prompt to draft 3 CV bullet points and a LinkedIn post about your sprint.',
  'Write your next-90-days plan: 3 skills to deepen, 1 project, 1 weekly habit.',
  'Choose your next step: keep practising, or join AI Expert User or Mastery to Money.'],
 """I just finished a 30-day AI-at-work sprint as a {role}. My results: [time saved, SOPs, assistants built, examples].
1. Write 3 CV bullet points that show AI skills with evidence (no hype).
2. Write a short LinkedIn post about what I learnt, ending with one useful tip for others in my field.
3. Suggest 5 remote-friendly roles or opportunities in my field where these skills help, and what to learn next for each.""",
 "Post your LinkedIn update or send your updated CV to one opportunity this week.",
 "Only claim skills you can demonstrate. Your portfolio is your proof.",
 ['oa_students', 'teams', 'fluency'])

# ---------------------------------------------------------------- track-specific days 8-12
TRACK_DAYS = {}
def tday(track, d, t, tool, concept, steps, prompt, apply, watch, src):
    TRACK_DAYS.setdefault(track, {})[d] = {'d': d, 'w': 2, 't': t, 'tool': tool, 'concept': concept, 'steps': steps,
                                           'prompt': prompt, 'apply': apply, 'watch': watch, 'src': src}

# ===== Corporate & Operations =====
tday('ops', 8, 'Emails & Memos That Get Read and Acted On', 'Your assistant',
 "Most office communication fails because it is too long, unclear about the ask, or wrong in tone. AI is excellent at drafting, shortening and adjusting tone, especially for difficult messages: declining a request, chasing a late submission, announcing an unpopular change. The method: give the context and the relationship, state the one action you need, and ask for versions in different tones.",
 ['Pick a real message you need to send (ideally a tricky one).', 'Run the prompt and pick the best version.', 'Ask: "What might the reader misunderstand or resent in this?" and fix it.', 'Send it after your own edit.'],
 """Context: I'm an HR/admin/ops professional. I need to write to [who] about [situation]. Our relationship: [formal / friendly / senior to me].
The ONE action I need from them: [action, deadline].
Write 3 versions: very formal, warm-professional, and short (WhatsApp length). Lead with the ask, under 120 words each.
Then tell me what the reader might misread in each.""",
 "Clear your 3 most overdue emails or memos using this method.",
 "Check names, dates and policy references yourself. AI may assume details you didn't give.", ['clear', 'examples'])
tday('ops', 9, 'Meeting Minutes & Action Trackers', 'Voice/record mode · Sheets',
 "Minutes are only useful if they turn into action. With AI you can go from recording or rough notes to clean minutes, an action tracker and reminder messages in minutes. Agree a standard format once (decisions, actions, owners, deadlines, open issues) and your minutes become consistent and fast.",
 ['Use notes or a transcript from a recent meeting.', 'Run the prompt to produce minutes and a tracker.', 'Paste the tracker into Google Sheets with a "status" column.', 'Send minutes to attendees after checking.'],
 """From these meeting notes/transcript:
<notes>[paste]</notes>
Produce: (1) formal minutes with attendees, agenda items, decisions; (2) an action tracker table: # | action | owner | due date | status; (3) a 3-line WhatsApp reminder for owners with actions due this week.
Write "not stated" where owners or dates are missing.""",
 "Use the format for your next real meeting and share the tracker.", "Get consent before recording meetings.", ['xml'])
tday('ops', 10, 'Reports From Raw Notes & Data', 'File upload · Sheets · Docs',
 "Monthly and weekly reports eat days. AI can combine your notes, figures and last month's report into a structured draft: summary, key numbers, trends, issues, recommendations. Upload last month's report as a style example, so the new one matches your organisation's format.",
 ['Gather inputs: last report (as example), this period\'s numbers, key events.', 'Run the prompt.', 'Check every number against your source.', 'Add your own judgement in the recommendations.'],
 """Write this month's operations report in the same format and tone as last month's:
<last_report>[paste or attach]</last_report>
<this_month_data>[figures, events, issues]</this_month_data>
Include: executive summary (5 lines), key metrics table vs last month, 3 trends, issues with proposed fixes, recommendations. Flag any figure that looks inconsistent.""",
 "Draft your real next report with this method.", "Numbers must match your source data. Check each one.", ['examples', 'oa_applied'])
tday('ops', 11, 'Slides & Briefings for Management', 'Gamma · Copilot/Claude/ChatGPT · Canva',
 "Executives want the point first. AI slide tools turn an outline into a designed deck in minutes, but the thinking still comes from you: what decision do you want, and what evidence supports it? Use AI to structure the story (situation → problem → options → recommendation), then generate slides.",
 ['Define the audience and the decision you want.', 'Run the prompt for an outline.', 'Paste the outline into Gamma or Canva (or ask your assistant to create slides).', 'Fix visuals and check every number.'],
 """I'm briefing [management audience] for [minutes]. The decision I need: [decision].
Create a 7-slide outline: each slide title is a full sentence stating the point; 2-3 bullets; suggested chart or visual. Structure: situation → problem → options with pros/cons → recommendation → next steps.""",
 "Build a real briefing deck for an upcoming meeting.", "Slides are where made-up statistics slip in. Check every one.", ['artifacts'])
tday('ops', 12, 'HR & Admin Documents in Minutes', 'Your assistant + Projects',
 "Job descriptions, interview questions, onboarding checklists, policy drafts, leave letters, appraisal templates: these follow patterns AI knows well. Your job is to supply your organisation's specifics, keep language fair and inclusive, and make sure policies follow Nigerian labour law and your company rules.",
 ['Pick one HR/admin document you need.', 'Run the prompt with your organisation\'s details.', 'Check for fairness and legal compliance.', 'Save it as a template in your Project.'],
 """Draft a [job description / onboarding checklist / policy / interview guide] for [role or purpose] at a [type, size] organisation in Nigeria.
Include: [key requirements]. Use fair, inclusive language (no age, gender or tribe preferences).
Add a list of points I should confirm with management or against Nigerian labour law before using it.""",
 "Produce one real HR/admin document you need this month.", "AI is not a lawyer. Have policies reviewed before adoption.", ['character'])

# ===== Project & Event Management =====
tday('pm', 8, 'From Messy Brief to Clear Scope', 'Your assistant',
 "Projects and events fail at the start, when the brief is vague. AI is excellent at turning a client's rambling WhatsApp messages or call notes into a structured scope: objectives, deliverables, budget, timeline, stakeholders, assumptions and, most valuable of all, the questions you still need to ask.",
 ['Collect the brief: messages, call notes, emails.', 'Run the prompt.', 'Send the clarifying questions to the client.', 'Save the scope as the project\'s first document.'],
 """Here's the raw brief for a project/event:
<brief>[paste messages/notes]</brief>
Create a one-page scope: objectives, deliverables, success measures, budget (if given), key dates, stakeholders, assumptions, out-of-scope items.
Then list the 8 most important questions I must ask the client before planning, ranked by risk.""",
 "Turn a real brief (current or recent) into a scope document and send your clarifying questions.", "Confirm assumptions in writing with the client. Don't plan on AI guesses.", ['clear'])
tday('pm', 9, 'Work Breakdown, Timeline & Task List', 'Your assistant · Sheets · Trello/Asana/ClickUp',
 "A good plan breaks big outcomes into small tasks with owners and dates. AI can create a work breakdown structure, sequence tasks, flag dependencies and work backwards from a deadline. You add reality: lead times in your city, vendor availability, public holidays, traffic, your team's capacity.",
 ['Use yesterday\'s scope.', 'Run the prompt for a task list with dates.', 'Paste into Sheets, Trello, Asana or ClickUp.', 'Adjust dates for real-world constraints.'],
 """Using this scope: [paste]. Final deadline/event date: [date].
Create a work breakdown: phases → tasks, with owner role, duration, dependency and start/end dates worked back from the deadline.
Output as a table I can paste into Google Sheets. Then highlight the critical path and the 3 tasks most likely to slip.""",
 "Build the real plan for a current project or event.", "Check dates against Nigerian public holidays and vendor lead times. AI often misses local realities.", ['oa_applied', 'chain'])
tday('pm', 10, 'Risk Register & Contingency Plans', 'Your assistant',
 "Professional planners think about what could go wrong before it does: power failure, rain at an outdoor event, a vendor no-show, a late payment, a speaker cancelling, traffic, security. AI is a tireless brainstorming partner for risks and backup plans. You decide what is realistic and what the budget allows.",
 ['Run the prompt for your project/event.', 'Score each risk for likelihood and impact (1–5).', 'Pick owners and triggers for the top 5.', 'Add contingency costs to your budget.'],
 """For this project/event: [short description, venue, date, size, budget].
Brainstorm 15 risks across: people, vendors, venue/logistics, weather, power, security, money, technology, health.
Give a risk register table: risk | likelihood 1-5 | impact 1-5 | early warning sign | prevention | contingency plan | owner.
Highlight the top 5.""",
 "Create the risk register for a real project and share the top 5 with your team.", "Don't let the list paralyse you. Focus on the top risks.", ['oa_applied'])
tday('pm', 11, 'Run-of-Show, Vendor Briefs & Budget Tracker', 'Your assistant · Sheets',
 "For events, the run-of-show (minute-by-minute programme) and vendor briefs make the day run smoothly. For projects, the equivalent is the delivery checklist and supplier specs. AI drafts these fast from your plan, and can build a budget tracker with formulas for estimate vs actual.",
 ['Run the prompt for a run-of-show or delivery checklist.', 'Generate one vendor/supplier brief.', 'Ask for a budget tracker template with formulas.', 'Check timings and costs with real quotes.'],
 """For my event/project: [details: date, venue, programme items, vendors].
1. A run-of-show table: time | item | duration | responsible | notes/cues.
2. A one-page brief for [vendor type]: deliverables, timings, access, contacts, payment terms.
3. A budget tracker layout for Google Sheets: item | estimate | quote | actual | variance (with formulas) | paid?""",
 "Produce the real run-of-show or delivery checklist for your next event/project.", "Confirm every timing with the people responsible.", ['examples'])
tday('pm', 12, 'Status Updates & Stakeholder Communication', 'Your assistant',
 "Stakeholders want short, honest updates: what's done, what's next, what's at risk, what you need from them. A RAG (Red-Amber-Green) status format makes that instant. AI turns your task tracker into a clear weekly update and drafts the hard messages: delays, budget overruns, scope changes. It also writes the post-event report.",
 ['Export or paste your current tracker.', 'Run the prompt for this week\'s update.', 'Edit for tone and accuracy.', 'Send it, and save the format for every week.'],
 """From this tracker/notes: [paste]
Write a weekly status update for {people}: overall RAG status with one-line reason, done this week, next week, risks/issues with mitigation, decisions needed from them (with deadline).
Under 200 words. Then draft a separate, calm message explaining [any delay or problem] with options.""",
 "Send a real status update this week using the format.", "Never hide bad news in an update. AI can help you say it clearly and calmly.", ['clear'])

# ===== Sales & Customer Service =====
tday('sales', 8, 'Know Your Buyer: Prospect Research', 'Web search · Deep research',
 "Selling starts with understanding. AI with web search can research a company, its recent news, likely priorities and decision-makers' public profiles in minutes, so your outreach is relevant instead of generic. Use it to prepare, never to pretend you know someone.",
 ['Pick 3 real prospects.', 'Run the research prompt for each.', 'Verify key facts on their website or LinkedIn.', 'Write one specific reason each prospect might need you.'],
 """Research [company name, city] using public sources.
Give me: what they do, size, recent news (last 12 months, with links), likely priorities or problems, and who probably makes buying decisions for [our product/service].
Then suggest 3 specific ways [our offer] could help them, and one good opening question for a first conversation.""",
 "Prepare research notes for 3 real prospects in your pipeline.", "Use only public information and respect privacy. No scraping personal data.", ['oa_agents', 'halluc'])
tday('sales', 9, 'Outreach That Gets Replies', 'Your assistant · WhatsApp · LinkedIn · Email',
 "Generic AI messages are everywhere, and buyers ignore them. The winning formula is AI-assisted personalisation: one specific detail about them, one useful idea, one easy question. AI drafts the sequence (first message plus 2 follow-ups that each add something new). You make it sound like you.",
 ['Use yesterday\'s research.', 'Run the prompt for one prospect.', 'Rewrite the first line in your own words.', 'Send to 3 real prospects (spaced out).'],
 """Prospect: [name, company, research notes]. My offer: [product/service]. Channel: [WhatsApp / LinkedIn / email].
Write a 3-touch sequence (day 1, day 4, day 9). Each under 70 words: opens with something specific about THEM, offers one useful idea, ends with an easy question. Never "just checking in".""",
 "Send personalised outreach to 3–5 real prospects today.", "Only message people with a legitimate business reason, and stop after 3 unanswered touches.", ['examples'])
tday('sales', 10, 'Discovery Calls & Objection Handling', 'Voice mode role-play',
 "AI is a free sparring partner. Ask it to play a realistic, slightly difficult buyer, with budget worries, an incumbent supplier and a busy schedule, and practise your discovery questions and objection handling by voice. Then ask for honest feedback. Ten minutes of practice beats walking into a call cold.",
 ['Open voice mode in your assistant.', 'Paste the role-play prompt and run a 10-minute practice call.', 'Type "END" and read the feedback.', 'Write your 3 best answers to common objections.'],
 """Role-play a [buyer role] at a [type of company] in Nigeria considering [our product]. You're interested but worried about price, switching from your current supplier, and whether it will work for you. Be realistic, not easy.
I'll run a discovery call. When I say "END", step out of character and give feedback: good questions I asked, what I missed, and better ways to handle each objection.""",
 "Practise before your next real sales call, then compare.", "Role-play builds confidence, but listen to the real customer. They won't follow a script.", ['oa_found'])
tday('sales', 11, 'Proposals & Quotes That Close', 'Your assistant · Docs/Canva',
 "A proposal should reflect the client's problem in their own words, show the value clearly and make saying yes easy. AI turns your call notes into a structured proposal fast, and can critique it as the client's sceptical finance manager, which is one of the best uses of AI in sales.",
 ['Take notes from a real or recent discovery call.', 'Run the prompt.', 'Run the critique and fix weaknesses.', 'Format with your company template and send.'],
 """From my call notes: <notes>[paste]</notes>
Write a 1-2 page proposal: their situation and goals (in their words), our recommended solution, what's included, timeline, investment in ₦ with options, why us, next step with a date.
Then act as their sceptical finance manager: list 5 objections and how the proposal should answer them.""",
 "Produce one real proposal or quote this week with this method.", "Don't promise what your company can't deliver. Check prices, timelines and terms.", ['chain'])
tday('sales', 12, 'Customer Service Replies, Complaints & CRM Notes', 'Your assistant · WhatsApp Business',
 "Fast, empathetic, accurate replies keep customers. AI drafts replies to complaints that acknowledge, apologise where right, explain and fix, without sounding robotic. It also turns messy call notes into clean CRM entries and builds a reply bank for common questions. Keep your company's policies in your Project so replies stay accurate.",
 ['Collect 5 common customer questions and 1 complaint.', 'Run the prompt.', 'Save the replies as WhatsApp quick replies or email templates.', 'Turn today\'s call notes into CRM entries with the second prompt line.'],
 """Our policies: [refunds, delivery, warranty, hours].
1. Draft a reply to this complaint: "[paste]". Acknowledge, take responsibility where appropriate, explain, offer a fix, end with a clear next step. Under 100 words, warm and professional.
2. Write quick replies for these 5 common questions: [list].
3. Turn these call notes into a CRM entry: summary, needs, next action, date: [notes].""",
 "Set up your reply bank and use it on real conversations today.", "Never promise refunds or discounts outside policy because an AI draft suggested it.", ['projects', 'clear'])

# ===== Freelancers & Creatives =====
tday('creative', 8, 'Client Briefs to Creative Direction', 'Your assistant',
 "Clients rarely give good briefs. AI helps you turn a vague request into a clear creative brief, ask the right questions and propose 3 distinct directions. That makes you look strategic, not just a pair of hands.",
 ['Take a real (or recent) client request.', 'Run the prompt.', 'Send the questions to the client.', 'Present the 3 directions as options.'],
 """Client request: "[paste]". Client: [business, audience, brand guide if any].
1. Turn this into a creative brief: objective, audience, key message, tone, deliverables, deadline, success measure.
2. List the questions I must ask the client.
3. Propose 3 distinct creative directions (name, idea, example headline, visual style).""",
 "Use this on your next real client request.", "Don't present AI ideas as finished strategy. Refine them with your expertise.", ['clear'])
tday('creative', 9, 'Content Calendars & Copy at Speed', 'Your assistant + brand voice examples',
 "Planning and writing a month of content is where AI saves freelancers the most time. The key to quality is voice: give the AI 3 examples of the client's best past posts and a list of words to use and avoid, so the output sounds like the brand.",
 ['Collect 3 strong past posts and the brand guide.', 'Run the prompt for a 2-week calendar.', 'Edit 3 posts to perfection.', 'Get client approval.'],
 """Brand: [client]. Audience: [who]. Goal this month: [goal].
<examples>[3 past posts that performed well]</examples>
Create a 2-week content calendar (table: date | platform | pillar | hook | caption | CTA | visual idea), matching the voice in the examples. Then write 3 posts in full.""",
 "Deliver real client content (or your own) using this workflow.", "Watch for clichés and repeated phrases across posts. Clients notice.", ['examples'])
tday('creative', 10, 'Visuals with AI: Images, Mockups & Designs', 'ChatGPT images · Canva AI · Ideogram · Firefly',
 "Image tools now handle text in images, consistent styles and edits by instruction. Use them for concepts, mockups, social graphics and photo clean-up. Describe like an art director: subject, setting, lighting, angle, style, colours, space for text, aspect ratio.",
 ['Write an art-director prompt for a real deliverable.', 'Generate 4 variations and pick one.', 'Edit by instruction ("make the background plain", "move text to the top").', 'Finish in Canva with brand fonts and logo.'],
 """Create an image for [client/brand]: [subject] in [setting], [lighting], [camera angle], [style], colour palette [brand colours], space at the [top/bottom] for a headline, aspect ratio [4:5 / 9:16 / 16:9]. No text in the image.""",
 "Produce one real visual for a client or your own portfolio.", "Check licence terms for commercial use, and never generate images of real people without consent.", ['oa_lib'])
tday('creative', 11, 'Video Scripts, Captions & Repurposing', 'Your assistant · CapCut · Descript',
 "One long video, podcast or blog post can become 10 pieces of content. AI finds the best moments, writes hooks for each platform, adds captions and suggests edits. Scripts written for the ear (short sentences, strong first 3 seconds) perform better.",
 ['Take one long piece of content (transcript or article).', 'Run the prompt.', 'Edit 2 clips in CapCut/Descript with auto-captions.', 'Schedule or deliver them.'],
 """From this transcript/article: [paste]
1. Find 5 moments for 30-60s short videos: quote the start/end, hook (first line on screen), why it works.
2. Write captions for TikTok, Instagram and LinkedIn for the best one.
3. Write a 45-second script version of the main idea for a talking-head video.""",
 "Repurpose one real piece of content into at least 3 assets.", "Only repurpose content you own or have permission to use.", ['chain'])
tday('creative', 12, 'Client Management: Proposals, Pricing & Revisions', 'Your assistant',
 "The business side is where freelancers lose time and money. AI helps you write proposals, set clear packages, handle scope creep politely, chase late payments and write invoices and contracts summaries. Clear communication protects your time.",
 ['Pick one client situation (new pitch, scope creep or late payment).', 'Run the prompt.', 'Edit and send.', 'Save the message as a template.'],
 """Help me with this client situation: [describe, e.g. client asking for extra revisions beyond scope / invoice 2 weeks late / new client wants a quote].
Write a firm but friendly message that protects the relationship and my time. Offer options (e.g. paid extra revisions at ₦X, or a package upgrade).
Then suggest how my packages or contract could prevent this next time.""",
 "Send one real client message you've been putting off.", "Keep agreements in writing. AI drafts don't replace a proper contract.", ['clear'])

# ===== Small Business Owners =====
tday('biz', 8, 'Customer Replies & WhatsApp Business Set-up', 'WhatsApp Business + your assistant',
 "Slow or unclear replies lose sales. Set up WhatsApp Business properly (catalogue, greeting, away message, quick replies, labels) and use AI to write answers to your 10 most common questions in your brand's voice.",
 ['Switch to WhatsApp Business if you haven\'t. Add your catalogue and business hours.', 'List your 10 most common customer questions.', 'Run the prompt and save the answers as quick replies (type "/" to use).', 'Set labels: New lead, Paid, Delivered, Follow up.'],
 """I run {role_short}. Policies: [prices, delivery areas/fees, payment options, returns].
Write: a greeting message, an away message, and quick replies for these 10 questions: [list].
Friendly, short (under 50 words each), in [English / Pidgin / both], each ending with a clear next step (e.g. "Send your address to confirm").""",
 "Use your new quick replies on real customer chats today.", "Keep prices and policies up to date, or quick replies will mislead customers.", ['oa_smb'])
tday('biz', 9, 'Sales Copy: Posts, Broadcasts & Flyers', 'Your assistant + Canva',
 "Good sales copy speaks to the customer's problem and makes the next step obvious. AI writes captions, broadcasts and flyer text using proven structures (AIDA, PAS). Your job: give real product details and customer words, and check prices and dates.",
 ['Pick one product or offer to promote this week.', 'Run the prompt.', 'Design the flyer in Canva using the text.', 'Send the broadcast only to customers who opted in.'],
 """Product/offer: [name, price, key benefit, deadline]. Customers: [who they are, what they care about].
Write: (1) an Instagram caption using AIDA; (2) a WhatsApp broadcast under 60 words using PAS; (3) flyer text: headline under 7 words, 3 bullets, price, call to action.
Then critique all three as a busy customer scrolling on a phone and improve them.""",
 "Publish or send one real promo today.", "Don't make claims you can't back up (\"best in Lagos\", \"100% guaranteed\").", ['examples'])
tday('biz', 10, 'A Simple Marketing Plan for the Month', 'Your assistant',
 "Most small businesses post randomly. A one-page monthly plan, with goal, offers, content themes and a posting schedule, keeps you consistent. AI drafts it from your goals and calendar (paydays, holidays, events). You keep it realistic for your time and budget.",
 ['Set one goal for the month (e.g. 50 orders, 20 new customers).', 'Run the prompt.', 'Cut anything you won\'t realistically do.', 'Put the posting days in your calendar.'],
 """My business: {role_short}. Goal this month: [goal]. Budget for ads: ₦[amount or 0]. Time I can spend: [hours/week].
Create a one-page marketing plan: key dates this month (paydays, holidays), 2 offers, 3 content themes, a 4-week posting schedule (3 posts/week), and one low-cost way to get new customers.""",
 "Plan your real next 4 weeks of marketing.", "A plan you'll follow beats an impressive plan you won't.", ['oa_smb'])
tday('biz', 11, 'Money: Pricing, Budget & Stock Tracking', 'Sheets + your assistant',
 "AI can build simple tools to track sales, expenses and stock, calculate real profit per product, and help you think through pricing. Upload your sales or stock sheet (no bank details) and ask clear questions.",
 ['Upload {data} (remove customer phone numbers).', 'Run the prompt.', 'Check profit for one product by hand.', 'Set a weekly reminder to update the sheet.'],
 """I've uploaded my sales/stock sheet. Columns: [list].
1. Calculate profit per product (price minus cost) and rank them.
2. Show my best and worst sellers this month.
3. Flag items to reorder (stock below [number]).
4. Suggest 2 pricing changes, explaining the trade-offs.
Give me the Google Sheets formulas so I can update it myself.""",
 "Build your real tracking sheet and make one decision from it.", "AI isn't an accountant. For tax and formal accounts, use a professional.", ['oa_applied'])
tday('biz', 12, 'Competitor Check & Customer Feedback', 'Web search + your assistant',
 "Knowing what competitors offer and what customers really say helps you improve. AI can summarise competitors' public offers and prices, and analyse your reviews and messages for patterns: what customers love, complain about and ask for.",
 ['Collect 10–20 reviews or customer messages (remove names).', 'Run the prompt.', 'List 3 competitors and check their public pages.', 'Choose one improvement to make this month.'],
 """Part 1: Here are customer reviews/messages (names removed): [paste]. Group them into: what they love, complaints, requests. Quote examples.
Part 2: Compare my offer with these competitors' public information: [names/links]. Table: product range, price level, delivery, unique selling point.
Then recommend 3 improvements for my business, ranked by impact vs effort.""",
 "Make one real improvement based on what you found.", "Use only public competitor information, and don't copy their content.", ['halluc'])

# ===== Students, Researchers & Educators =====
tday('student', 8, 'Study Plans & Your AI Tutor', 'ChatGPT study mode · Claude learning mode · Gemini',
 "AI can help you learn faster, or help you avoid learning. The difference is how you use it. Study and learning modes act like a tutor: they ask you questions and make you think instead of handing you answers. Combine that with a realistic study plan built around your exam dates and timetable.",
 ['Turn on study/learning mode if your assistant has it (or use the prompt).', 'Build a study plan for your next exam or deadline.', 'Do a 15-minute tutor session on one hard topic.', 'Finish with a 5-question quiz.'],
 """I'm a [level] student. Course: [course]. Exam/deadline: [date]. Hours available per week: [X].
1. Build a week-by-week study plan with short daily sessions and revision days.
2. Then be my tutor on [topic]: don't just explain, ask me questions one at a time, wait for my answers and correct me. Start by checking what I already know.""",
 "Follow your plan for the next 7 days.", "If AI does the thinking for you, you won't remember it in the exam.", ['oa_students', 'limits'])
tday('student', 9, 'Reading & Summarising Papers Properly', 'NotebookLM · File upload',
 "Upload a paper or chapter and get a structured summary, but insist on quotes and page references so you can check and cite correctly. NotebookLM keeps answers grounded in your sources with citations, and can make an audio overview for revision.",
 ['Upload {doc} to NotebookLM or your assistant.', 'Run the prompt.', 'Check 3 quotes against the paper.', 'Write your own 5-line summary from memory, then compare.'],
 """Read the uploaded paper/chapter fully.
1. Summarise: research question, method, sample, key findings, limitations. Quote the supporting sentence with page numbers for each.
2. Explain the hardest concept in simple terms.
3. List 3 critical questions a strong student would ask about this paper.
Only use the document; say "not stated" if missing.""",
 "Summarise one real reading from your course or research this way.", "Always cite the original source, not the AI summary.", ['longdoc', 'oa_students'])
tday('student', 10, 'Finding & Verifying Sources for Literature Reviews', 'Consensus · Elicit · Perplexity · Google Scholar',
 "Research tools like Consensus and Elicit search academic papers. Perplexity and deep research modes search the wider web. They speed up finding sources dramatically, but AI can still invent or mis-cite papers. The rule: every source you cite must be one you have found and opened yourself.",
 ['Run your research question in Consensus or Elicit.', 'Use the prompt to plan your search and structure.', 'Open every paper you intend to cite (Google Scholar, library access).', 'Build a source table with full references.'],
 """My research topic: [topic]. Level: [undergraduate / MSc / PhD].
1. Suggest search keywords and synonyms for academic databases.
2. Propose a structure for my literature review (themes, not paper-by-paper).
3. Create a source-tracking table template: author | year | title | method | key finding | relevance | verified? (Y/N).
Do NOT list specific papers unless you mark them "to verify".""",
 "Start a real literature review source table for your project.", "Fake references are a serious academic offence. Verify every citation exists and says what you claim.", ['halluc', 'oa_students'])
tday('student', 11, 'Writing With Integrity: Outlines, Feedback & Proofreading', 'Your assistant',
 "The ethical, effective way to use AI in academic writing is as a coach: brainstorm, outline, give feedback on your draft, check clarity and grammar. You write the substance. Always follow your institution's AI rules and disclose AI help where required.",
 ['Check your institution/course rules on AI use.', 'Write your own draft paragraph or section.', 'Run the feedback prompt.', 'Revise it yourself based on the feedback.'],
 """Act as a strict but helpful lecturer. Here's my draft: <draft>[paste your own writing]</draft>
Give feedback on: argument clarity, structure, use of evidence, academic tone, grammar. Point to specific sentences.
Do NOT rewrite it for me. Ask me questions that will help me improve it myself.""",
 "Improve one real piece of your writing with AI feedback, without letting AI write it.", "Submitting AI-written work as your own can be academic misconduct. When in doubt, ask your lecturer.", ['oa_students', 'fluency'])
tday('student', 12, 'Presentations, Group Work & Career Prep (Educators: Lesson Plans)', 'Gamma · Canva · your assistant',
 "Students: AI helps plan group projects, build presentation slides and prepare CVs, internship applications and interview practice. Educators: AI drafts lesson plans, activities, quizzes and marking guides aligned to your objectives. You review everything for accuracy and fit.",
 ['Choose: a presentation, a group project plan, a CV/application, or (educators) a lesson plan.', 'Run the prompt.', 'Edit and check for accuracy.', 'Use it in real life this week.'],
 """[Students] Help me with [presentation on X / group project plan / CV for an internship in Y]: create a structured outline, then ask me what details to add from my own experience.
[Educators] Create a 40-minute lesson plan on [topic] for [class/level]: objectives, starter, main activity, check for understanding (5 questions with answers), and differentiation for weaker and stronger learners.""",
 "Produce one real presentation, application or lesson plan.", "Check facts in slides and lesson materials. Students and examiners will.", ['oa_students', 'oa_edu'])

# Short role phrase for small-business prompts
for k, v in TRACKS.items():
    v['role_short'] = 'a small fashion and accessories business on Instagram and WhatsApp' if k == 'biz' else v['role']
