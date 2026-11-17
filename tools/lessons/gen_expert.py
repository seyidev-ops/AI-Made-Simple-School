# AI Expert User: Weeks 5-12 (Days 21-60). Weeks 1-4 (Days 1-20) are shared with Mastery to Money.
# Month 1 = Days 1-20, Month 2 = Days 21-40, Month 3 = Days 41-60 (matches the admin panel and home-page syllabus).
E = []
def L(d, w, t, tool, task, inc, notes, idea, prompt, watch, src):
    mo = 2 if d <= 40 else 3
    E.append({'d': d, 'w': w, 'mo': mo, 'ph': mo, 't': t, 'tool': tool, 'task': task, 'inc': inc,
              'notes': notes, 'deep': {'idea': idea, 'prompt': prompt, 'watch': watch, 'src': src}})
def S(x): return {'s': 'step', 'x': x}
def H(x): return {'s': 'hl', 'x': x}
def T(x): return {'s': 'tip', 'x': x}
def W(x): return {'s': 'warn', 'x': x}
def C(*x): return {'s': 'check', 'x': list(x)}

# ================= WEEK 5 · Marketing & content =================
L(21,5,'Know Your Customer with AI','Claude / ChatGPT',
 'Build a one-page customer profile and brand voice guide for your business or job.',
 'Every post and message from now on starts from this page',
 [S('<strong>Gather real material first:</strong> 5 customer WhatsApp messages, 3 reviews, your 3 best-selling products or services. Remove names and phone numbers.'),
  S('<strong>Paste it in</strong> and ask the AI to describe your typical customer: who they are, what they want, what worries them, the words they use.'),
  H('Ask for the customer\'s own words. "Fast delivery" from a review is more powerful in an advert than any phrase the AI invents.'),
  S('<strong>Voice guide:</strong> ask for 5 words that describe how your brand sounds, plus phrases to use and phrases to avoid.'),
  T('Save this as a document. In Claude, put it inside a Project so every future chat already knows your customer.'),
  C('Customer profile written from real messages','Voice guide with words to use and avoid','Saved where you can reuse it')],
 "Marketing is about the customer, not the product. AI can't guess your customers well from nothing, but it is very good at finding patterns in real material you give it: messages, reviews, questions. This is Anthropic's \"context\" principle at work. The more real detail you provide, the more specific and useful the output. Today's document becomes the context for every marketing prompt you write from now on.",
 """Here are real messages and reviews from my customers (names removed):
<customer_messages>
[paste 5-10]
</customer_messages>

From these only:
1. Describe my typical customer: situation, goals, worries, what makes them buy.
2. List phrases customers actually use that I should reuse in my marketing.
3. Write a brand voice guide: 5 tone words, 5 phrases to use, 5 to avoid.
Don't invent details that aren't supported by the messages.""",
 "Never paste customers' names, phone numbers or account details into an AI tool. Remove them first.",
 ['clear','projects','xml'])

L(22,5,'A Month of Posts in One Sitting','Claude / ChatGPT + Canva',
 'Plan 4 weeks of social posts (3 per week) for your business or professional page.',
 '12 posts planned, so no more "what do I post today?"',
 [S('Open your Day 21 customer profile and paste it into the chat first.'),
  S('Ask for content pillars: 3–4 themes your customers care about (e.g. tips, behind the scenes, results, offers).'),
  H('A good mix: about half helpful content, a quarter proof (reviews, results), a quarter offers. All-offer pages get ignored.'),
  S('Ask for 12 post ideas as a table: date, pillar, hook (first line), key message, call to action.'),
  S('Write 3 of the posts in full now, and design one in Canva.'),
  C('Content pillars agreed','12-post calendar in a table','3 posts written, 1 designed')],
 "Consistency matters more than brilliance on social media, and planning is what makes it possible. Doing a month's thinking in one session with AI is a classic example of what Anthropic calls augmentation. You stay in charge of what you say. The AI handles the blank-page problem and the structure.",
 """Here is my customer profile and brand voice: [paste Day 21 document].

Create a 4-week content calendar, 3 posts per week, as a table:
date | pillar | hook (first line, under 10 words) | key message | call to action.
Mix: ~50% helpful tips, ~25% proof (results, reviews), ~25% offers.
Then write posts 1-3 in full in my brand voice.""",
 "Don't schedule a month of posts and forget them. Leave room for real moments, such as a new product, a holiday or a customer story.",
 ['examples','fluency'])

L(23,5,'Captions, Ads & Broadcasts That Sell','Claude / ChatGPT',
 'Write a product caption, a WhatsApp broadcast and a short ad using a copywriting framework.',
 'Sales copy for your next promo, ready to send',
 [S('<strong>Learn two frameworks:</strong> AIDA (Attention, Interest, Desire, Action) and PAS (Problem, Agitate, Solution).'),
  S('Pick one product or service. Ask for a caption with AIDA and a WhatsApp broadcast with PAS.'),
  H('WhatsApp broadcasts: short, personal, one offer, one clear action. Open with the customer\'s name if your tool allows it. Never send long paragraphs.'),
  S('Ask the AI to review its own copy as a busy customer scrolling on a phone: what would make them stop, and what would make them skip?'),
  W('Only broadcast to people who saved your number or opted in. Spamming gets your WhatsApp Business account restricted.'),
  C('AIDA caption written','PAS broadcast written','Revised after the "busy customer" review')],
 "Frameworks like AIDA and PAS are just proven structures for persuasion. AI knows them well, so naming the framework is a short, clear instruction. The bigger lesson is asking the AI to critique from the reader's point of view. Getting a second perspective on your own work is one of the most useful things AI can do, and it costs you one extra prompt.",
 """Product: [name, price, key benefit]. Customer: [paste profile].

1. Write an Instagram caption using AIDA (under 120 words).
2. Write a WhatsApp broadcast using PAS (under 60 words, one clear action).
3. Now act as a busy customer scrolling on a phone. Tell me honestly what would make you stop and what would make you skip each one. Then rewrite both to fix the weak spots.""",
 "Don't make claims you can't prove (\"best in Lagos\", \"guaranteed results\"). It erodes trust, and advertising rules apply to small businesses too.",
 ['role','chain'])

L(24,5,'Get Found on Google: SEO Basics with AI','Claude / ChatGPT + Google Search',
 'Write or improve one web page or blog post so it answers what your customers search for.',
 'One page that can bring customers for years',
 [S('<strong>Find the questions:</strong> type your topic into Google and note the "People also ask" questions and the autocomplete suggestions.'),
  S('Give those real questions to the AI and ask for an article outline that answers them clearly.'),
  H('Search engines (and the AI answers inside them) favour pages that answer a question clearly, early and with real expertise. Write for the person first.'),
  S('Write the article, then ask for a title under 60 characters and a meta description under 155 characters.'),
  T('Optional: tools like Surfer SEO give keyword suggestions. Useful later, but not required to start.'),
  C('Collected real search questions','Article outline and draft','Title and meta description written')],
 "SEO (search engine optimisation) means making your pages easy to find. In 2026 many searches end in an AI-written summary, and those summaries draw on pages that are clear, specific and trustworthy. So the fundamentals matter more than tricks: answer real questions, show real experience and keep it readable. Use AI to structure and draft, and add the local, first-hand detail only you know.",
 """My business: [what, where]. Customers search for questions like these (from Google):
[paste 5-8 real questions]

1. Create an article outline that answers them, most important first.
2. Write the article (600-800 words), plain English, with short paragraphs and subheadings phrased as questions.
3. Mark 3 places where I should add my own experience or a local example.
4. Give a title (under 60 characters) and meta description (under 155).""",
 "Don't publish dozens of AI articles with no real expertise in them. Search engines and readers both treat thin content as low quality.",
 ['examples','limits'])

