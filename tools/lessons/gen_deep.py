# "Understand it" layer for Days 1-90 (Days 1-20 shared by both programmes; 21-90 = Mastery to Money).
# idea = plain-language explanation; prompt = copyable prompt; watch = common mistake; src = keys into SRC.
D = {}
def add(d, idea, prompt, watch, src): D[d] = {'idea': idea, 'prompt': prompt, 'watch': watch, 'src': src}

# ---------- WEEK 1 · Text AI ----------
add(1,
"A chatbot like ChatGPT, Gemini or Claude has read a huge amount of text and learnt to predict what words should come next. It does not know you, your customers or your city unless you tell it. That is why a short, vague request gets a generic answer. Anthropic suggests a simple test: picture a brilliant new employee on their first day. They are clever but know nothing about your business. Whatever you would explain to them, explain to the AI. That covers who it is helping, the situation, what you want and why you want it. A role (\"You are a Nigerian business writer\") helps, but the context and the reason do most of the work.",
"""You are an experienced business writer who knows the Nigerian market.

My situation: I run [your business] in [city]. My customers are mostly [who they are].
What I need: a short follow-up message to a customer who asked for a price two days ago but has not replied.
Why it matters: I don't want to sound desperate, but I don't want to lose the sale.

Write 3 versions: one warm, one direct, one with a small time-limited offer. Keep each under 60 words.""",
"Don't judge AI by one try. If the first answer is weak, the fix is usually more context, not a new tool. Tell it what was wrong and ask again.",
['clear','fluency','claude101'])

add(2,
"Chatbots answer from what they learnt during training, which stops at a cut-off date. They can also produce something that sounds right but isn't, because they are predicting likely words, not looking facts up. Research tools like Perplexity, and the web-search modes in Claude, ChatGPT and Gemini, first search the web and then write an answer with numbered sources. The rule is simple. When the answer depends on facts, prices, dates, laws or news, use a tool that searches and open at least one source yourself. Anthropic calls this skill Discernment: judging whether an output deserves your trust.",
"""Search the web and answer: [your question, e.g. "What are the current CAC requirements to register a business name in Nigeria?"]

Rules:
- Use only sources from the last 12 months where possible.
- Put a numbered citation after every factual claim.
- If sources disagree or you are unsure, say so plainly instead of guessing.
- End with "What I should double-check myself".""",
"A citation is not proof. Open the link. Sometimes the source says something different, or is a blog quoting another blog.",
['limits','halluc','fluency'])

add(3,
"Writing is where AI saves most people the most time, because almost every job involves emails, posts, reports and proposals. The skill is not \"make the AI write for me\". It is directing the writing like an editor would. Two techniques from Anthropic's guide work very well here. First, give an example of the tone you want, such as a post you wrote before that you liked. Examples steer style better than adjectives like \"professional\" or \"fun\". Second, give feedback in rounds. Ask for a draft, say what to keep and what to change, then ask again.",
"""Here is a LinkedIn post I wrote before that sounds like me:
<example>
[paste a post, email or message you wrote that you liked]
</example>

Write a new post in the same voice about: [topic].
Audience: [who will read it]. Goal: [what you want them to do after reading].
Length: under 200 words. No hashtags in the body; add 3 at the end.""",
"AI-written text has tell-tale habits: \"In today's fast-paced world\", too many dashes, lists of three, a big dramatic closing line. Ask it to remove them, or edit them out yourself. Your readers notice.",
['examples','best'])

add(4,
"Modern AI tools can read a long PDF, a contract or a 60-page report in seconds. What the AI can hold and work with at once is called its context window, and you can think of it as its working memory. Two tips from Anthropic help with long documents. Put the document first and your question after it. Then ask the AI to quote the exact sentences it is relying on before it summarises. Quotes make it much easier to spot when the AI has filled a gap with a guess.",
"""I've attached [document name]. Read it fully first.

1. List the 5 most important points. For each, quote the exact sentence from the document that supports it.
2. Explain each point in plain English, as if to a smart 12-year-old.
3. Give me 3 actions I can take this week based on it.
If something I'd expect is NOT in the document, tell me rather than filling the gap.""",
"Very long documents can lose detail in the middle. For anything important (contracts, policies, figures), ask about specific sections and check the quotes against the original.",
['longdoc','limits'])

add(5,
"This week you have practised the core loop of working with AI. Decide what to hand over, describe it clearly, check what comes back and take responsibility for the result. Anthropic's AI Fluency course calls these the 4Ds: Delegation, Description, Discernment and Diligence. Delegation is the first and most overlooked one. Not every task should go to AI. Hand over first drafts, summaries, idea lists and reformatting. Keep the judgement calls, relationships and final decisions for yourself.",
"""I want to solve this problem today: [describe your real problem].

Before doing anything, help me plan:
1. Break this into steps.
2. For each step, tell me whether AI should do it, help me do it, or whether I should do it myself, and why.
3. Then let's start with the first AI step.""",
"Saving time is only half the win. Check the output before it goes to a customer or boss. Your name is on it, not the AI's.",
['fluency','econ'])

# ---------- WEEK 2 · Image AI ----------
add(6,
"Image generators learnt from millions of pictures paired with descriptions, so they turn words into visuals. They respond best to what a photographer or art director would say. Describe the subject, the setting, the lighting, the camera angle, the style and the mood. \"A shop\" gives you something random. \"A small Lagos fashion boutique at golden hour, shot from the doorway, warm light, Ankara fabrics on display, photo-realistic\" gives you something usable. Newer tools like Ideogram and the image features in ChatGPT and Gemini handle text inside images far better than older ones did.",
"""A [subject] in [setting], [time of day / lighting], shot from [angle, e.g. eye level / above / close-up], [style: photo-realistic / flat illustration / 3D render], [mood: warm / premium / playful], colour palette of [colours]. Leave empty space at the top for a headline. Aspect ratio 4:5 for Instagram.""",
"Look closely at hands, faces and any text before you use an image. And never pass off an AI image as a real photo of your actual product. Customers feel misled, and on some platforms it breaks the rules.",
['best','fluency'])

add(7,
"Generative fill lets you select part of a photo and describe what should be there: remove a stranger in the background, extend a cropped image, replace a messy table with a clean one. The AI is not copying from a stock library. It paints new pixels that match the light and texture around them. That makes it ideal for tidying real product photos while keeping the product itself honest.",
"""(For Canva Magic Edit / Firefly Generative Fill, select the area, then type:)
"Plain light-grey studio background, soft shadow under the product, nothing else"

(To ask a chat assistant for help first:)
I sell [product] and my photos are taken on my phone at home. Give me a 5-step routine to get clean, consistent product photos using my phone and an AI editing tool.""",
"Don't edit the product itself (colour, size, finish) in a way that misrepresents what the customer will receive. That leads to refunds and bad reviews.",
['fluency'])

