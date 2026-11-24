import cairosvg, html
BG='#0E0E10'; GOLD='#C9A84C'; CREAM='#F0EDE6'; GREY='#8A877F'; CARD='#17171A'
E=html.escape
def T(x,y,s,size,fill=CREAM,w=400,fam='Inter',anchor='start',ls=0,op=1):
    return f'<text x="{x}" y="{y}" font-family="{fam}" font-weight="{w}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls}" opacity="{op}">{E(s)}</text>'
def H(x,y,lines,size,fill=CREAM,lh=1.08,anchor='start',gold_idx=()):
    return ''.join(T(x,y+i*size*lh,l,size,GOLD if i in gold_idx else fill,800,'Inter Display',anchor) for i,l in enumerate(lines))
def frame(w,h):
    return (f'<rect width="{w}" height="{h}" fill="{BG}"/>'
      f'<defs><radialGradient id="g" cx="0.85" cy="0.1" r="0.8"><stop offset="0" stop-color="{GOLD}" stop-opacity="0.22"/><stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></radialGradient>'
      f'<pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse"><path d="M60 0H0V60" fill="none" stroke="{GOLD}" stroke-opacity="0.07"/></pattern></defs>'
      f'<rect width="{w}" height="{h}" fill="url(#grid)"/><rect width="{w}" height="{h}" fill="url(#g)"/>'
      f'<rect width="{w}" height="8" fill="{GOLD}"/>'
      f'<path d="M50 110v-50h50" fill="none" stroke="{GOLD}" stroke-width="4"/>')
def pill(x,y,label,size=30,fill=GOLD,tc=BG,pad=26):
    wdt=len(label)*size*0.56+pad*2
    return f'<rect x="{x}" y="{y}" width="{wdt}" height="{size*1.9}" rx="{size*0.95}" fill="{fill}"/>'+T(x+pad,y+size*1.3,label,size,tc,700), wdt
def outline_pill(x,y,label,size=28):
    wdt=len(label)*size*0.55+52
    return f'<rect x="{x}" y="{y}" width="{wdt}" height="{size*1.9}" rx="{size*0.95}" fill="none" stroke="{GOLD}" stroke-width="2.5"/>'+T(x+26,y+size*1.3,label,size,CREAM,500), wdt
def pills(x,y,labels,size=28,gap=16):
    out='';cx=x
    for l in labels:
        s,w=outline_pill(cx,y,l,size); out+=s; cx+=w+gap
    return out
def brand(w,h,y=None):
    y=y or h-70
    return (T(60,y,'AI Made Simple',36,GOLD,800,'Inter Display')+T(w-60,y,'aimadesimpleschool.com',28,GREY,500,anchor='end'))
def chat(x,y,w):  # mini AI chat card
    return (f'<rect x="{x}" y="{y}" width="{w}" height="300" rx="28" fill="{CARD}" stroke="{GOLD}" stroke-opacity="0.35"/>'
      +T(x+36,y+56,'● LIVE · lesson preview',24,GOLD,700,'JetBrains Mono')
      +f'<rect x="{x+36}" y="{y+86}" width="{w-200}" height="70" rx="18" fill="#26262B"/>'+T(x+60,y+131,'Write my weekly report from these notes…',26,CREAM)
      +f'<rect x="{x+164}" y="{y+176}" width="{w-200}" height="90" rx="18" fill="{GOLD}" fill-opacity="0.15" stroke="{GOLD}" stroke-opacity="0.5"/>'
      +T(x+188,y+214,'Done. Summary, 3 risks, next steps.',26,CREAM,600)+T(x+188,y+250,'Ready to send ✓',24,GOLD,600))
def save(name,w,h,body):
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{frame(w,h)}{body}</svg>'
    cairosvg.svg2png(bytestring=svg.encode(),write_to=f'out/{name}.png'); print(name)
import os; os.makedirs('out',exist_ok=True)

# 1. Feed post 1080x1350
w,h=1080,1350
b=T(70,190,'// 30_DAY_AI_SPRINT',30,GOLD,700,'JetBrains Mono',ls=2)
b+=H(70,320,['Use AI to be','better at','your job.'],116,gold_idx=(2,))
b+=T(70,640,'30 minutes a day. Lessons written for your field.',36,CREAM,500)
b+=T(70,690,'Real work from Day 1. No coding.',36,GREY,500)
b+=chat(70,750,940)
b+=T(70,1175,'₦10,000',110,GOLD,800,'Inter Display')+T(560,1130,'for the full',32,GREY,500)+T(560,1172,'30 days',32,CREAM,700)
b+=pills(70,1200,['Day 1 free','7-day money-back'],26)
b+=brand(w,h,1300)
save('01-feed-post-1080x1350',w,h,b)

# 2. Story / WhatsApp status 1080x1920
w,h=1080,1920
b=T(80,260,'// FOR NIGERIAN PROFESSIONALS',30,GOLD,700,'JetBrains Mono',ls=2)
b+=H(80,420,['Everyone says','"use AI".','Nobody shows','you how.'],120,gold_idx=(3,))
b+=T(80,960,'We do. In 30 minutes a day.',44,CREAM,600)
b+=chat(80,1030,920)
b+=T(80,1500,'₦10,000',150,GOLD,800,'Inter Display')+T(700,1440,'30 days',40,CREAM,700)+T(700,1490,'one payment',34,GREY,500)
b+=pills(80,1550,['Day 1 free','No coding','Money-back'],30)
s,_=pill(80,1680,'Tap the link / reply "AI" to start →',38); b+=s
b+=brand(w,h,1850)
save('02-status-story-1080x1920',w,h,b)