L(25,5,'Weekly Challenge: A Mini Campaign','All Week 5 tools',
 'Plan and produce a 1-week mini campaign: 3 posts, 1 broadcast, 1 flyer, all with one message.',
 'A complete campaign you can actually run',
 [S('Pick one real goal: e.g. "sell 20 units of X this week" or "get 10 enquiries for Y".'),
  S('Write a one-paragraph campaign brief: goal, audience, single message, offer, deadline.'),
  S('Produce the assets with this week\'s prompts: 3 posts, 1 broadcast, 1 flyer in Canva.'),
  H('Consistency check: same offer, same price, same deadline, same call to action on every asset.'),
  C('Brief written','5 assets produced','Consistency check done')],
 "A campaign is several pieces working together towards one goal. Today you practise directing AI across multiple outputs while keeping them consistent, and that skill transfers to every bigger project. Start with a brief, chain your prompts step by step, and check everything against the brief at the end.",
 """Campaign brief: Goal: [x]. Audience: [y]. Single message: [z]. Offer and deadline: [ ].
Using my brand voice [paste], create:
1. 3 social posts (Mon, Wed, Fri) that build up to the deadline
2. 1 WhatsApp broadcast for Thursday
3. Text for 1 flyer: headline, 3 bullets, call to action
Then check all 5 for consistency (offer, price, date, call to action) and list any mismatches.""",
 "Check the final assets yourself. AI consistency checks help but can miss a wrong date or price.",
 ['chain','fluency'])

# ================= WEEK 6 · Research & data =================
L(26,6,'Deep Research with Sources','Perplexity / Claude Research / Gemini Deep Research',
 'Produce a 1-page research brief on a question that matters to your work, with sources you have checked.',
 'Better decisions, backed by evidence',
 [S('Choose a real question: a market, a regulation, a competitor, a supplier option.'),
  S('Run it in a research mode (Perplexity, Claude with web search/Research, or Gemini Deep Research). These search many sources and write a cited report.'),
  H('Open at least 3 of the sources. Check that each one actually says what the summary claims, and how recent it is.'),
  S('Ask a follow-up: "What are the strongest arguments against this conclusion?"'),
  W('For laws, tax, health or money decisions, use official sources (government sites, regulators) and a professional, not just AI.'),
  C('Research report generated','3+ sources opened and checked','Counter-arguments requested')],
 "Research modes are AI agents: they plan searches, read many pages and combine what they find. That saves hours, but it also means mistakes can hide inside a confident, well-formatted report. Anthropic's course on AI capabilities explains that models are strongest on mainstream, well-covered topics and weakest on rare, recent or local ones. Many Nigerian business questions fall into that second group. So treat the report as a good first draft of your research, not the final word.",
 """Research question: [your question, with country/city and timeframe].

Please:
- Search recent, reliable sources (official sites and established outlets first).
- Cite every factual claim.
- Separate "well-supported" findings from "uncertain or disputed" ones.
- End with: the 3 strongest counter-arguments, and what I should verify with a professional.""",
 "A long report can feel more trustworthy than it is. Length is not accuracy.",
 ['limits','halluc','fluency'])

L(27,6,'NotebookLM: Your Documents as a Study Partner','NotebookLM / Claude Projects',
 'Load 3–5 documents about one topic and use AI to question, summarise and turn them into an audio overview.',
 'A personal expert on your own documents',
 [S('Go to notebooklm.google.com. Create a notebook and upload 3–5 sources: PDFs, Google Docs, web links, YouTube videos.'),
  S('Ask questions. Every answer cites the exact passage in your documents, so click the citations to check.'),
  H('This is called grounding: the AI answers from your material rather than its general memory. It is the most reliable way to use AI on facts.'),
  S('Generate an Audio Overview (a podcast-style discussion of your sources) and listen on your commute.'),
  T('Claude Projects work the same way: upload files once, then every chat can draw on them.'),
  C('Notebook with 3+ sources','Asked 3 questions and checked citations','Generated an audio overview')],
 "Most AI mistakes happen when the model answers from memory. When you give it your own documents and ask it to answer only from them, with citations, accuracy goes up sharply. Anthropic's guidance for long documents says the same: give the material, ask for quotes, then the answer. NotebookLM and Claude Projects both make this easy for non-technical users.",
 """Using ONLY the sources in this notebook/project:
1. What are the 5 most important points across all documents? Cite each.
2. Where do the documents disagree with each other?
3. What important question do these documents NOT answer?
If something isn't in the sources, say "not in the sources".""",
 "Check the uploaded files are the right versions. The AI will faithfully cite an outdated policy if that's what you gave it.",
 ['longdoc','projects','halluc'])

L(28,6,'Spreadsheets with AI','Claude / ChatGPT / Gemini in Sheets',
 'Use AI to clean a messy spreadsheet, write formulas you didn\'t know and explain them.',
 'Spreadsheet work in minutes, not hours',
 [S('Take a real spreadsheet (sales, expenses, stock) or create a sample one. Remove sensitive data.'),
  S('Describe what you want in plain English: "a column showing profit per item" or "total sales by month".'),
  H('Always ask the AI to explain the formula in one line. If you can\'t follow the explanation, you can\'t spot when it\'s wrong.'),
  S('Upload the file to Claude or ChatGPT and ask for 3 insights. These tools can run the calculations for you.'),
  S('Spot-check: calculate one number by hand and compare.'),
  C('One task solved with a formula','Formula explained in plain English','One result checked by hand')],
 "AI assistants can now read spreadsheets and run real calculations. They write and run code behind the scenes rather than guessing numbers, which makes them far more reliable for maths than a plain chat. Your job is to define the question clearly and spot-check the result. Anthropic's AI Fluency course calls this Discernment: judging the process, not just the final answer.",
 """I've uploaded a spreadsheet of [what it contains]. Columns: [list].

1. Check for problems (blanks, duplicates, text in number columns) and tell me how you'd fix them.
2. Calculate [what you need, e.g. total and average sales per month].
3. Give me the Google Sheets / Excel formula for each calculation, with a one-line explanation.
4. Show your working for one result so I can check it by hand.""",
 "Don't upload customer, staff or financial data your employer hasn't approved for AI tools. Use a sample or anonymised copy.",
 ['fluency','limits'])

L(29,6,'Charts & Reports from Data','Claude / ChatGPT / Julius AI',
 'Turn a spreadsheet into 2 clear charts and a one-page summary someone can act on.',
 'Reports your boss or partner will actually read',
 [S('Use your Day 28 spreadsheet. Ask the AI: "What are the 3 most useful charts for a business owner to see from this data?"'),
  S('Generate the charts. Claude, ChatGPT and Julius AI can all draw them from your file.'),
  H('A good chart title states the finding ("Sales dropped 20% in August"), not just the topic ("Sales by month").'),
  S('Ask for a one-page summary: what happened, why it might have happened (marked as possibilities), and what to do next.'),
  C('2 charts with finding-style titles','One-page summary','Possible causes clearly marked as guesses')],
 "Data only helps if it leads to a decision. AI is good at both the mechanics (charts, calculations) and the first draft of the story. It cannot know why your sales dropped in August. It can only suggest possibilities. Keep a clear line between what the data shows and what is interpretation. Your knowledge of the business fills the gap.",
 """Using the data I've uploaded:
1. Recommend the 2 most useful charts for a small business owner and create them.
2. Give each chart a title that states the finding.
3. Write a one-page summary: What happened (facts from the data) / Possible reasons (clearly labelled as possibilities) / 3 recommended actions.""",
 "Correlation is not cause. If the AI says sales fell because of rain, ask how it knows.",
 ['artifacts','fluency'])