add(8,
"Canva's AI features (Magic Design, Magic Write, Magic Edit) let non-designers start from a description instead of a blank page. The AI gives you a layout. Your job is the design judgement: is the message clear in two seconds, does it look like your brand, and can people read it on a phone? A designer's three checks still apply: one main message, strong contrast and plenty of empty space.",
"""I'm designing an Instagram post for [business]. Goal: [e.g. announce our Saturday promo].
Give me:
- 3 headline options under 7 words each
- 1 line of supporting text
- a clear call to action
- suggested colours and font style that fit a [premium / friendly / bold] brand
Then tell me what to put in the Canva Magic Design prompt.""",
"Templates are shared by millions. Change the colours, fonts and layout enough that your post doesn't look like everyone else's.",
['clear'])

add(9,
"AI is excellent at exploring many logo directions quickly: wordmarks, icons, colour schemes. It is weaker at producing a final, clean logo file you can trademark and print at any size. Use AI for exploration and a mood board, then refine the chosen direction in a vector tool, or hand it to a designer with a much clearer brief. That split saves time and money.",
"""Act as a brand strategist. My brand: [name], selling [what] to [who] in [where]. Personality: [3 words].
1. Suggest 5 different logo directions (e.g. wordmark, icon, monogram), each with a one-line rationale.
2. For each, write an image-generation prompt I can paste into Ideogram.
3. Recommend 2 colour palettes with hex codes and explain why they suit this audience.""",
"Check that your favourite concept is not too close to an existing brand. AI can echo famous logos without meaning to.",
['examples'])

add(10,
"Combining tools is where AI gets powerful. One tool writes, another designs, another edits. This is the first time you chain them on purpose: the output of one step becomes the input of the next. Anthropic's guide calls this prompt chaining. Breaking a big job into clear steps gives better results than one giant request, and you can check each step before moving on.",
"""Step 1. Help me write a movie poster for my life story. Ask me 5 quick questions about my journey, then give me 5 title options and 5 taglines.

(After you answer and choose:)
Step 2. Now write an image-generation prompt for the poster: style, lighting, composition, where the title goes. Make it cinematic.""",
"Keep a copy of each step's output. If the final result goes wrong, you can go back one step instead of starting from zero.",
['chain'])

# ---------- WEEK 3 · Productivity ----------
add(11,
"A second brain is one place where your notes, plans and ideas live, with AI built in to search, summarise and draft from them. The same idea now exists inside the chat assistants. Claude Projects (and similar features in ChatGPT and Gemini) let you upload your key files and write standing instructions once. After that, every chat in the project already knows your business, your prices and your tone, so you stop re-explaining yourself.",
"""Standing instructions for my [business / job] project:

About me: [role, business, location, customers].
How I like answers: short, practical, British English, Naira prices.
Always: ask a clarifying question if my request is vague.
Never: invent prices, laws or statistics. Say "check this" instead.

Files attached: [price list / brand guide / FAQs / past proposals].""",
"Don't upload anything you are not allowed to share, such as client contracts, staff records or customer phone numbers, unless your workplace approves the tool.",
['projects','personal'])

add(12,
"AI slide tools (Gamma, Canva Docs-to-Deck, and the slide features in Claude and ChatGPT) build a whole deck from an outline. The quality of the deck depends almost entirely on the outline you give. Decide your audience and the one decision you want them to make, then build the slides around that. Let the AI handle layout and visuals. You own the story.",
"""I'm presenting to [audience] for [minutes] minutes. The decision I want from them: [e.g. approve the budget].
Create an 8-slide outline:
- slide title (a full sentence that states the point, not a label)
- 2-3 bullet points
- a suggestion for a visual or chart
End with a slide that asks for the decision clearly.""",
"Check every number and claim the AI adds to your slides. Decks are where made-up statistics most often slip through.",
['artifacts','clear'])

add(13,
"Planning is a great task to share with AI, because the hard part is often getting everything out of your head. You do the brain dump. The AI sorts it with a framework like the Eisenhower Matrix (urgent vs important). You make the final call, because only you know which client is really angry or which deadline is actually soft.",
"""Here is everything on my mind this week, in no order:
[brain dump. Don't tidy it.]

1. Sort these into an Eisenhower Matrix (urgent and important, important not urgent, urgent not important, neither).
2. Suggest what to do today, what to schedule, what to delegate and what to drop.
3. Ask me about anything where you'd need more context to decide.""",
"AI doesn't know your real priorities, politics or energy levels. Treat its plan as a first draft.",
['fluency'])

add(14,
"Transcription tools turn speech into text, and AI then turns that text into summaries, decisions and to-do lists. The skill is asking for the right output: not just \"summarise\" but \"who agreed to do what, by when\". Always tell people when you're recording. In many places it is a legal requirement, and it is basic respect.",
"""Here is a meeting transcript:
<transcript>
[paste]
</transcript>

Give me:
1. A 5-line summary
2. Decisions made
3. Action items as a table: task | owner | deadline
4. Open questions nobody answered
Only use what's in the transcript. If an owner or deadline wasn't stated, write "not stated".""",
"Transcripts mishear names, numbers and Nigerian accents. Check names and figures before you send minutes.",
['xml','halluc'])

add(15,
"This challenge tests the full loop: decide what to delegate, describe it well, check the output, own the result. Speed comes from reusing what worked. By now you should have a few prompts you trust, so start from those instead of typing from scratch. Professionals who are good with AI are not faster typists. They have a library of proven prompts and know which tool fits which job.",
"""I have a task that normally takes me 2 hours: [describe it].
Help me do it in 30 minutes:
1. Break it into steps and estimate minutes for each.
2. Tell me which steps AI can draft and which I must do.
3. Let's start step 1 now. Ask me only the questions you truly need answered.""",
"Fast and wrong is worse than slow and right. Keep 5 minutes at the end for checking.",
['chain','fluency'])

# ---------- WEEK 4 · Audio & Video ----------
add(16,
"Text-to-speech tools like ElevenLabs now sound close to human, with breathing, emphasis and different accents. They read exactly what you write, so write for the ear. Use short sentences, spell numbers the way they should be said and add commas where you want a pause. Then listen once and fix anything that sounds robotic.",
"""Rewrite this text so it sounds natural when read aloud by a voice tool:
- short sentences, max 15 words
- numbers written how they should be spoken (e.g. "twenty-five thousand naira")
- add commas for natural pauses
- remove anything that only works on paper (bullets, brackets, URLs)
Text: [paste]""",
"Never clone someone's voice without their clear permission, including your own staff or celebrities. Voice cloning scams are rising, and it can be illegal.",
['clear'])

