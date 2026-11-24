import sys, math
from engine import *
G=1600
def ground(): return line((-50,G),(W+50,G),c=GREY,w=4)
def chatwin(x,y,w,h): return card(x,y,w,h)+f'<circle cx="{x+40}" cy="{y+40}" r="9" fill="{RED}"/><circle cx="{x+70}" cy="{y+40}" r="9" fill="{GOLD}"/><circle cx="{x+100}" cy="{y+40}" r="9" fill="#5FA36B"/>'+T(x+w-40,y+50,'AI chat',24,GREY,600,'JetBrains Mono',anchor='end')
def typed(s,p): return s[:int(len(s)*cl(p))]
def s1(lt,L):
    o=''
    for i,l in enumerate(['Stop using','ChatGPT','like Google.']):
        o+=T(W/2,420+i*150,l,140,GOLD if i==2 else CREAM,800,'Inter Display',op=ease(P(lt,0.05+i*0.25,0.5+i*0.25)))
    a=ease(P(lt,0.6,1.2))
    o+=f'<g opacity="{a:.2f}"><rect x="190" y="900" width="700" height="100" rx="50" fill="{CARD}" stroke="{CREAM}" stroke-width="4"/><circle cx="260" cy="950" r="22" fill="none" stroke="{GREY}" stroke-width="6"/>'+line((276,966),(296,986),c=GREY,w=6)+T(320,962,'write a report',36,GREY,500,anchor='start')+'</g>'
    x=ease(P(lt,1.2,1.6))
    if x>0: o+=f'<g opacity="{x:.2f}">'+line((170,880),(910,1020),c=RED,w=16)+line((910,880),(170,1020),c=RED,w=16)+'</g>'
    sh=math.sin(lt*12)*14*P(lt,1.2,1.5)*(1-P(lt,2.5,3))
    sp,_,_=stick(540,G,1.3,aL=(-30,-15),aR=(30,15),face='neutral',tilt=sh); return o+sp+ground()
BAD="In today's fast-paced world, reports are an essential tool for communication. A good report should be clear, concise and well-structured. Here are some general tips to consider…"
def s2(lt,L,phase=0):
    o=cap(['Generic in.','Generic out.'],P(lt,4.0,4.6) if phase else 0,y=290,gold=(1,))
    o+=chatwin(70,450,940,700)
    msg=typed('Write a report.',P(lt,0.2,1.0))
    if msg: o+=f'<rect x="560" y="530" width="400" height="80" rx="24" fill="{GOLD}"/>'+T(940,582,msg,34,BG,700,anchor='end')
    if lt>1.4:
        o+=T(110,680,'AI',26,GOLD,700,'JetBrains Mono',anchor='start')
        shown=typed(BAD,P(lt,1.5,3.6)); o+=textblock(110,730,shown,46,32,'#B9B5AC',400,1.35)
    if lt>3.8:
        a=ease(P(lt,3.8,4.2)); o+=f'<g opacity="{a:.2f}" transform="rotate(-8 800 1060)"><rect x="620" y="1010" width="340" height="96" rx="12" fill="none" stroke="{RED}" stroke-width="7"/>'+T(790,1077,'GENERIC',52,RED,800,'Inter Display')+'</g>'
    sp,_,_=stick(540,G,1.15,aL=(-30,-15),aR=(150,175),face='sad' if lt>3.8 else 'neutral',tilt=-6); return o+sp+ground()
CARDS=[('PERSONA','Who should it be?','"You are an operations manager at a logistics company in Lagos."'),
       ('CONTEXT','What does it need to know?','"Here are my notes from this week. My director will read it."'),
       ('TASK','Exactly what you want','"Write a one-page weekly report: summary, 3 risks, next steps. Plain English."')]
def s3(lt,L):
    o=cap(['The Persona, Context,','Task formula'],P(lt,0.05,0.6),y=270,gold=(1,))
    o+=T(W/2,450,'Day 1 of the 30-Day AI Sprint',34,GREY,600,op=ease(P(lt,0.3,0.8)))
    for i,(h,sub,ex) in enumerate(CARDS):
        p=P(lt,L*(0.22+i*0.22),L*(0.22+i*0.22)+0.6)
        if p<=0: continue
        dx=(1-ease(p))*300; y=520+i*330
        o+=f'<g opacity="{ease(p):.2f}" transform="translate({dx:.0f},0)">'+card(70,y,940,300)+f'<rect x="70" y="{y}" width="16" height="300" rx="8" fill="{GOLD}"/>'
        o+=T(120,y+75,f'{i+1}. {h}',50,GOLD,800,'Inter Display',anchor='start')+T(960,y+72,sub,28,GREY,500,anchor='end')
        o+=textblock(120,y+150,ex,44,36,CREAM,500,1.32)+'</g>'
    return o