L(30,6,'Weekly Challenge: Evidence-Based Decision','Consensus / Perplexity / NotebookLM',
 'Make one real decision using AI research, your own documents and your data. Write it up in one page.',
 'One decision made with evidence, not guesswork',
 [S('Pick a real decision: a new product, a supplier, a price change, a training choice.'),
  S('Research it (Day 26), check your own documents (Day 27) and look at your numbers (Days 28–29).'),
  T('For questions about health, education or other research topics, Consensus.app searches academic papers. It is useful when you want studies, not blogs.'),
  S('Write a one-page decision memo: options, evidence for each, recommendation, risks.'),
  H('Ask the AI to argue for the option you didn\'t choose. If its argument changes your mind, good. If not, you\'re more confident.'),
  C('Evidence from 3 types of source','One-page decision memo','Tested against the opposite view')],
 "This week's skill is combining sources: the web, your own documents and your data. That is how professionals use AI for decisions. It also shows the 4th D, Diligence. You own the decision and can explain why you made it. \"The AI said so\" is never a good enough reason.",
 """Decision: [describe]. Options: [A, B, C].
Here's my evidence: <research>[paste]</research> <my_data>[paste summary]</my_data>

1. Summarise the evidence for and against each option in a table.
2. Recommend one and explain why.
3. Then argue as strongly as you can for the option you did NOT recommend.""",
 "Keep your memo. Revisit it in a month to see if the decision worked. That's how your judgement improves.",
 ['fluency','chain'])

# ================= WEEK 7 · Automation =================
L(31,7,'Think in Workflows','Pen & paper + Claude',
 'Map 3 repetitive tasks from your week as trigger → steps → result, and pick one to automate.',
 'Your first automation target chosen',
 [S('List tasks you do the same way every week: sending receipts, copying form answers into a sheet, reminding customers.'),
  S('For each, write: <strong>Trigger</strong> (what starts it) → <strong>Steps</strong> → <strong>Result</strong>.'),
  H('Automation works on rules: "when a form is submitted, add a row and send an email". If a task needs judgement every time, it might need AI in one step, or it might be better done by you.'),
  S('Score each: minutes saved per week × how often it goes wrong when done by hand. Pick the highest.'),
  C('3 tasks mapped','Each scored','One chosen for this week')],
 "Before any tool, learn to see your work as a workflow. Anthropic's AI Fluency course describes three ways to work with AI. Automation means AI does a defined task. Augmentation means you and AI work together. Agency means AI acts more independently towards a goal. Most real gains for individuals and small businesses come from simple automation of boring, repeatable steps. Anthropic's engineering team gives the same advice for building with AI: start with the simplest thing that works.",
 """Here are 3 tasks I repeat every week: [describe each in a few sentences].
For each:
1. Write it as Trigger → Step 1 → Step 2 → … → Result.
2. Mark which steps are pure rules and which need judgement.
3. Estimate minutes saved per week if automated.
Recommend which to automate first and why.""",
 "Don't automate a messy process. Tidy it up by hand first, or you'll just make mistakes faster.",
 ['fluency','agents'])

L(32,7,'Your First Zap: Form → Sheet → Email','Zapier + Google Forms + Gmail',
 'Build an automation: when someone fills a form, add them to a sheet and send a thank-you email.',
 'Your first working automation',
 [S('Create a Google Form (name, email, what they need). Link it to a Google Sheet.'),
  S('In Zapier: Trigger = "New Form Response" → Action 1 = "Create Spreadsheet Row" (or skip if linked) → Action 2 = Gmail "Send Email".'),
  S('Use the form fields in your email: "Hi {{name}}, thanks for…".'),
  H('Test with your own details first. Zapier shows each step\'s result. Green ticks mean it worked.'),
  T('Stuck? Describe the error message to Claude or ChatGPT. They\'re very good at fixing automation problems.'),
  C('Form and sheet connected','Zap built and switched on','Tested with your own entry')],
 "A Zap is a small program you build by clicking instead of coding. Every automation tool works the same way: a trigger, then actions, with data passed from one step to the next. Once you understand that pattern, you can learn any automation tool in an afternoon. Zapier also has an AI builder, so you can describe the Zap in a sentence and then check and adjust what it builds.",
 """I'm building my first Zapier automation:
When someone submits my Google Form (fields: [list]), I want to [add them to a sheet] and [send them a thank-you email].
Give me step-by-step click instructions, the email text using the form fields, and the 3 most common errors beginners hit with this Zap and how to fix them.""",
 "Check the free plan limits (number of tasks per month) so your automation doesn't silently stop.",
 ['agents'])

L(33,7,'Add an AI Step: Make.com Scenario','Make.com + Claude / OpenAI module',
 'Build a scenario where AI reads each new enquiry, labels it and drafts a reply for you to approve.',
 'Enquiries sorted and drafted automatically',
 [S('In Make.com: trigger = new form response or new email. Add an AI module (Anthropic Claude or OpenAI), then a Google Sheets "Add row".'),
  S('In the AI module, write clear instructions (see the prompt below). Ask for a fixed output format so the next step can use it.'),
  H('Keep a human in the loop: AI drafts go into a sheet or your drafts folder. You approve before anything is sent.'),
  S('Test with 5 realistic fake enquiries, including one rude one and one off-topic.'),
  W('AI modules cost money per use. Set a usage limit on your AI account.'),
  C('Scenario with an AI step built','Tested with 5 fake enquiries','Human approval step in place')],
 "This is where automation meets AI. The rule-based steps move data around, and the AI step handles the part that needs understanding, like reading a message and judging what it's about. In Anthropic's terms, this is a workflow: a fixed path where AI does one well-defined job. Workflows are predictable and easy to check, which is why they're the right place to start.",
 """(Instruction for the AI step in Make.com)
You will receive a customer enquiry for [business].
<enquiry>{{message}}</enquiry>

Do three things:
1. Category: one of [order, price question, complaint, other]
2. Urgency: high / normal, with a 5-word reason
3. Draft reply: under 60 words, friendly, in our tone. Never promise prices or dates not given here: [paste key facts].

Reply in exactly this format:
CATEGORY: …
URGENCY: …
DRAFT: …""",
 "Never let an AI step send messages to customers on its own until you've reviewed many of its drafts and trust it.",
 ['agents','xml','role'])

L(34,7,'Follow-ups on Autopilot: Email & WhatsApp','WhatsApp Business + Make.com / Zapier',
 'Set up quick replies and labels in WhatsApp Business, and an automated reminder for one type of follow-up.',
 'No more forgotten follow-ups',
 [S('<strong>WhatsApp Business basics:</strong> set a greeting message, an away message and 5 quick replies (type / to use them) for your most common answers.'),
  S('Use labels (New lead, Paid, Follow up) to see at a glance who needs attention.'),
  S('Build one reminder automation, e.g. a Google Sheet row with a follow-up date triggers an email or calendar reminder to you on that day.'),
  H('Use AI to write your quick replies: paste your 5 most common customer questions and ask for short, friendly answers.'),
  W('Fully automated WhatsApp messaging needs the official WhatsApp Business Platform (API) and an approved provider. Avoid unofficial "bulk sender" apps, which can get your number banned.'),
  C('Greeting, away message and 5 quick replies set','Labels in use','One reminder automation working')],
 "Not every automation needs an AI agent. Many of the biggest wins are simple: templates, labels and reminders that make sure nothing slips. The deeper WhatsApp automations (chatbots, CRM follow-ups) are covered in the WhatsApp Lead Automations and CRM masterclasses included with your programme.",
 """Here are the 5 questions my customers ask most on WhatsApp: [list].
Write a quick reply for each: under 40 words, friendly, ends with a question or clear next step.
Also write: a greeting message for new chats and an away message for after hours, in [English / Pidgin / both].""",
 "Quick replies can sound robotic if overused. Personalise the first line when you can.",
 ['clear'])