add(17,
"Avatar tools like HeyGen animate a photo or a recorded presenter to speak any script, and even translate it into other languages with lip-sync. That is powerful for training videos, product explainers and multilingual messages. Viewers trust a face, so be honest about it. Disclose that a video uses an AI avatar, especially in ads.",
"""Write a 40-second welcome video script for [business], spoken by an AI avatar.
- Hook in the first 5 seconds
- 3 short sentences on what we do and who for
- one clear next step
- warm, confident tone; no jargon
Also give a version in [Yoruba / Hausa / Igbo / Pidgin / French] for subtitles.""",
"Always disclose AI avatars in adverts and never use a real person's face without consent.",
['fluency'])

add(18,
"Music tools like Suno create songs from a description of genre, mood, instruments and lyrics. They are useful for jingles, background tracks and content intros. Before using AI music commercially, check the tool's licence for your plan. Paid plans usually grant commercial rights; free ones often do not.",
"""Write lyrics for a 30-second jingle for [brand], which sells [what].
- catchy 2-line chorus with the brand name
- style: [Afrobeats / highlife / gospel / jazz]
- mood: [upbeat / premium]
Then write the music-style description I should paste into Suno (genre, tempo, instruments, vocal type).""",
"Don't prompt for \"in the style of [famous artist]\" for commercial use. It creates legal risk, and many tools block it anyway.",
['fluency'])

add(19,
"AI video editors like CapCut and Descript can add captions automatically, remove background noise, cut filler words and even edit video by editing the transcript. Most people watch social video with the sound off, so captions alone can double how much of your video gets watched. Let the AI do the tedious part, then spend your time on the hook and the pacing.",
"""Here is the transcript of my video:
[paste]
1. Suggest the strongest 3-second hook from what I said.
2. Mark sections I can cut without losing meaning.
3. Write a caption for the post (under 150 characters) plus 5 relevant hashtags.""",
"Auto-captions often misspell names, places and Pidgin. Check them before you post; mistakes look careless.",
['clear'])

add(20,
"Your capstone combines writing, images, audio and video, which is a real job businesses pay for. The best results come from a short creative brief before you open any tool: who the audience is, the one message, the tone and the call to action. A brief keeps every asset consistent. It is the same principle as everything this month: clear description in, better work out.",
"""Act as a creative director. Write a one-page creative brief for a campaign for [fictional Nigerian business].
Include: audience, single key message, tone, call to action, 3 assets to create (post, 30s video, voiceover), and a checklist to make them consistent (colours, fonts, words to use and avoid).""",
"Consistency beats cleverness. Check that all assets use the same name, price, colours and call to action before you call it finished.",
['fluency','examples'])

# ---------- WEEK 5 · Advanced prompting (M2M) ----------
add(21,
"A prompt library is a set of tested prompts with blanks you fill in. It is the most valuable asset you build in this course, because good prompts are reusable. Anthropic's guide recommends structuring longer prompts into clear parts: instructions, context, examples and the input to work on, each wrapped in labelled tags like <context> and </context>. Tags stop the AI mixing up your instructions with the material it is working on.",
"""<role>You are a [role].</role>
<context>[about the business, audience, situation]</context>
<instructions>
1. [what to do]
2. [format and length]
3. [what to avoid]
</instructions>
<example>[a past output you liked]</example>
<input>[the material to work on]</input>""",
"A template only stays good if you update it. When a prompt fails, note why and fix the template, not just that one chat.",
['xml','examples','pe'])

add(22,
"There are thousands of AI tools, but most fall into a few categories: general assistants (Claude, ChatGPT, Gemini), research, image, video, audio, automation and app builders. The general assistants now do much of what single-purpose tools used to: writing, images, data analysis, documents. Map tools by the job they do, and before paying for a specialist tool, check whether your main assistant can already do it.",
"""Build me a table of AI tools by category for someone who [sells AI services / runs a small business].
Columns: category | best general-assistant option | specialist tool worth paying for | what the specialist does better | free tier? (yes/no)
Only include tools you are confident exist. Mark anything uncertain with "(check)".""",
"Tool lists go out of date fast. Check prices and features on the tool's own website before you recommend it to a client.",
['econ','limits'])

add(23,
"RISEN (Role, Instructions, Steps, End goal, Narrowing) is one handy checklist for business prompts. What matters more is the principle behind it. Anthropic's guide says to explain why a rule exists, not just state it. \"Keep it short because clients read on their phones\" works better than \"keep it short\", because the AI can apply the reason to situations you didn't list. Also say what to do instead of what not to do. \"Write in plain sentences\" beats \"don't use bullet points\".",
"""<role>You are a proposal writer for a small Nigerian [type] business.</role>
<instructions>Write a proposal for [service] for [client type].</instructions>
<steps>Executive summary → their problem → our solution → timeline → price → next step.</steps>
<goal>A signed agreement within 5 days. That's why the next step must be easy and specific.</goal>
<narrowing>Plain English, under 400 words, because the client is not technical and will read this on a phone.</narrowing>""",
"Over-long prompts packed with rules can backfire. If the AI ignores something, ask whether the instruction was clear and important, or just noise.",
['clear','xml','role'])

add(24,
"AI can be confidently wrong. That is called hallucination, and it happens because the model predicts plausible text rather than checking facts. It is most likely with names, numbers, quotes, legal or medical details and anything recent or niche. Three habits reduce the risk: let the AI say \"I don't know\", ask it to cite or quote its sources, and verify anything you will act on. Your personal AI policy is your Diligence, the 4th D. It covers what you will and won't use AI for, what you'll disclose, and what you'll always check yourself.",
"""Help me write a one-page personal AI policy for my work as a [role].
Sections:
1. Tasks I'll use AI for
2. Tasks I won't use AI for (and why)
3. What I always verify before sharing
4. What I tell clients about my AI use
5. Data I never paste into AI tools
Keep it practical: things I can actually follow.""",
"The more an answer flatters you or agrees with you, the more carefully you should check it. AI models can lean towards telling you what you want to hear.",
['halluc','fluency','character','limits'])

add(25,
"A personal brand is how people describe you when you're not in the room. AI helps you write a consistent bio, headline and content themes, but they must come from your real story. Feed it your actual experience, wins and opinions. The AI is good at structure and polish. It cannot invent credibility you don't have.",
"""Interview me to build my personal brand. Ask me 8 questions one at a time about my experience, results, values and who I want to serve.
After my answers, write:
- a one-line headline
- a 3-sentence bio
- 3 content pillars with 5 post ideas each
- 5 words that describe my tone""",
"Don't let AI exaggerate your experience. Overclaiming is the fastest way to lose a client's trust.",
['personal','examples'])

# ---------- WEEK 6 · Outreach & proposals ----------
add(26,
"AI makes it easy to send 100 generic messages, and that is exactly why generic messages now get ignored. The winning approach is AI-assisted research plus genuine personalisation. Spend 3 minutes learning about each prospect, use AI to draft a message that mentions something specific and useful to them, then edit it so it sounds like you.",
"""Here's what I know about this prospect:
[name, business, what they post, a problem I noticed]

My service: [what you offer].
Write a 70-word DM that:
- opens with something specific about THEM (not me)
- offers one small, useful idea for free
- ends with a low-pressure question
Give me 2 versions.""",
"Never scrape or buy contact lists and blast them. It damages your reputation and can break data-protection law (NDPA in Nigeria).",
['examples'])