# 3. Tonight deadline status
w,h=1080,1920
b=T(80,300,'// FOUNDING COHORT',32,GOLD,700,'JetBrains Mono',ls=2)
b+=H(80,470,['Closes','tonight,','11:59 pm.'],150,gold_idx=(2,))
b+=T(80,960,'Join today and start the 30-Day AI Sprint',44,CREAM,600)
b+=T(80,1020,'together with this week’s group.',44,CREAM,600)
items=['30 daily lessons for your field (6 tracks)','Copy-ready prompts: ChatGPT, Claude, Gemini','Daily WhatsApp nudge + help when stuck','Portfolio + certificate at the end']
for i,it in enumerate(items):
    y=1140+i*90; b+=f'<circle cx="104" cy="{y-14}" r="22" fill="{GOLD}"/>'+T(93,y-3,'✓',28,BG,800)+T(150,y,it,36,CREAM,500)
b+=T(80,1600,'₦10,000',140,GOLD,800,'Inter Display')+T(720,1545,'7-day',38,CREAM,700)+T(720,1592,'money-back',38,GREY,500)
s,_=pill(80,1680,'Reply "AI" to get your code →',40); b+=s
b+=brand(w,h,1850)
save('03-tonight-deadline-1080x1920',w,h,b)

# 4. Landscape (LinkedIn / Facebook / X) 1200x675
w,h=1200,675
b=T(70,140,'// 30-DAY PROFESSIONAL AI SPRINT',24,GOLD,700,'JetBrains Mono',ls=2)
b+=H(70,240,['Use AI to be better','at your job.'],80,gold_idx=(1,))
b+=T(70,400,'30 minutes a day · written for your field · no coding',30,CREAM,500)
b+=T(70,520,'₦10,000',96,GOLD,800,'Inter Display')+T(480,480,'for 30 days',30,CREAM,700)+T(480,520,'Day 1 free · 7-day money-back',26,GREY,500)
b+=brand(w,h,615)
save('04-landscape-1200x675',w,h,b)

# 5-7 carousel 1080x1350
w,h=1080,1350
b=T(70,180,'1 / 3',30,GOLD,700,'JetBrains Mono')+H(70,340,['You tried','ChatGPT.','It felt generic.'],120,gold_idx=(2,))
for i,(k,v) in enumerate([('WARN','The answers didn’t fit your work'),('WARN','Reports and replies eat your evenings'),('WARN','No time for long video courses')]):
    y=820+i*120; b+=f'<rect x="70" y="{y-60}" width="940" height="96" rx="20" fill="{CARD}" stroke="{GOLD}" stroke-opacity="0.3"/>'+T(100,y,k,26,'#E0A458',700,'JetBrains Mono')+T(210,y,v,34,CREAM,500)
b+=T(70,1240,'Swipe →',36,GOLD,700)+brand(w,h,1300)
save('05-carousel-1-1080x1350',w,h,b)
b=T(70,180,'2 / 3',30,GOLD,700,'JetBrains Mono')+H(70,320,['In 30 days','you will…'],120,gold_idx=(1,))
for i,(k,v) in enumerate([('Write in minutes','Emails, reports, proposals that sound like you'),('Read less, know more','Long PDFs and spreadsheets, summarised and checked'),('Turn paper into data','Receipts and voice notes into tables'),('Prove it','A portfolio and certificate for your boss or clients')]):
    y=620+i*145; b+=f'<rect x="70" y="{y-70}" width="940" height="125" rx="22" fill="{CARD}" stroke="{GOLD}" stroke-opacity="0.3"/>'+T(110,y-10,k,40,GOLD,800,'Inter Display')+T(110,y+36,v,30,CREAM,400)
b+=T(70,1240,'Swipe →',36,GOLD,700)+brand(w,h,1300)
save('06-carousel-2-1080x1350',w,h,b)
b=T(70,180,'3 / 3',30,GOLD,700,'JetBrains Mono')+H(70,330,['Start today.','Pay once.'],120,gold_idx=(1,))
b+=T(70,690,'₦10,000',170,GOLD,800,'Inter Display')+T(70,760,'for the full 30 days · 30 minutes a day',38,CREAM,500)
for i,(n,t) in enumerate([('01','Take the 1-minute quiz'),('02','Pay, get your code the same day'),('03','30 minutes a day on real work')]):
    y=880+i*95; b+=T(70,y,n,40,GOLD,700,'JetBrains Mono')+T(160,y,t,40,CREAM,600)
b+=pills(70,1135,['Day 1 free','7-day money-back','No coding'],28)
b+=T(70,1240,'Link in bio · WhatsApp 0703 313 4979',34,GOLD,700)+brand(w,h,1300)
save('07-carousel-3-1080x1350',w,h,b)