L(35,7,'Weekly Challenge: Automate One Weekly Chore','Zapier / Make.com',
 'Fully automate the task you chose on Day 31, document it and measure the time saved.',
 'Hours back every month, for good',
 [S('Build the automation for your Day 31 task, using this week\'s skills.'),
  S('Run it for real (or with realistic test data) at least 3 times.'),
  S('Write a short "how this works" note: trigger, steps, where to check if it breaks, who to call.'),
  H('Measure: minutes per week before vs after. Multiply by 52. That number is the value of what you learnt this week.'),
  C('Automation built and running','Documented in a short note','Time saved measured')],
 "Documenting an automation is as important as building it. If it breaks while you're travelling, someone else (or you, months later) needs to understand it. Write it down as you would for a new colleague. This is Diligence again: taking responsibility for what your AI-powered systems do.",
 """Here's the automation I built: [describe the steps].
Write a one-page "how this works" note for a non-technical colleague: what it does, what triggers it, each step in plain English, how to tell if it's broken, and how to switch it off safely.""",
 "Check your automation again after a week. Small issues (wrong time zone, missing field) often appear only with real use.",
 ['skills','fluency'])

# ================= WEEK 8 · Websites & apps =================
L(36,8,'A One-Page Website from a Prompt','Framer AI / 10Web / Carrd + Claude',
 'Create a simple one-page website for your business or yourself, with a WhatsApp button.',
 'You exist online, professionally',
 [S('Use Claude or ChatGPT to write the content first: headline, short intro, 3 services, 3 reasons to choose you, testimonials, contact.'),
  S('Paste a description into an AI website builder (Framer AI, 10Web) or use a template (Carrd), then paste in your content.'),
  H('Add a "Chat on WhatsApp" button: link it to https://wa.me/234XXXXXXXXXX (your number without the leading 0).'),
  S('Check it on your phone. Most of your visitors will be on mobile.'),
  C('Content written with AI','Site created','WhatsApp button working on mobile')],
 "AI website builders generate layout, design and placeholder text from a description. Like every AI tool, they produce something generic unless you feed them specifics. Writing your content first, with your Day 21 customer profile, is what makes the site yours. The builder is just the frame.",
 """Write the content for a one-page website for [business/you].
Customer profile: [paste Day 21]. Goal of the page: [e.g. get WhatsApp enquiries].
Sections: headline (under 8 words), subheadline, 3 services (2 lines each), 3 reasons to choose us, a short "about", 2 placeholder testimonials marked [REPLACE WITH REAL], and a call-to-action button text.""",
 "Replace every placeholder before publishing, especially testimonials. Fake reviews are illegal in many places and destroy trust.",
 ['clear','examples'])

L(37,8,'Build Small Tools by Describing Them','Claude Artifacts / ChatGPT Canvas',
 'Describe and build a small useful tool, such as a price calculator, quiz or checklist, without coding.',
 'Your own custom tool, in minutes',
 [S('Think of a small tool you or your customers would use: a delivery fee calculator, a loan repayment estimator, a "which product is right for you" quiz.'),
  S('In Claude, describe it. It builds a working version as an Artifact you can use and share. ChatGPT Canvas works similarly.'),
  H('Improve it in small steps: "make the buttons bigger", "add Naira formatting", "add a reset button". One change at a time.'),
  S('Test with real numbers and check the results by hand.'),
  C('Tool described and built','Improved through 3+ rounds of feedback','Results checked by hand')],
 "This is what people call vibe coding: describing what you want and letting AI write the code. For small personal tools it is genuinely useful, and you don't need to read the code. You do need to describe clearly, test carefully and give specific feedback. Those are the same Description and Discernment skills you've used all course.",
 """Build a simple interactive tool: [describe, e.g. "a delivery fee calculator for my Lagos bakery"].
How it works: [inputs → calculation → output, e.g. "choose area from a list, enter number of cakes; fee = area rate + ₦500 per extra cake"].
Design: clean, mobile-friendly, large buttons, prices in ₦ with commas.
Include a reset button and a short instruction line at the top.""",
 "Small personal tools are fine. Anything handling payments, passwords or customer data needs a proper developer's review.",
 ['artifacts','chain'])

L(38,8,'AI Coding Assistants: What They Can Do for You','Cursor / Claude Code (overview)',
 'Understand what AI coding tools do, try one small change with guidance, and know when to hire help.',
 'You can talk confidently about AI-built software',
 [S('Watch a short demo or read about Cursor or Claude Code: tools where AI writes, edits and runs code in a real project.'),
  S('Try a guided exercise: ask Claude (in chat) to create a simple HTML page, then ask it to explain each part in plain English.'),
  H('The big shift: AI coding tools can now plan and build entire features, not just suggest lines. That is why non-programmers can create real software, as long as they can describe it clearly and test it.'),
  S('Write down one idea you\'d build if you had a developer, and describe it as clearly as you can. That description is the most valuable part.'),
  W('Security, payments and personal data are where AI-built software most often goes wrong. Get expert review before launching anything that handles them.'),
  C('Understood what AI coding tools do','Built and had explained one simple page','Wrote a clear description of one software idea')],
 "AI coding assistants are agents: they read files, write code, run it, see errors and fix them, looping until the task is done. Anthropic publishes free courses on Claude Code if you want to go further. Even if you never code, knowing what these tools can do helps you brief developers, estimate costs and spot opportunities in your job.",
 """I'm not a programmer. Create a simple web page for [purpose] in a single HTML file.
Then explain it to me in plain English: what each section does, what I could easily change myself (text, colours), and what I should NOT change without help.""",
 "Don't believe claims that AI makes developers unnecessary. It makes good developers faster and lets beginners build small things.",
 ['agents','claude101'])

L(39,8,'Forms, Payments & WhatsApp on Your Site','Paystack / Flutterwave + Google Forms',
 'Add a way to collect orders or bookings and a payment link to your Day 36 website.',
 'Your site can take orders and payments',
 [S('Create a Paystack (or Flutterwave) payment page for one product or service. No coding needed; you get a link.'),
  S('Add an order or booking form (Google Forms or Tally) and connect it to a sheet.'),
  S('Put both on your site with clear buttons: "Pay now" and "Book / Order".'),
  H('Use AI to write the confirmation message customers see after paying: what happens next, when, and who to contact.'),
  C('Payment link created and tested','Order/booking form connected to a sheet','Buttons added to your site')],
 "Taking payments online used to need a developer. Payment pages and form tools now let anyone do it. Today is less about AI and more about connecting the pieces, with AI helping you write clear instructions and messages. Clear communication around payments builds the trust that gets people to pay online.",
 """Write the customer messages for my online orders for [business]:
1. Text above the "Pay now" button (what they're paying for, what happens next)
2. The confirmation message after payment
3. A short FAQ (5 questions) about delivery, refunds and contact
Friendly, clear, reassuring. Customers may be nervous about paying online.""",
 "Test the full flow with a real small payment before sharing the link, and check the money arrives in your account.",
 ['clear'])