add(27,
"A proposal persuades someone to say yes. The AI can structure and polish it, but the persuasion comes from understanding the client's problem in their own words. Feed it the notes from your conversation, not just the service name. Ask the AI to critique your proposal as a sceptical client would. That is one of the best uses of AI there is.",
"""Here are my notes from talking to the client: [paste].
Write a proposal using their own words for the problem.
Then switch roles: you are the client's sceptical finance manager. List the 5 objections you'd raise and how I should answer each.""",
"Don't send a proposal with figures or timelines the AI suggested that you haven't checked you can deliver.",
['role','chain'])

add(28,
"Pricing is a judgement call, but AI is a great thinking partner for it. It can model packages, compare value-based vs hourly pricing and stress-test your numbers. Give it your real costs and time, then ask it to argue against your price as well as for it.",
"""My service: [what]. Time per job: [hours]. My costs: [tools, data, transport].
My target monthly income: ₦[amount].
1. Calculate the minimum price per job and jobs needed per month.
2. Suggest 3 packages (starter / standard / premium) with what each includes.
3. Argue why my price might be too LOW and too HIGH for [audience].""",
"AI doesn't know current local market rates reliably. Check what real competitors charge before you settle on a price.",
['limits'])

add(29,
"Most deals are won in the follow-up. AI helps you keep track and write timely, polite, varied follow-ups so you are not repeating \"just checking in\". Keep a simple tracker (who, last contact, next step, date) and let AI draft each touch based on what happened last time.",
"""Here's my lead tracker:
[paste: name | what I offered | last contact date | their response]
For each lead, suggest the next step and draft a short follow-up that adds something new (a tip, an example, a deadline), never just "checking in".""",
"Know when to stop. Three polite follow-ups with no reply usually means not now. Move on and try again in a few months.",
['clear'])

add(30,
"Reviewing your progress with AI turns scattered notes into clear lessons. Paste in what you did, what worked and what didn't. Ask for patterns, not praise. Good reflection prompts make the AI an honest coach rather than a cheerleader.",
"""Here's what I did in the last 30 days: [tools learnt, assets made, outreach sent, income earned, what felt hard].
Be an honest coach, not a cheerleader:
1. What patterns do you see in what worked and what didn't?
2. What should I stop, start and continue?
3. Give me a focused plan for the next 30 days with weekly targets.""",
"If the AI only tells you you're doing great, ask it directly for the three weakest points in your plan.",
['character','fluency'])

# ---------- WEEK 7 · Freelancing ----------
add(31,
"Anthropic publishes research on how people actually use AI at work, the Anthropic Economic Index. It shows heavy use for writing, editing, coding, analysis and research help. Those are good signals of where clients already see value. Combine that with what is in demand on Fiverr and Upwork and what you are genuinely good at. The overlap is your niche.",
"""I'm choosing a freelance niche. My skills: [list]. Tools I'm good at: [list]. Industries I know: [list].
1. Suggest 5 specific AI-assisted services at the overlap (e.g. "product photos for Instagram fashion sellers", not "AI design").
2. For each: who pays, typical deliverable, and how I'd find the first 3 clients.
3. Mark which ones I could start this week.""",
"Popular doesn't mean right for you. Pick something you can deliver well and repeatedly without dreading it.",
['econ'])

add(32,
"Packages make buying easy. Instead of \"I do design\", a client sees three clear options with fixed deliverables and prices. Most people pick the middle option, so design that one first and make it your best value. AI is useful here for writing clear package descriptions and spotting gaps in what you've included.",
"""Turn my service into 3 packages: [service].
For each: name, price in ₦, exactly what's included (numbers, not adjectives), delivery time, revisions included.
Make the middle package the best value. Then list questions a client might still have after reading them.""",
"Vague package wording (\"premium quality\", \"unlimited revisions\") causes disputes. Be specific.",
['clear'])

add(33,
"A portfolio proves you can do the work. Three strong, relevant pieces beat twenty random ones. If you don't have clients yet, create realistic samples for a made-up brand in your niche, and say clearly that they are samples. Use AI to write short case-study captions: problem, what you did, the result.",
"""Write a short case-study caption for this portfolio piece:
Client (or sample brand): [name]. Their problem: [what]. What I made: [what]. Tools: [list]. Result or intended result: [what].
Format: 3 lines, results-focused, no hype.""",
"Label sample work as samples. Presenting made-up work as real client work is dishonest and easy to discover.",
['fluency'])

add(34,
"On Upwork and similar platforms, clients get dozens of proposals that all sound the same, and many are obviously AI-written. Yours stands out by answering the client's specific post, showing one relevant example and asking a smart question. Use AI to analyse the job post and draft, then rewrite the first two lines yourself.",
"""Here's an Upwork job post: [paste].
1. What does this client really care about? What are they worried about?
2. Draft a 120-word proposal that opens with their problem, references one relevant piece of my work ([describe]), and ends with one smart question about the project.
No "Dear Hiring Manager", no "I am excited to apply".""",
"Platforms detect and penalise copy-paste proposals. Every one should clearly be about that job.",
['examples'])

add(35,
"Delivering well turns a one-off client into a repeat client. Write down your process as you work: steps, tools, timing, what went wrong. That document becomes your standard operating procedure. Next time, you, an assistant or an AI workflow can follow it.",
"""I just finished a project. Here are my rough notes: [paste].
Turn this into a reusable checklist with stages: before starting → during → before delivery → after delivery.
Add the quality checks I should never skip.""",
"Don't deliver straight from the AI. Do one full read-through as if you were the client.",
['skills'])

# ---------- WEEK 8 · Clipping ----------
add(36,
"Clipping tools like Opus Clip use AI to find the most engaging moments in a long video, cut them into vertical clips and add captions. The AI scores moments by things like hooks, emotion and topic changes. It makes a good first pass, but human judgement on the best moments is what clients pay for.",
"""Here's the transcript of a 10-minute video: [paste].
Find the 5 strongest 30–60 second moments for TikTok/Reels. For each give: start and end quote, why it works (hook, insight, emotion), and a title under 8 words.""",
"Only clip content you have permission to use. Reposting other people's videos without a licence can get accounts banned.",
['longdoc'])

add(37,
"A brand template (fonts, colours, caption style, logo position) makes every clip instantly recognisable as the client's. Consistency is what turns views into followers. Set it up once in CapCut or Descript and apply it to every clip.",
"""Create a clip style guide for [client/brand]:
caption font and size, colours (hex), caption position, how to highlight key words, intro/outro, logo placement, and 3 rules for hooks.
Keep it to one page I can follow every time.""",
"Check captions on a small phone screen. What looks fine on a laptop is often unreadable on mobile.",
['clear'])