def s4(lt,L):
    o=cap(['Same AI.','Completely different answer.'],P(lt,0.05,0.6),y=270,gold=(1,))
    o+=chatwin(70,430,940,850)
    o+=T(110,530,'AI',26,GOLD,700,'JetBrains Mono',anchor='start')+T(110,600,'Weekly Operations Report',46,CREAM,800,'Inter Display',anchor='start')+T(110,645,'Week 47 · for the Director',28,GREY,500,anchor='start')
    secs=[('Summary','Deliveries up 8% on last week; 2 trucks out for repair.'),('Risks','1. Fuel cost rising  2. Driver shortage Friday  3. Late invoice from Ace Ltd'),('Next steps','Book repair Wed · cover Friday · chase Ace Ltd')]
    for i,(h,b_) in enumerate(secs):
        p=P(lt,0.6+i*0.7,1.0+i*0.7)
        if p>0:
            y=730+i*185; o+=f'<g {pop(p)}>'+T(110,y,h,36,GOLD,800,'Inter Display',anchor='start')+textblock(110,y+55,b_,48,32,CREAM,400,1.3)+'</g>'
    if lt>2.8: o+=check_item(140,1225,'Ready to send',P(lt,2.8,3.2))
    sp,_,_=stick(860,G,0.9,aL=(-120,-170),aR=(30,15),face='happy'); return o+sp+ground()
def s5(lt,L):
    o=cap(['Pro tip: make it','check itself.'],P(lt,0.05,0.6),y=270,gold=(1,))
    o+=chatwin(70,430,940,880)
    q=typed('What did you assume, and what might be wrong?',P(lt,0.5,2.0))
    if q: o+=f'<rect x="170" y="520" width="800" height="140" rx="24" fill="{GOLD}"/>'+textblock(940,575,q,36,34,BG,700,1.3,anchor='end')
    if lt>2.4:
        a=ease(P(lt,2.4,2.9)); o+=f'<g opacity="{a:.2f}">'+T(110,730,'AI',26,GOLD,700,'JetBrains Mono',anchor='start')
        o+=textblock(110,790,'I assumed the delivery figures are for Lagos only.',46,34,CREAM,500,1.3)
        o+=textblock(110,920,'Please check the fuel cost: your notes show two different numbers (₦1,050 and ₦1,150 per litre).',46,34,CREAM,500,1.3)+'</g>'
    if lt>4: o+=check_item(140,1180,'Mistake caught early',P(lt,4,4.4))
    return o
def s6(lt,L): return cta(lt,['That was Day 1.','Try it free.'],'for the full 30 days · 30 minutes a day',['Day 1 free','No coding','7-day money-back'],'aimadesimpleschool.com',tag='// 30-DAY AI SPRINT · DAY 1')
N=lambda s:(NV,'+6%','+0Hz',s); C=lambda s:(MV,'+0%','+0Hz',s)
beats=[dict(say=N("Stop using ChatGPT like Google."),draw=s1,min=3.4,post=0.8),
 dict(say=C("Write a report."),draw=s2,scene='bad',pre=0.3,post=3.3),
 dict(say=N("Generic in. Generic out."),draw=lambda lt,L:s2(lt+4.0,L,1),scene='bad',pre=0.1,post=0.6),
 dict(say=N("Use the Persona, Context, Task formula. Persona: tell it who to be. Context: give it your notes and who will read it. Task: say exactly what you want, and in what format."),draw=s3,post=1.2),
 dict(say=N("Same AI. Completely different answer."),draw=s4,post=2.2,min=4.5),
 dict(say=N("Then ask one more thing: what did you assume, and what might be wrong? That's how you catch mistakes before your boss does."),draw=s5,post=0.8),
 dict(say=N("That was Day 1 of the 30-Day AI Sprint, and it's free. The full Sprint is ten thousand naira, thirty minutes a day. Try Day 1 at aimadesimpleschool.com."),draw=s6,post=1.5,min=8)]
PROG=[[50,57,62,65],[46,53,58,62],[41,53,57,60],[48,55,60,64]]
if __name__=='__main__':
    st=[float(x) for x in sys.argv[1:]] or None
    build('Video3-Stop-Using-ChatGPT-Like-Google',beats,PROG,0.6,stills=st)