L(40,8,'Month 2 Capstone: Your Online Presence','All Month 2 tools',
 'Bring it together: website, content calendar, one automation and one research-backed decision.',
 'Month 2 complete: you work like a modern professional',
 [S('Review your Month 2 outputs: customer profile, content plan, research memo, spreadsheet report, automation, website.'),
  S('Fix the weakest one. Ask AI to review it as a customer or boss would.'),
  S('Make a one-page "my AI toolkit" summary: the tools you now use, what for, and the prompt you rely on most for each.'),
  H('Share your website and one result (time saved, a sale, a better report) with a colleague or friend. Explaining it reinforces it.'),
  C('Weakest output improved','One-page AI toolkit written','Shared one result with someone')],
 "Month 2 was about bringing AI into real work: marketing, research, data, automation and web presence. Your toolkit page captures what you've learnt in a form you'll keep using. Anthropic's free AI Fluency course is an excellent companion if you want to go deeper on the thinking behind it all.",
 """Here's what I built in Month 2: [list].
Act as a demanding but kind mentor. For each item, tell me one specific way to make it better.
Then help me write a one-page "My AI toolkit": tool | what I use it for | my go-to prompt.""",
 "Don't add more tools for the sake of it. Five you use well beat twenty you've only tried.",
 ['fluency'])

# ================= WEEK 9 · Advanced video =================
L(41,9,'How AI Video Works & Prompting Shots','Runway / Google Veo / Luma',
 'Generate 3 short video clips from text, using film language: shot type, camera movement, lighting.',
 'You can direct AI video like a filmmaker',
 [S('Pick one tool with a free tier: Runway, Luma Dream Machine, Pika, or Veo inside Gemini.'),
  S('Learn 4 terms: <strong>shot type</strong> (wide, medium, close-up), <strong>camera movement</strong> (static, slow push-in, pan, handheld), <strong>lighting</strong> (golden hour, soft studio, neon), <strong>pace</strong> (slow motion, real time).'),
  H('Prompt formula: [shot type] of [subject] [doing what] in [setting], [camera movement], [lighting], [style]. Example: "Close-up of hands kneading dough in a Lagos bakery, slow push-in, warm morning light, documentary style."'),
  S('Generate 3 clips, changing one element each time so you learn what each word does.'),
  C('Learnt 4 film terms','Generated 3 clips','Noted what each change did')],
 "AI video models generate moving images frame by frame from text or an image, keeping motion and lighting consistent. Clips are short (usually 5–10 seconds), so you think in shots, not whole films. Like image tools, they respond to the language professionals use. Changing one thing at a time is the fastest way to learn any AI tool, because you see cause and effect.",
 """Help me plan 3 AI video shots for [business/topic].
For each give: shot type, subject and action, setting, camera movement, lighting, style, and the full prompt to paste into [Runway / Luma / Veo].
Make them work together as the opening of a 15-second promo.""",
 "AI video still struggles with hands, text and complex actions. Plan shots that avoid them, or expect to regenerate.",
 ['examples'])

L(42,9,'Bring Product Photos to Life','Runway / Luma / Kling (image-to-video)',
 'Turn 2 still product photos into short moving clips for social media.',
 'Eye-catching product videos without a film crew',
 [S('Pick 2 good product photos (clean background, good light. Use your Day 7 skills).'),
  S('Upload to an image-to-video tool and describe only the motion: "slow 360° rotation", "steam rising from the cup", "fabric moving gently in a breeze".'),
  H('Image-to-video keeps your real product as the starting point. That is more honest and more consistent than generating the product from text.'),
  S('Choose the best result and trim it to 3–5 seconds.'),
  C('2 photos animated','Motion-only prompts used','Best clip trimmed and saved')],
 "Starting from a real photo gives the AI an anchor, so the product stays recognisable while the scene moves. This is a useful general principle: the more concrete input you give AI (an image, a document, an example), the less it has to invent.",
 """My product: [describe]. I have a photo of it on a [background].
Suggest 5 subtle, premium-looking motions for a 4-second image-to-video clip (e.g. slow rotation, light sweep, gentle steam). For each, give the exact motion prompt and say which platform it suits best.""",
 "Check the product hasn't been changed (shape, logo, colour) in the generated video before you post it.",
 ['examples'])

L(43,9,'A 30-Second Ad, End to End','Claude + ElevenLabs + Runway + CapCut',
 'Script, voice, generate clips and edit a 30-second advert for a real or sample product.',
 'A complete video ad made by you',
 [S('<strong>Script</strong> with Claude: hook (3 sec), problem, solution, proof, call to action. About 70 spoken words.'),
  S('<strong>Voice</strong> with ElevenLabs (Day 16) or record yourself.'),
  S('<strong>Visuals:</strong> mix real footage, image-to-video clips (Day 42) and generated shots (Day 41).'),
  S('<strong>Edit</strong> in CapCut: cut to the voiceover, add captions, add music, export vertical (9:16).'),
  H('Write the shot list and script together, shot by shot, so every line of voiceover has a matching visual.'),
  C('Script and shot list','Voiceover recorded','Edited and exported in 9:16')],
 "This lesson chains everything: writing, voice, video and editing. Planning first (script plus shot list) is what separates a coherent ad from a pile of clips. It's the same prompt-chaining principle as before. Do one clear step at a time, check it, then pass it on.",
 """Write a 30-second vertical video ad for [product] aimed at [customer].
Format as a table: time | voiceover line | on-screen visual (say whether it's real footage, image-to-video, or AI-generated) | on-screen text.
Hook in the first 3 seconds. About 70 spoken words total. End with a clear call to action.""",
 "Use licensed music only. CapCut's built-in library is the safest choice for social media.",
 ['chain'])

L(44,9,'Keeping Your Brand Consistent in AI Video','Runway / CapCut + brand kit',
 'Create a brand video kit (intro, outro, caption style, colours) and apply it to 2 clips.',
 'Every video instantly looks like yours',
 [S('Decide your video brand rules: logo position, caption font and colour, intro/outro (2 seconds each), music style.'),
  S('Build a template in CapCut so you can reuse it for every video.'),
  H('For recurring characters or scenes, use the "reference image" features many AI video tools now offer. Feed the same reference each time for consistency.'),
  S('Apply the template to 2 clips and compare them side by side.'),
  C('Video brand rules written','Reusable template built','Applied to 2 clips')],
 "Consistency is one of AI video's hardest problems, because every generation starts fresh. The fixes are reference images, templates and written rules. That's a pattern you'll see across all of AI: when a tool doesn't remember, you supply the memory through instructions, examples and reusable assets.",
 """Create a one-page video brand guide for [business]:
logo placement, caption font/size/colours (hex), how to highlight key words, intro and outro (2 sec each), music mood, and 5 rules for consistent AI-generated scenes (lighting, colour palette, setting).""",
 "Keep your raw files organised (one folder per video). You'll want to reuse clips.",
 ['personal'])

L(45,9,'Weekly Challenge: Your Promo Video','All Week 9 tools',
 'Produce a finished 30-second promo for a real need (your business, workplace, church, community event) and post or share it.',
 'A real video, seen by real people',
 [S('Choose a real purpose and audience.'),
  S('Make the video using this week\'s process: plan → generate → edit → brand.'),
  H('Add a short note in the caption if AI-generated people or scenes appear, such as "Made with AI tools". Being open about it builds trust.'),
  S('Share it and note one piece of feedback.'),
  C('Video finished','AI use disclosed where relevant','Shared and feedback noted')],
 "Being open about AI-generated content matters more each year. Many platforms now label it, and audiences increasingly expect it. Anthropic's AI Fluency course describes this as part of Diligence: being transparent about how AI contributed to your work, appropriate to the situation.",
 """Here's my finished promo video plan/transcript: [paste].
Write 3 caption options for [platform], each with a natural, short note that AI tools helped create the video. Keep it confident, not apologetic.""",
 "Never generate realistic videos of real people (including public figures) saying things they didn't say.",
 ['fluency'])