add(38,
"Each platform rewards slightly different things. TikTok favours fast hooks, YouTube Shorts favours searchable titles, LinkedIn favours insight and Instagram favours polish. The same clip often needs a different hook, caption and length for each. AI is great at producing those variations from one master clip.",
"""Here's my clip's transcript and topic: [paste].
Write the hook (first line on screen), caption and hashtags for: TikTok, Instagram Reels, YouTube Shorts and LinkedIn.
Explain in one line why each version suits that platform.""",
"Platform rules change often. Check current length limits and best practices rather than trusting old advice, from AI or from blogs.",
['limits'])

add(39,
"A free demo works because it shows instead of tells. Making 2–3 clips from a business's existing video costs you 20 minutes with AI and gives them something concrete to say yes to. Personalisation is the whole strategy.",
"""I made a free sample clip for [business] from their video [title].
Write a short DM to send with it: what I noticed about their content, the clip link, one sentence on how a weekly clipping service would help, and a low-pressure question.
Under 80 words.""",
"Don't post the demo publicly on their behalf. Send it privately and let them decide.",
['examples'])

add(40,
"Retainers (monthly paid work) give you predictable income and give clients consistent results. The pitch works best after you've delivered something they liked. Frame it around their goal (steady growth, saved time), not your hours.",
"""Write a short retainer proposal for [client] after a successful first project.
Include: what we achieved, the monthly scope (exact numbers), the price in ₦, a 3-month minimum and why it helps them, and an easy yes/no next step.""",
"Define scope tightly (\"12 clips per month\", not \"all the clips you need\") or the retainer will slowly eat your time.",
['clear'])

# ---------- WEEK 9 · Automation ----------
add(41,
"Automation tools like Make.com and Zapier connect apps: when X happens, do Y. Adding AI means one of those steps can read, write or decide, for example \"summarise this enquiry and label it hot, warm or cold\". Anthropic's engineering team gives simple advice for this kind of work: start with the simplest workflow that solves the problem, and add complexity only when you can see it helps.",
"""I want to automate this task: [describe what you do by hand].
1. Write it as a workflow: Trigger → Step 1 → Step 2 → … → Result.
2. Mark which steps are simple app actions and which need AI (and what the AI should do).
3. Suggest the simplest version I could build today in Make.com.""",
"Test with fake data first. An automation with a bug can send the wrong message to hundreds of people in seconds.",
['agents'])

add(42,
"A lead capture workflow (form → CRM → welcome email) is the most requested small-business automation, because missed leads mean missed money. Speed matters: replying in five minutes converts far better than replying the next day. Adding AI to draft a personalised welcome based on what the lead wrote makes it feel human.",
"""In my Make.com scenario, an AI step receives a new form entry: name, business, message.
Write the instruction for that AI step so it:
- classifies the lead as hot / warm / cold with a one-line reason
- drafts a personalised 60-word welcome email that references their message
- outputs as JSON with fields: category, reason, email_subject, email_body""",
"Always include a human checkpoint before AI-written messages go to high-value leads, at least until you trust the workflow.",
['agents','xml'])

add(43,
"Selling automation is about outcomes, not technology. Clients don't buy \"a Make.com scenario\". They buy \"no more missed WhatsApp leads\" or \"invoices that chase themselves\". Name each package after the problem it solves.",
"""Turn these automations into a client-friendly service menu: [list].
For each: a problem-focused name, a one-line promise, what's included, setup price in ₦, optional monthly maintenance.
No technical jargon. A shop owner should understand every word.""",
"Price in ongoing tool costs (Make.com, Zapier and AI API usage) or they'll come out of your profit.",
['clear'])

add(44,
"A free audit gives prospects a quick, personalised map of where they're losing time or money and what you'd automate. It positions you as an advisor, not a seller. AI helps you turn their answers into a neat report in minutes.",
"""Here are a business owner's answers to my audit form: [paste].
Write a one-page audit report: their 3 biggest time-wasters, what each costs them per month (estimate, clearly labelled as an estimate), the automation I'd build for each, and a suggested first step.""",
"Label estimates as estimates. Don't present AI-guessed numbers as facts.",
['halluc'])

add(45,
"A working demo beats any description. Build it for a realistic mock client (a restaurant taking orders, a salon taking bookings), record a 3-minute Loom walkthrough and you have a sales asset you can reuse for every prospect in that niche.",
"""Plan a demo automation for a mock [restaurant / salon / clinic].
Give me: the problem it solves, the workflow steps, test data (5 fake customers), what to show in a 3-minute video, and the one sentence to say at the end to ask for a call.""",
"Never use real customer data in a demo. Generate realistic fake data instead.",
['agents'])

# ---------- WEEK 10 · Chatbots & digital products ----------
add(46,
"A chatbot has two parts. The conversation design (what it should handle, what it should hand to a human) and the brain that understands and answers. Modern chatbots usually use an AI model plus a knowledge base: your FAQs, price list and policies. Design on paper first. A clear map of what the bot should and should not do matters more than the tool.",
"""Help me design a FAQ chatbot for [business].
1. List the 15 questions customers ask most (ask me if unsure).
2. Group them into topics.
3. Mark which the bot should answer, which need a human, and which it must never answer (e.g. refunds, medical advice).
4. Write the bot's greeting and its "I'll connect you to a person" message.""",
"A bot that confidently gives wrong prices or policies is worse than no bot. Always give it a clear way to hand over to a human.",
['agents','role'])

add(47,
"Conversation design is writing for a back-and-forth. Keep messages short, offer clear choices and always plan for what happens when the user types something unexpected. Script the happy path first, then the most likely detours.",
"""Script a 10-step chatbot conversation for [business] booking an appointment.
Show: bot message → expected user reply → next bot message.
Then add: 3 unexpected user replies (an emoji, a question off-topic, "talk to a human") and how the bot handles each.""",
"Test your bot with someone who has never seen it. They'll break it in ways you didn't imagine.",
['clear'])

add(48,
"Connecting an AI model to your bot means writing a system prompt: standing instructions for its role, tone, knowledge and limits. This is where everything you've learnt about prompting pays off. Give the bot your FAQ as reference material, tell it to answer only from that material, and tell it what to do when it doesn't know.",
"""<role>You are the customer assistant for [business] in [city].</role>
<knowledge>[paste FAQs, prices, opening hours, policies]</knowledge>
<rules>
- Answer only from the knowledge above. If the answer isn't there, say you'll connect them to a team member.
- Keep replies under 50 words. Friendly, professional, [English / Pidgin].
- Never promise refunds, discounts or delivery dates not listed above.
</rules>""",
"Watch your API costs. Set spending limits in the AI provider's dashboard before going live.",
['role','xml','halluc'])