# ================= WEEK 10 · Personal learning =================
L(46,10,'AI as Your Personal Tutor','Claude (Learning mode) / ChatGPT (Study mode)',
 'Learn one new concept with AI as a tutor that asks you questions instead of just giving answers.',
 'You learn faster, and it sticks',
 [S('Pick something you want to understand: a work topic, Excel, budgeting, a language, anything.'),
  S('Turn on a learning style if available: Claude\'s Learning mode or ChatGPT\'s Study mode. Or use the prompt below.'),
  H('Tutor mode asks you questions and makes you think, rather than handing you the answer. It feels slower, but research on learning shows active recall makes knowledge stick far better.'),
  S('After 20 minutes, ask it to quiz you on what you covered.'),
  C('Tutor session on one topic','Answered its questions yourself','Passed a short quiz')],
 "AI can make learning easier in a way that backfires: if it does all the thinking, you remember little. That's why Anthropic and others built learning modes that guide you with questions rather than giving answers. Use AI to think harder, not less, and you'll learn faster than you ever have.",
 """I want to learn [topic]. My current level: [beginner / some knowledge]. Why I'm learning: [goal].
Be my tutor. Don't just explain. Teach me step by step by asking me questions, wait for my answer, then correct or build on it.
Start by checking what I already know with 2 questions.""",
 "If you only read AI explanations, you'll feel you understand but forget quickly. Answer the questions yourself before reading on.",
 ['limits','fluency'])

L(47,10,'Build a 30-Day Learning Plan','Claude / ChatGPT + Calendar',
 'Create a realistic 30-day plan to learn one skill, with daily 20-minute tasks, and put it in your calendar.',
 'A plan you can actually follow',
 [S('Choose one skill and a concrete goal: "build a budget spreadsheet on my own" beats "learn Excel".'),
  S('Tell the AI your available time, current level and preferred learning style.'),
  H('A good plan has small daily tasks, a weekly practice project and a clear "how will I know I\'ve learnt it" test at the end.'),
  S('Add the sessions to your calendar as recurring events.'),
  C('Concrete goal set','30-day plan created','Sessions in calendar')],
 "AI is excellent at structure: breaking a big goal into small, sequenced steps. That is exactly what most self-learners lack. Your job is to be honest about your real time and energy, so the plan fits your life and doesn't stay a fantasy.",
 """Create a 30-day learning plan for: [skill]. Goal at the end: [specific outcome].
My level: [x]. Time available: [20 min/day, more on weekends].
Format: Week → daily tasks (20 min each) → weekend practice project.
Include free resources (be specific, and mark any you're unsure exist) and a final test to prove I've learnt it.""",
 "Check any resources the AI recommends actually exist. Course and book suggestions are a common place for made-up titles.",
 ['halluc','chain'])

L(48,10,'Flashcards & Quizzes from Your Notes','NotebookLM / Claude + Anki or Quizlet',
 'Turn your notes or a document into flashcards and a practice quiz.',
 'Revision that takes minutes to set up',
 [S('Upload your notes, a chapter or a training document to NotebookLM or Claude.'),
  S('Ask for 20 flashcards (question on one side, short answer on the other), then a 10-question quiz with explanations.'),
  H('Ask for questions that test understanding ("Why…", "What would happen if…"), not just memory ("What is…").'),
  S('Import the flashcards into Anki or Quizlet, or just use them in the chat.'),
  C('20 flashcards generated from your material','10-question quiz taken','Weak areas identified')],
 "Testing yourself (active recall) and reviewing over spaced intervals are two of the best-proven learning techniques. Creating the materials used to take hours. Now it takes minutes, especially when the AI works from your own documents, which keeps it accurate to what you're actually studying.",
 """From the document I've shared, create:
1. 20 flashcards in the format: Question | Answer (answers under 20 words). Mix "what", "why" and "what would happen if" questions.
2. A 10-question multiple-choice quiz with the correct answer and a one-line explanation for each.
Use only information in the document.""",
 "Check a few answers against the source. If the document is wrong, the flashcards will be too.",
 ['longdoc'])

L(49,10,'Learn Anything Faster: The Explain-Back Method','Claude / ChatGPT',
 'Use the Feynman technique: explain a topic simply to AI and let it find the gaps in your understanding.',
 'Deeper understanding of things that matter at work',
 [S('Pick a topic from your work you "sort of" understand.'),
  S('Explain it to the AI in your own words, as if to a 12-year-old.'),
  H('Ask the AI to play a curious student: point out what\'s unclear, wrong or missing in your explanation. Gaps you can\'t fill show you exactly what to study.'),
  S('Study the gaps, then explain again. Compare the two explanations.'),
  C('First explanation written','Gaps identified by AI','Improved second explanation')],
 "Explaining something is the best test of understanding. Here the AI isn't the teacher. It's the questioner that exposes gaps. This kind of collaboration (you think, AI challenges) is where AI adds the most to your own growth rather than replacing your effort.",
 """I'm going to explain [topic] in my own words. Act as a curious, smart 12-year-old.
After my explanation: ask me the 3 questions a curious student would ask, point out anything unclear or incorrect, and tell me which part I seem least sure about.
Don't explain the topic to me yet. Let me try first.

My explanation: [write it]""",
 "Don't let the AI simply rewrite your explanation for you. The struggle is where the learning happens.",
 ['fluency'])

L(50,10,'Helping Others Learn with AI','Claude / ChatGPT / Gemini',
 'Create a learning activity for a child, a student, a team member or your congregation, using AI responsibly.',
 'You can teach with AI, not just learn',
 [S('Pick someone to help: your child\'s homework topic, a new staff member\'s training, a youth group lesson.'),
  S('Use AI to create a short lesson: explanation, a local example, an activity and 3 questions.'),
  H('For children: use AI to make practice questions and explanations, not to do their homework for them. Sit with them and use tutor mode together.'),
  S('Deliver it and note what worked.'),
  W('Check content for accuracy and age-appropriateness. You are responsible for what you teach.'),
  C('Learning activity created','Delivered to someone','Reflected on what worked')],
 "Teaching others is how AI fluency spreads in families, workplaces and communities. Anthropic has published free AI fluency courses for educators and students alongside the main course, because using AI to support learning, not replace it, is a skill in itself.",
 """Create a 20-minute learning activity on [topic] for [who, e.g. a 10-year-old / new sales staff].
Include: a simple explanation with a Nigerian example, a hands-on activity, 3 questions to check understanding (with answers), and one way to make it fun.
Keep the language right for their level.""",
 "Never upload children's personal information or photos to AI tools.",
 ['fluency'])

# ================= WEEK 11 · Travel & lifestyle =================
L(51,11,'Plan a Trip with AI','Claude / ChatGPT / Gemini + Google Maps',
 'Plan a real or dream trip: itinerary, budget in Naira, and a packing list.',
 'Better trips, planned in a fraction of the time',
 [S('Give the AI your destination, dates, budget, who\'s travelling and what you enjoy.'),
  S('Ask for a day-by-day itinerary with travel times and a budget table.'),
  H('AI is great at structure and ideas, but prices, opening hours and availability change. Check them on official sites or booking platforms before you pay.'),
  S('Ask for a packing list and a "what could go wrong" list with backup plans.'),
  C('Itinerary created','Budget table in ₦','Key details verified on official sites')],
 "Travel planning shows both sides of AI clearly. It's brilliant at organising options and building plans around your preferences. But its knowledge of prices and schedules may be out of date, and it can invent details about small or local businesses. Use web-search mode for current information, and verify anything you'll pay for.",
 """Plan a [number]-day trip to [destination] for [who], [dates], budget about ₦[amount] total (excluding flights / including flights).
We enjoy: [food, history, beaches, shopping…].
Give: day-by-day plan with travel times, a budget table, 3 money-saving tips, and a list of everything I must verify before booking.""",
 "Never book through a link from an AI answer without checking it's the official site. Travel scams often use look-alike websites.",
 ['limits','halluc'])

L(52,11,'Visas, Documents & Official Information','Claude / ChatGPT + official government sites',
 'Build a document checklist for a trip, application or official process, verified against official sources.',
 'Fewer rejected applications and wasted trips',
 [S('Pick a real process: a visa, passport renewal, business registration, exam registration.'),
  S('Ask the AI for a checklist and timeline, with links to official sources.'),
  H('Then go to the official website (embassy, NIS, CAC, exam body) and tick off each item against what it actually says. Note any differences.'),
  S('Ask the AI to turn the verified checklist into a timeline with deadlines.'),
  W('Requirements change often, and AI can be months or years out of date. The official source is always right over the AI.'),
  C('AI checklist created','Every item verified on the official site','Timeline with deadlines')],
 "This lesson is about knowing the limits. AI knowledge has a cut-off and can be confidently wrong about specific rules. Anthropic's course on AI capabilities and limitations explains that models are weakest on niche, recent and fast-changing information, which describes most official requirements. The right approach is to use AI to get organised, then use the official source for the facts.",
 """I need to [process, e.g. apply for a UK visitor visa from Nigeria].
1. Give me a checklist of documents and steps, marking anything you're unsure is still current.
2. List the official websites where I should verify each item.
3. Give me a timeline working back from [date].
Be clear about what might have changed since your information was last updated.""",
 "Never pay an agent or website just because an AI mentioned it. Use only official channels for government processes.",
 ['limits','halluc'])

L(53,11,'Personal Finance & Budgeting with AI','Claude / ChatGPT + Google Sheets',
 'Build a monthly budget and savings plan with AI, without sharing sensitive account details.',
 'Clarity on where your money goes',
 [S('List your income and spending categories with rough monthly amounts. No account numbers, no bank logins.'),
  S('Ask the AI to organise it into a budget, spot patterns and suggest realistic savings.'),
  H('Ask for a Google Sheets budget template with formulas, then fill it in privately yourself.'),
  S('Ask it to explain any financial term you don\'t understand (inflation, interest, treasury bills…).'),
  W('AI is not a financial adviser. For investments, loans or big decisions, speak to a licensed professional. Be very wary of anyone using "AI trading" to promise returns.'),
  C('Budget organised','Spreadsheet template with formulas','One savings action chosen')],
 "AI is a patient, judgement-free helper for personal finance basics: organising numbers, explaining terms, building templates. It isn't licensed, doesn't know your full situation and can't give regulated financial advice. Use it to understand and organise, and use professionals for decisions. Privacy matters most here. Never paste account numbers, PINs or passwords into any AI tool.",
 """Help me build a monthly budget. Rough figures (no account details):
Income: [amounts]. Spending: [category: amount, …]. Goal: [e.g. save ₦50,000/month].
1. Organise this into a clear budget table.
2. Show where my money mostly goes.
3. Suggest 3 realistic changes to reach my goal.
4. Give me a Google Sheets template with formulas for tracking it monthly.""",
 "Any \"AI investment\" scheme promising guaranteed returns is almost certainly a scam.",
 ['fluency'])

L(54,11,'Health, Fitness & Meals: Useful and Safe','Claude / ChatGPT / Gemini',
 'Create a weekly meal plan and simple fitness routine, and learn when AI health information needs a professional.',
 'Healthier routines, planned in minutes',
 [S('Ask for a weekly meal plan using local, affordable ingredients, with a shopping list and budget.'),
  S('Ask for a simple home workout routine that matches your fitness level and time.'),
  H('Good uses: planning, recipes, explaining what a doctor told you in simpler words, preparing questions for your appointment.'),
  W('AI is not a doctor. For symptoms, medication, pregnancy, children\'s health or any serious concern, see a qualified health professional. Never change medication because of an AI answer.'),
  C('Weekly meal plan with shopping list','Simple fitness routine','Wrote down questions for your next doctor visit')],
 "Health is a high-stakes area where AI can help with planning and understanding, but must not replace professional care. Anthropic builds its models to be helpful with health information and to point people to professionals when it matters. You need the same judgement: AI for organising and explaining, professionals for diagnosing and treating.",
 """Create a 7-day meal plan for [number] people using affordable Nigerian ingredients, budget about ₦[amount] for the week.
Preferences/needs: [e.g. less sugar, vegetarian, kids].
Include a shopping list grouped by market section and simple prep tips for busy weekdays.
(If any need above is medical, remind me to check the plan with a health professional.)""",
 "If you have a health condition, check any diet or exercise plan with your doctor before starting.",
 ['character'])

L(55,11,'Languages, Translation & Voice','Google Translate / Claude / ChatGPT voice mode',
 'Use AI to translate, practise a language by voice and communicate across languages.',
 'Talk to more people, in more languages',
 [S('Translate one message into Yoruba, Hausa, Igbo, Pidgin, French or another language, then ask the AI to translate it back to English to check the meaning survived.'),
  S('Try voice mode in the ChatGPT, Gemini or Claude app: hold a 5-minute spoken conversation to practise a language or rehearse a presentation.'),
  H('AI translation is strong for major languages and weaker for Nigerian languages and dialects. For anything important (contracts, signs, public messages), have a native speaker check.'),
  C('Translated and back-translated one message','5-minute voice conversation','Native speaker checked anything important')],
 "Voice mode turns AI into a conversation partner you can talk to while walking or driving, ideal for language practice and rehearsing. Translation quality depends on how much of that language the model saw during training. That's why it's excellent for French and weaker for Ijaw, a direct example of the knowledge limits you learnt about in Week 1.",
 """Translate this message into [language], keeping the tone [polite / casual / formal]:
"[your message]"
Then translate your version back into English word for word, so I can check nothing changed.
Tell me how confident you are in this translation and anything a native speaker might phrase differently.""",
 "For legal, medical or official documents, use a certified human translator.",
 ['limits'])

# ================= WEEK 12 · Capstone =================
L(56,12,'Your Personal AI Operating System','Claude Projects / ChatGPT Projects + custom instructions',
 'Set up your AI tools so they already know you: profile, preferences, projects and your best prompts.',
 'AI that works like a trained assistant, not a stranger',
 [S('Write your custom instructions or preferences: who you are, your work, how you like answers (length, tone, language, Naira).'),
  S('Create 2–3 Projects (e.g. "My business", "Learning", "Personal admin") with relevant files and standing instructions in each.'),
  S('Move your best prompts from this course into a prompt library document. Group them by task.'),
  H('Memory and personalisation features save you re-explaining yourself, but check what the AI remembers. You can usually view and delete memories in settings.'),
  C('Custom instructions written','2–3 Projects set up','Prompt library organised')],
 "Most people use AI as a blank chat every time, which means re-explaining their context again and again. Setting up preferences, projects and saved prompts turns a general assistant into one that knows your work. This is the habit that separates casual users from experts. Anthropic's help centre explains how preferences, Projects and memory work in Claude, and other assistants have similar features.",
 """Help me write my AI custom instructions (under 200 words):
About me: [role, business/employer, location, main tasks].
How I like answers: [length, tone, British/American English, Naira, bullet points or prose].
Always: [e.g. ask before assuming, flag uncertainty].
Never: [e.g. invent statistics, use American spellings].
Then suggest 3 Projects I should set up and what files and instructions to put in each.""",
 "Don't put passwords, ID numbers or other people's private data in instructions or memory.",
 ['personal','projects','skills'])