add(49,
"Digital products (e-books, templates, prompt packs) are sold once and delivered automatically. AI speeds up drafting, but buyers pay for your specific knowledge and a clear result. Outline first, add your own examples and stories, then use AI to polish. A short, practical guide that solves one problem sells better than a long general one.",
"""I want to write a short e-book: [topic] for [audience].
1. Suggest 5 titles that promise a specific result.
2. Create a 10-chapter outline. Each chapter should end with an action step.
3. For each chapter, ask me one question about my own experience I should include, so the book isn't generic.""",
"Many marketplaces are flooded with low-effort AI e-books. Your own experience and local examples are what make yours worth buying.",
['chain','examples'])

add(50,
"People find products by searching, so your title, description and tags must use the words buyers actually type. AI can suggest keywords and rewrite your listing, but check real search data (eRank, Google Trends) for the final choice.",
"""Rewrite my product listing to be found and bought:
Product: [details]. Audience: [who].
Give: 3 title options under 70 characters, a description that opens with the buyer's problem, 5 bullet benefits, and 10 search keywords. Mark which keywords I should verify with real search data.""",
"Don't stuff keywords. Listings that read badly lose sales even if they rank.",
['limits'])

# ---------- WEEK 11 · Sales sprint ----------
add(51,
"Warm outreach (people who already know you or have engaged with your content) converts much better than cold. This week, AI helps you produce useful content daily and personalise every message. Think of AI as your research assistant and first-draft writer, not a bulk sender.",
"""Here are 5 people who engaged with my posts this month: [name + what they commented/liked].
For each, draft a short, natural DM that continues the conversation and offers something useful. Only mention my service if it clearly fits their need.""",
"Don't pitch in the first message to everyone. Lead with help, and the sales conversations will come.",
['examples'])

add(52,
"A proposal plus a short video walkthrough feels personal and is easier to understand than a PDF alone. Use AI to draft both: the document and the script for your 3-minute video.",
"""Based on this proposal [paste], write a 3-minute video script for me to record on Loom:
- 20-second recap of their problem in their words
- walkthrough of the solution
- the price and what's included
- one clear next step
Natural spoken English, not a reading of the document.""",
"Record in a quiet place with good light. Clarity beats production value.",
['chain'])

add(53,
"A discovery call is about understanding, not selling. AI can help you prepare questions and practise. Ask it to role-play a realistic, slightly difficult client and give you feedback afterwards.",
"""Role-play a [type of business owner] in Lagos who is interested in [service] but worried about cost and whether it works.
I'll run a 15-minute discovery call. Stay in character, be realistic (not too easy).
When I type "END", step out of character and give me feedback: what I did well, what I missed, and better questions I could have asked.""",
"Practise out loud, not just in text. Real calls have pauses and interruptions.",
['role'])

add(54,
"An onboarding system makes you look professional and saves hours. Clients know what happens next, and you get everything you need on day one. Map it once, then automate the repetitive parts.",
"""Design a client onboarding process for my [service]:
welcome email, onboarding form questions, kickoff call agenda, shared folder structure, and a timeline of the first 14 days.
Write the welcome email in full.""",
"Ask only for the information you actually need. Long forms delay projects.",
['skills'])

add(55,
"Delivery day is your best marketing moment. A tidy handover with a short explanation of what you did and why shows expertise and invites referrals. AI can help you write the handover note and a simple guide for the client.",
"""Write a delivery message for [client] for [project].
Include: what's delivered (with links), 3 decisions I made and why, how to use or maintain it, and an invitation to give feedback. Warm and professional, under 150 words.""",
"Double-check links and file permissions before sending. A broken link on delivery day looks careless.",
['clear'])

add(56,
"Testimonials sell better than anything you say about yourself. Make it easy for happy clients by asking at the right moment, right after a win, with specific questions. AI can turn their answers into a short testimonial for them to approve.",
"""A client said this about my work: [paste their message or call notes].
Draft a 2–3 sentence testimonial in their voice that mentions the specific result. I'll send it to them to edit and approve.""",
"Never publish a testimonial the client hasn't approved word for word.",
['fluency'])

# ---------- WEEK 12 · Retainers & review ----------
add(57,
"Converting a happy client to a monthly retainer is the fastest way to stable income. Show the results from the first project, propose ongoing work tied to their goals, and make the decision simple.",
"""Help me prepare a retainer conversation with [client].
Results so far: [list]. Their goals for the next 3 months: [list].
Give me: 3 talking points, a proposed monthly scope and price, 3 likely objections with responses, and the exact closing question.""",
"Don't discount just to close. Offer a smaller scope instead of a lower price.",
['role'])

add(58,
"Scaling means more income without working proportionally more hours: higher prices, productised services, retainers and automation. AI can analyse your income data and spot which services earn the most per hour.",
"""Here are my last 60 days of work: [list each job: service, price, hours spent].
1. Calculate my effective hourly rate per service.
2. Which service should I double down on, and which should I drop or reprice?
3. Suggest a price increase plan.""",
"Raise prices for new clients first. Give existing clients notice before changing theirs.",
['chain'])

add(59,
"A portfolio audit ensures your best, most recent work is front and centre. Ask AI to review your portfolio as a potential client would and tell you what's missing.",
"""Act as a busy [type of client] deciding whether to hire me. Here's my portfolio summary: [paste].
In 60 seconds of looking, what convinces you and what makes you hesitate?
List the 3 changes that would most increase your trust.""",
"Remove weak or outdated work. Every piece should be one you'd happily do again.",
['role'])

add(60,
"Your Phase 2 review turns results into a credential. A short, honest deck showing clients served, services delivered and lessons learnt is useful for your own planning and for impressing prospects.",
"""Turn this summary of my last 60 days into a 10-slide review deck outline: [paste numbers, clients, testimonials, lessons].
Each slide: a title that states the point + 2 bullets. Finish with my 3 goals for Phase 3.""",
"Use real numbers only. If something didn't work, say so. Honesty makes the wins believable.",
['artifacts'])

# ---------- WEEK 13 · Production chatbots ----------
add(61,
"A production chatbot must handle real customers reliably. That means testing every path, unexpected inputs and the hand-off to humans. Write test cases before launch, just like a software team would.",
"""Write 20 test messages for my [business] chatbot: 10 normal questions, 5 unusual ones (typos, Pidgin, emojis, two questions at once) and 5 that should trigger a hand-off to a human.
For each, write the ideal bot response so I can compare.""",
"Re-test after every change. Fixing one path can quietly break another.",
['agents','halluc'])

add(62,
"Integrations make a chatbot useful: booking straight into a calendar, adding a lead to a mailing list, notifying staff. Each connection is a point that can fail, so log what happens and set up alerts.",
"""My chatbot needs to: book appointments (Calendly), add leads to Brevo, and alert me on WhatsApp for urgent requests.
List each integration, what data passes between tools, what could go wrong, and how I'd notice if it broke.""",
"Get the client's permission before connecting their business accounts, and store logins securely, not in a chat or a spreadsheet.",
['agents'])