L(57,12,'AI Agents: Delegating Multi-Step Work','Claude Cowork / ChatGPT agent / Gemini',
 'Give an AI agent one multi-step task (research and compile, organise files, draft and format a report) and supervise it.',
 'You can delegate whole tasks, not just questions',
 [S('Understand the difference: a chat answers; an <strong>agent</strong> plans steps, uses tools (web, files, apps) and works until the task is done.'),
  S('Choose a safe, low-risk task, e.g. "research 10 suppliers of X in Lagos and put their public details in a spreadsheet".'),
  H('Brief it like you\'d brief a capable new assistant: the goal, the context, what "done" looks like, and what it must not do (pay, send, delete, sign up).'),
  S('Watch what it does, check the output carefully and note where it needed correcting.'),
  W('Don\'t give agents access to your bank, email sending or anything irreversible until you understand and trust them. Approve important actions yourself.'),
  C('Understood agents vs chat','Briefed an agent on a low-risk task','Checked the output and noted corrections')],
 "Agents are the biggest shift in AI right now. Instead of answering one question, they carry out a task over many steps, which Anthropic's AI Fluency course calls Agency. Anthropic's own advice on agents is to give clear goals and boundaries, keep humans in charge of risky actions and check the results. The 4Ds matter even more here: delegate wisely, describe precisely, check carefully and stay responsible.",
 """Task brief for an AI agent:
Goal: [what you want done].
Context: [why, for whom, any useful background].
Done looks like: [exact output: e.g. a spreadsheet with columns A, B, C for 10 items].
Rules: use only public information; do NOT make purchases, send messages, sign up for anything or delete files; ask me before any action that can't be undone.
When finished, summarise what you did and anything you were unsure about.""",
 "An agent working for 20 minutes can make 20 minutes of mistakes. Check its work as you would a new hire's.",
 ['fluency','agents','cowork','teams'])

L(58,12,'Your AI Rules: Privacy, Safety & Honesty','Reflection + Claude',
 'Write your personal (or team) AI use policy: what you use AI for, what you check, what you never share.',
 'Confidence that you use AI well and safely',
 [S('List the ways you now use AI at work and at home.'),
  S('For each, note what could go wrong: wrong facts, leaked data, unfair or biased output, over-reliance.'),
  H('A good policy covers: approved tools, data you never paste, what always gets human review, when you tell people AI was used, and who to ask when unsure.'),
  S('If you\'re in a workplace, check your employer\'s AI policy and make sure yours fits within it.'),
  C('Uses and risks listed','One-page AI policy written','Checked against your workplace rules')],
 "This is Diligence, the 4th D: taking responsibility for how you use AI and what you produce with it. Being honest with customers and colleagues about AI use, protecting other people's data and checking outputs are what make AI use trustworthy, for you and for the people affected by your work.",
 """Help me write a one-page AI use policy for [me personally / my team at X].
Sections: tools we use and for what; information we never put into AI tools; what must always be checked by a person; when we tell others AI was used; how we handle mistakes.
Make it practical and short. Rules people will actually follow.""",
 "A policy nobody reads is useless. Keep it to one page and revisit it every 6 months as tools change.",
 ['fluency','character'])

L(59,12,'Capstone Build: Your AI Solo-preneur Mini Launch','All course tools',
 'Use your skills to launch one small real thing: an offer, a product, an improved workflow at work or a community project.',
 'Proof you can use AI to create real value',
 [S('Choose your capstone: a small offer for your business, a digital resource, a workflow that saves your team time, or a community project.'),
  S('Plan it with AI: goal, audience, steps, assets needed, timeline (this week).'),
  S('Build the assets with the tools you\'ve learnt: content, visuals, a page or form, an automation.'),
  H('Keep it small enough to finish this week. A small finished launch beats a big unfinished plan.'),
  S('Launch it, even to just 10 people.'),
  C('Capstone chosen and planned','Assets created','Launched to real people')],
 "Your capstone brings all the course skills together: Description (briefing AI clearly), Discernment (checking quality), Delegation (choosing what AI does) and Diligence (owning the outcome). The goal isn't perfection. It's proof that you can turn an idea into something real with AI as your team.",
 """My capstone: [describe the idea]. Audience: [who]. Goal: [measurable result].
Act as my project manager:
1. Break this into tasks for the next 5 days (30-60 minutes each).
2. For each task: which AI tool to use and a starter prompt.
3. List what could go wrong and how to prevent it.
4. Define how I'll measure success by day 7.""",
 "Don't wait until it's perfect. Launch, learn and improve. That's how AI-native work gets done.",
 ['fluency','chain'])

L(60,12,'Present, Reflect & Plan Your Next 90 Days','Gamma / Canva + Claude',
 'Create a short presentation of your capstone and course journey, and a plan for the next 90 days.',
 'Course complete: you are an AI Expert User 🏆',
 [S('Make a 6-slide presentation: where you started, what you learnt, your capstone, results, what\'s next.'),
  S('Present it to someone: a colleague, family, your cohort, or record a short video.'),
  S('Write your next-90-days plan: 3 skills to deepen, 1 project, and how you\'ll keep up with new tools.'),
  H('To keep learning for free, try Anthropic\'s Claude Academy courses, especially AI Fluency and AI capabilities and limitations. They go deeper into the thinking behind what you\'ve practised.'),
  C('6-slide presentation made','Presented or recorded','Next-90-days plan written')],
 "Twelve weeks ago you learnt to write a clear prompt. Now you use AI for writing, design, research, data, automation, video, learning and life admin, and you know its limits. Tools will keep changing every few months. The skills you've built won't go out of date: clear description, careful checking, wise delegation and responsible use. Keep practising them with every new tool.",
 """Here's my journey through the course: [what I could do before, what I can do now, my capstone, results].
1. Create a 6-slide presentation outline (title + 2 bullets per slide).
2. Write a 2-minute spoken script to go with it.
3. Draft my next-90-days AI learning plan: 3 skills to deepen, 1 project, and a weekly habit to stay current.""",
 "Keep your prompt library alive. Add to it every week, and it will keep paying you back.",
 ['fluency','limits','claude101'])

# Expert-specific outcomes for the shared Weeks 1-4 (replaces the income milestones shown to Mastery to Money)
EXPERT_INC = {
 1:'Your first useful prompt, on a real task', 2:'Research you can check, with sources', 3:'A post or letter in your own voice',
 4:'Hours of reading cut to minutes', 5:'One real problem solved in 30 minutes', 6:'Images for posts and flyers',
 7:'Cleaner product and profile photos', 8:'A designed post without a designer', 9:'Logo ideas to brief a designer',
 10:'A finished visual with a tagline', 11:'Notes, plans and files in one place', 12:'Slides in minutes, not hours',
 13:'A prioritised week', 14:'Meeting notes and action items, done', 15:'Two hours of work done in 30 minutes',
 16:'Voiceovers without a studio', 17:'A talking-head welcome video', 18:'A jingle for your brand',
 19:'Captions and clean audio', 20:'A full content pack for a business',
}