add(63,
"A live demo page turns your skill into something prospects can try. It's far more convincing than screenshots. Keep it simple: one page, one clear explanation, the bot and a contact button.",
"""Write the copy for a one-page site that hosts my chatbot demo:
headline, 2-line explanation, 3 benefits for [type of business], instructions to try the bot, and a call-to-action button text.""",
"Add a short privacy note explaining what the bot stores. It builds trust, and Nigeria's data protection rules expect it.",
['artifacts'])

add(64,
"Three tiers again, now for chatbots. Price based on the business value (bookings gained, staff time saved), not just your build time, and include ongoing maintenance, because bots need updating as prices and policies change.",
"""Help me justify chatbot pricing to a [restaurant/clinic] owner.
Estimate (clearly labelled as estimates) how many enquiries they get, how many are missed, and what each booking is worth.
Then explain my ₦[price] package in terms of what it pays back.""",
"Be careful with ROI promises. Show your assumptions and let the client adjust them.",
['halluc'])

add(65,
"A personalised demo built for a specific business is almost impossible to ignore. With AI it takes 20 minutes. Use their public information (menu, services, hours) to build it, then send the link.",
"""Here's the public info for [business]: [paste menu, services, hours from their page].
Turn it into a FAQ knowledge base for a demo chatbot: 15 Q&As in their tone. Mark anything I should confirm with them.""",
"Only use public information, and tell them it's a demo built from their public page.",
['examples'])

# ---------- WEEK 14 · Agency ----------
add(66,
"An agency niche is a specific type of client you understand deeply. A narrow niche makes marketing easier, because you speak their language and know their problems. Use AI to research the niche, but validate it by talking to real business owners.",
"""Help me define an Ideal Client Profile for an AI services agency focused on [niche] in [city].
Include: business size, owner's goals and frustrations, where they hang out online, budget range, and 5 questions I should ask 5 real owners to validate this.""",
"AI's picture of a niche is a starting hypothesis. Five real conversations beat fifty AI paragraphs.",
['limits'])

add(67,
"All-in-one platforms like GoHighLevel combine CRM, funnels, messaging and booking. They are powerful but complex. Set up only what your niche needs first, and document every setting so you can repeat it for the next client.",
"""I'm setting up GoHighLevel for a [niche] client. List the minimum setup for launch: pipelines, forms, automations, calendar.
For each, write the exact settings as a checklist I can reuse.""",
"Watch the subscription costs. Don't keep paying for a platform before you have clients to put on it.",
['skills'])

add(68,
"A delivery stack is your repeatable system: which tool does which step, in what order, with which prompt. Writing it down as standard operating procedures (SOPs) is what lets you serve more clients without lower quality, and later hand work to an assistant or to AI.",
"""Turn my agency delivery process into an SOP:
[describe how you deliver a typical month of work]
Format: step | tool | prompt or template used | quality check | time.
Highlight steps that could be automated next.""",
"An SOP is only useful if it's followed. Review it with each new client and update it.",
['skills','agents'])

add(69,
"A discovery framework helps you uncover the gap between where a client is and where they want to be. Only then do you propose. AI can help you prepare questions tailored to each prospect and practise handling objections.",
"""Prepare me for a discovery call with [business]. Research notes: [paste].
Give me: 8 open questions to find their current state and desired outcome, the 3 objections they're most likely to raise, and calm responses to each.""",
"Listen more than you talk. If you're explaining your services in the first 10 minutes, you're pitching too early.",
['role'])

add(70,
"A paid pilot lowers the client's risk and gives you a case study. Define success clearly at the start, such as \"20 qualified leads in 30 days\", so converting to full price is a natural next step.",
"""Write a 30-day pilot agreement summary for [client]:
scope, price, what success looks like (measurable), how we'll report progress, and what happens at day 30 if targets are met.""",
"Agree the success measures in writing before you start, so the result isn't open to argument.",
['clear'])

# ---------- WEEK 15 · Micro-SaaS ----------
add(71,
"A micro-SaaS is a small paid software tool that solves one specific problem. The biggest risk is building something nobody wants, so validate before building. AI can help you design interview questions and analyse the answers.",
"""I have an idea: [describe]. Help me validate it.
1. Write 8 interview questions about the problem (not my solution) to ask 10 potential users.
2. Tell me what answers would mean "build it" and what would mean "stop".""",
"Friends saying \"nice idea\" is not validation. Someone offering to pay, or pre-paying, is.",
['limits'])

add(72,
"A one-page spec forces clarity: who it's for, the 3 core features, the first-time user journey and how it makes money. A good spec also makes AI app builders produce far better results, because they're only as clear as your description.",
"""Turn my validated idea into a one-page MVP spec: [idea + interview findings].
Sections: problem, target user, 3 core features only, user journey from sign-up to first value, pricing, success metric.
Then list features I should NOT build yet.""",
"Feature creep kills small products. If a feature isn't in your top 3, write it down for later.",
['clear'])

add(73,
"AI app builders (Lovable, Bolt, Claude Artifacts and others) turn a plain-English description into a working app. You are now the product manager: describe clearly, test everything and give precise feedback. Build in small steps. Get one screen working before asking for the next.",
"""Build a simple web app: [one-sentence description].
Users: [who]. Core features (only these): 1) … 2) … 3) …
Start with just the first screen: [describe what the user sees and can do].
Use a clean, mobile-friendly design. Explain how to test it when you're done.""",
"Don't put real customer data or payments into an AI-built app until someone with technical knowledge has checked its security.",
['artifacts','chain'])

add(74,
"A pricing page should make the decision easy: clear tiers, one recommended option and a simple way to pay. For Nigerian customers, local payment options like Paystack or Flutterwave often convert better than card-only checkouts.",
"""Write pricing page copy for my tool [name], which helps [who] [do what].
3 tiers with names, ₦ prices, what's included and who each is for. Mark the middle as recommended. Add 4 FAQs about payments and cancellation.""",
"Test the full payment flow yourself, including a refund, before launch.",
['clear'])

add(75,
"A beta launch is for learning, not profit. Get 10 real users, watch how they use the product and fix what confuses them. Post where your users already are and lead with helpful content, not ads.",
"""I'm launching a beta of [tool] for [audience]. Suggest 5 places they gather online, then write a helpful post for each that shares something useful and mentions the beta naturally at the end.""",
"Read each community's rules. Many ban self-promotion, and breaking them ruins your reputation there.",
['examples'])

# ---------- WEEK 16 · Commit & launch ----------
add(76,
"After testing several income models, commit to one primary model. Focus compounds. AI can help you compare the evidence: what paid, what you enjoyed, what can grow.",
"""Here's my data from the past 75 days for each model I tried: [income, hours, enjoyment 1–10, client feedback].
Compare them in a table and recommend one primary model, with the honest trade-offs. Then argue for the second-best option, so I'm sure.""",
"Don't choose the model that sounds most impressive. Choose the one with evidence.",
['chain'])

add(77,
"A unique value proposition (UVP) says who you help, what result you deliver and how you're different, in one sentence. AI is great at generating variations. You choose the one that sounds like you and resonates with real clients.",
"""Write 10 variations of my value proposition using: "I help [audience] get [result] in [timeframe] without [pain]".
My details: [audience, result, how you work]. Then rank them by clarity and explain the top pick.""",
"Test your top two UVPs on real prospects. Their reactions matter more than AI's ranking.",
['examples'])

add(78,
"Launching your brand means consistency everywhere: same name, photo, bio and message on every platform. AI can audit your profiles and rewrite them to match.",
"""Here are my current bios on LinkedIn, Instagram and WhatsApp Business: [paste].
Rewrite them so they're consistent with my UVP: [paste], adapted to each platform's length and style.""",
"Use a real photo of yourself for your main profile. People buy from people.",
['personal'])

add(79,
"The content that attracts clients shows your work: before-and-after, how you solved a problem, quick tips. AI helps you turn each project into several posts. Your real results are the ingredient that can't be faked.",
"""I just completed this project: [describe].
Turn it into: 1 LinkedIn post (story format), 1 Instagram carousel outline (6 slides), and 1 short video script (30 seconds). Each should teach something useful, not just show off.""",
"Get client permission before sharing their name or results publicly.",
['examples'])

add(80,
"Outreach at volume still needs quality. A sprint works when each message is researched and personalised. Batch the research, use AI for drafts, and track every reply so you learn what works.",
"""I'm doing a 30-message outreach sprint. Create a tracker template (columns) and a 3-message sequence (day 1, day 4, day 9) for [audience] offering [service]. Each message must reference something specific I'll research about the person.""",
"Space your messages out. Sending dozens at once can get your account flagged as spam.",
['clear'])

# ---------- WEEK 17 · Systems ----------
add(81,
"Every \"no\" or silence carries information about your offer, your audience or your message. AI is good at finding patterns across many responses that are hard to see one by one.",
"""Here are replies and non-replies from my outreach: [paste].
Group the objections, find patterns, and suggest specific changes to my offer and message. Separate "fix the message" issues from "fix the offer" issues.""",
"Look for patterns, not single opinions. One harsh reply is not a trend.",
['chain'])

add(82,
"Automating your own business frees you to do more client work. Start with the tasks you repeat weekly that follow the same steps every time. Those are the best candidates.",
"""List my weekly tasks: [paste]. For each, estimate minutes per week and mark whether it could be automated, assisted by AI or should stay manual.
Recommend the 3 automations that save the most time, with the workflow steps.""",
"Automate a process only after you've done it by hand a few times and know it works.",
['agents'])

add(83,
"Projections turn hopes into numbers you can track. AI can build the spreadsheet formulas and scenarios. You supply realistic assumptions.",
"""Build a 6-month income projection for Google Sheets: retainers (clients × price), one-off projects, product sales.
Give me the column layout and the exact formulas, plus a "worst / expected / best" scenario section. Explain each formula in one line.""",
"Base assumptions on what actually happened in the last 90 days, not on goals.",
['chain'])

add(84,
"An email list is an audience you own. Platforms change their algorithms, but your list stays yours. A short, useful weekly newsletter keeps you in mind for when people are ready to buy.",
"""Plan my first newsletter for [audience]: 5 name ideas, the first issue (intro, one useful AI tip with steps, one resource, a soft mention of my service), and a 4-week topic plan.""",
"Only add people who have agreed to receive it. Adding contacts without consent breaks data-protection law and harms deliverability.",
['examples'])

add(85,
"Accountability keeps you consistent when motivation drops. A weekly check-in with a peer works best. AI can help structure those check-ins so they stay focused and useful.",
"""Create a 20-minute weekly accountability check-in agenda for two people building AI income.
Include: wins, numbers to share, one problem to solve together, commitments for next week, and a simple scoring system.""",
"AI can't replace a real partner who notices when you go quiet. Find a human.",
['teams'])

# ---------- WEEK 18 · Scale & capstone ----------
add(86,
"Your master portfolio is a sales tool. Each case study should show the problem, what you did and the measurable result. AI can help you write tight, results-focused case studies from your notes.",
"""Turn these project notes into 3 portfolio case studies: [paste].
Format each: Client and challenge (2 lines) → What I built (3 bullets) → Result (numbers) → Client quote (if approved).""",
"Numbers must be real and approved by the client. Rounded and honest beats impressive and invented.",
['examples'])

add(87,
"A 30-day content calendar takes daily decisions off your plate. Mix proof (what you built), value (tips), social proof (results) and personality (behind the scenes). AI drafts the plan; you batch-create the content.",
"""Create a 30-day content calendar for an AI services business serving [audience].
Columns: date | platform | post type (proof/value/social proof/personal) | hook | key message | call to action.
Balance: 40% proof, 27% value, 20% social proof, 13% personal.""",
"Leave room for real moments: a client win or an industry update. Don't let a calendar make you robotic.",
['clear'])

add(88,
"SOPs turn your know-how into something others, people or AI, can follow. This is how you grow beyond yourself. Anthropic describes a shift from using AI on your own to working in teams where people and AI agents share the work. Clear written processes are what make that possible.",
"""Write an SOP for [process] so a new assistant (or an AI agent) could follow it without asking me questions.
Include: purpose, trigger, inputs needed, numbered steps, quality checks, what to do if something goes wrong, and tools used.""",
"Test the SOP by giving it to someone else. Every question they ask shows a gap to fill.",
['teams','skills'])

add(89,
"The 90-day review closes the loop: what you set out to do, what happened and what you learnt. An honest review makes your next 90 days far more effective than the first.",
"""Here's my 90-day summary: [income, clients, skills, tools I use daily, biggest lessons, what I'd do differently].
Act as a mentor: identify my 3 strongest assets, my biggest risk, and write a focused 90-day plan with monthly targets.""",
"Celebrate progress, but plan from reality. Next quarter's targets should rest on this quarter's evidence.",
['fluency'])

add(90,
"Your capstone pitch brings everything together: the problem you solve, for whom, your proof and your plan. Presenting it out loud, to your cohort, a mentor or even a mirror, builds the confidence to sell. You started 90 days ago learning to write a prompt. Now you can direct AI to do real work for real clients.",
"""Help me build my capstone pitch deck (10 slides): problem, who I serve, my offer, proof (results and testimonials), how I deliver (tools and process), pricing, 90-day results, next 90-day plan, and the ask.
Then give me a 3-minute spoken script to go with it.""",
"Keep learning. AI tools change every few months, but the skills of clear description, critical checking and taking responsibility don't go out of date.",
['fluency','limits'])
