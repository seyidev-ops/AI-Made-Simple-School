import sys, math
from engine import *
G=1560; FAB=['#B5523B','#2E7D6B','#C9A84C','#6A4C93','#E07A5F','#3D6FA5']
def woman(x,y,s=1.3,face='neutral',**kw):
    sp,head,sh=stick(x,y,s,face=face,**kw); hx,hy=head
    dress=f'<path d="M{x-16*s:.0f} {sh[1]+12*s:.0f} L{x+16*s:.0f} {sh[1]+12*s:.0f} L{x+62*s:.0f} {y-50*s:.0f} L{x-62*s:.0f} {y-50*s:.0f} Z" fill="#B5523B" stroke="{CREAM}" stroke-width="{6*s:.0f}" stroke-linejoin="round"/>'
    dress+=''.join(f'<circle cx="{x+dx*s:.0f}" cy="{y+dy*s:.0f}" r="{6*s:.0f}" fill="{GOLD}"/>' for dx,dy in [(-25,-80),(10,-110),(30,-75),(-5,-150),(-35,-115)])
    gele=f'<path d="M{hx-58*s:.0f} {hy-18*s:.0f} Q{hx-30*s:.0f} {hy-105*s:.0f} {hx+20*s:.0f} {hy-80*s:.0f} Q{hx+70*s:.0f} {hy-70*s:.0f} {hx+58*s:.0f} {hy-18*s:.0f} Q{hx:.0f} {hy-48*s:.0f} {hx-58*s:.0f} {hy-18*s:.0f}Z" fill="{GOLD}" stroke="{CREAM}" stroke-width="{4*s:.0f}"/>'
    gele+=f'<path d="M{hx+40*s:.0f} {hy-70*s:.0f} q30 -40 50 -10 q-20 10 -50 10z" fill="{GOLD}" stroke="{CREAM}" stroke-width="{3*s:.0f}"/>'
    return sp+dress+gele, head
def ground(): return line((-50,G),(W+50,G),c=GREY,w=4)
def shop(): 
    o=''
    for r in range(3):
        o+=f'<rect x="560" y="{760+r*170}" width="440" height="14" rx="4" fill="{GOLD}" opacity="0.8"/>'
        for k in range(5): o+=f'<rect x="{580+k*84}" y="{760+r*170-120}" width="66" height="118" rx="10" fill="{FAB[(k+r*2)%6]}" stroke="{CREAM}" stroke-width="3"/>'+line((580+k*84+12,760+r*170-100),(580+k*84+54,760+r*170-100),c=CREAM,w=3)
    return o
def counter(): return f'<rect x="80" y="1330" width="560" height="230" rx="14" fill="#2A2420" stroke="{GOLD}" stroke-width="4"/>'+T(360,1460,'AMAKA FABRICS',40,GOLD,800,'Inter Display')
def phonebox(cx,cy,w,h,inner,sc=1,op=1):
    return (f'<g opacity="{op:.2f}" transform="translate({cx},{cy}) scale({sc:.3f}) translate({-w/2},{-h/2})"><rect x="0" y="0" width="{w}" height="{h}" rx="56" fill="#1D1D21" stroke="{CREAM}" stroke-width="8"/>'
            f'<rect x="22" y="22" width="{w-44}" height="{h-44}" rx="38" fill="{BG}"/><rect x="{w/2-50}" y="40" width="100" height="14" rx="7" fill="#2a2a2f"/>{inner}</g>')

def s1(lt,L):
    o=cap(['Meet Amaka.','Fabrics & ready-to-wear,','Abuja.'],P(lt,0.1,0.8),gold=(2,))+ground()+shop()
    wm,_=woman(330,1520,1.25,face='happy',aL=(-40,-20),aR=(40,20)); return o+wm+counter()
MSGS=['How much is this one?','Do you deliver to Gwarinpa?','Is it still available??','Pls send price list','Last price?','Hello?? Are you there?','Can I pay on delivery?','Do you have size XL?']
def s2(lt,L):
    o=cap(['100+ messages','every single day.'],P(lt,0.1,0.8),gold=(1,))
    n=min(len(MSGS),int(lt/0.45)+1); inner=''
    st=max(0,n-7)
    for i,m in enumerate(MSGS[st:n]):
        y=110+i*95
        inner+=f'<rect x="50" y="{y}" width="{len(m)*13.5+50}" height="74" rx="22" fill="#26262B"/>'+T(75,y+48,m,28,CREAM,500,anchor='start')
    o+=phonebox(640,1080,520,900,inner)
    cnt=min(99,int(12+lt*22)); o+=f'<circle cx="880" cy="650" r="54" fill="{RED}"/>'+T(880,668,f'{cnt}+' if cnt>=99 else str(cnt),40,'#fff',800)
    wm,head=woman(220,G,1.1,face='sad',aL=(-30,-10),aR=(150,170),tilt=-6); o+=wm+sweat(head[0]+60,head[1]-30,lt)+ground()
    return o
def s3(lt,L):
    o=cap(['And the sales records…'],P(lt,0.1,0.7))
    o+=f'<g transform="rotate(-4 540 980)"><rect x="170" y="620" width="740" height="680" rx="16" fill="#EDE6D6"/>'+line((540,630),(540,1290),c='#C8BFA9',w=4)
    scr=[('Mrs Bola - 4,500?',220,700),('paid?? ask',230,780),('Ada 2 sets',220,880),('~~12,000~~ 10k',225,960),('Emeka owes??',600,720),('deliv. Wuse',600,800),('3 yds blue',600,900),('who paid??',600,1000)]
    for i,(t_,x,y) in enumerate(scr):
        if lt>0.3+i*0.25: o+=T(x,y,t_.replace('~~',''),36,'#3a3328',600,'Inter',anchor='start')
        if '~~' in t_ and lt>0.3+i*0.25: o+=line((x,y-12),(x+150,y-12),c=RED,w=5)
    o+=''.join(f'<path d="M{200+k*60} {1120+((k*37)%40)} q20 -30 40 0 t40 0" fill="none" stroke="#7a6f5a" stroke-width="4"/>' for k in range(10) if lt>2)
    o+='</g>'
    wm,head=woman(860,G,1.05,face='sad',aL=(-20,-10),aR=(160,200)); o+=wm+ground()
    o+=bubble(380,1330,460,130,['Ah! Who even paid','last week?'],P(lt,0.8,1.3),size=36,tail='right')
    return o
def s4(lt,L):
    o=cap(['So she joined the','30-Day AI Sprint.'],P(lt,0.1,0.8),gold=(1,))
    p=ease(P(lt,0.2,1.2))
    inner=(T(260,150,'// 30_DAY_AI_SPRINT',24,GOLD,700,'JetBrains Mono')+T(260,240,'Your track:',38,GREY,500)+T(260,300,'Small Business',50,CREAM,800,'Inter Display')+T(260,360,'Owner',50,GOLD,800,'Inter Display'))
    for i,t_ in enumerate(['Customer replies','Social media posts','Records & prices','30 min a day']):
        y=450+i*78; inner+=f'<rect x="50" y="{y-44}" width="420" height="62" rx="16" fill="{CARD}" stroke="{GOLD}" stroke-opacity="0.4"/>'+T(260,y-3,t_,28,CREAM,600)
    o+=phonebox(560,1100,520,860,inner,sc=0.3+0.7*p,op=cl(lt*3))
    return o
def s5(lt,L):
    o=cap(['AI now helps her','every day.'],P(lt,0.05,0.6),y=270,gold=(1,))
    f=lambda i: P(lt,0.4+i*L*0.27,0.9+i*L*0.27)
    # 1 reply
    a=f(0)
    if a>0:
        o+=f'<g {pop(a)}>'+card(80,470,920,330)+T(120,530,'1 · CUSTOMER REPLY',26,GOLD,700,'JetBrains Mono',anchor='start')
        o+=f'<rect x="120" y="560" width="520" height="66" rx="20" fill="#26262B"/>'+T(145,604,'How much is the Ankara set?',28,CREAM,500,anchor='start')
        o+=f'<rect x="300" y="645" width="660" height="130" rx="20" fill="{GOLD}" fill-opacity="0.16" stroke="{GOLD}" stroke-opacity="0.5"/>'
        o+=T(325,690,'₦18,000, sizes M to XL. Delivery in Abuja',27,CREAM,600,anchor='start')+T(325,730,'is ₦2,000. Shall I reserve one for you?',27,CREAM,600,anchor='start')+T(935,762,'AI draft ✓',22,GOLD,700,anchor='end')+'</g>'
    a=f(1)
    if a>0:
        o+=f'<g {pop(a)}>'+card(80,830,920,300)+T(120,890,'2 · INSTAGRAM POST',26,GOLD,700,'JetBrains Mono',anchor='start')
        for k in range(6): o+=f'<rect x="{120+k*35}" y="915" width="35" height="180" fill="{FAB[k]}"/>'
        o+=T(370,960,'New Ankara sets just landed.',30,CREAM,700,anchor='start')+T(370,1005,'Sizes M to XL. Abuja delivery.',28,CREAM,400,anchor='start')+T(370,1050,'Send a DM to order.',28,GOLD,600,anchor='start')+'</g>'
    a=f(2)
    if a>0:
        o+=f'<g {pop(a)}>'+card(80,1160,920,370)+T(120,1220,'3 · SALES SPREADSHEET',26,GOLD,700,'JetBrains Mono',anchor='start')
        cols=[120,290,520,760]; hdr=['Date','Customer','Item','Paid']
        o+=''.join(T(c,1275,h,26,GOLD,700,anchor='start') for c,h in zip(cols,hdr))
        rows=[('Mon','Mrs Bola','Ankara set','₦18,000 ✓'),('Tue','Ada','2 gowns','₦30,000 ✓'),('Wed','Emeka','3 yds lace','Owes ₦9,000')]
        for r,row in enumerate(rows):
            if P(lt,0.6+2*L*0.27+r*0.35,0.9+2*L*0.27+r*0.35)>0:
                y=1335+r*60; o+=line((120,y-42),(960,y-42),c='#2a2a2f',w=2)+''.join(T(c,y,v,28,RED if v.startswith('Owes') else CREAM,500,anchor='start') for c,v in zip(cols,row))
        o+='</g>'
    return o
def s6(lt,L):
    o=cap(['30 minutes a day.','Fast answers. Clear numbers.'],P(lt,0.1,0.8),gold=(1,))+ground()+shop()
    up=ease(P(lt,0.2,1))
    wm,_=woman(330,1520,1.25,face='happy',aL=(-40-100*up,-50-100*up),aR=(40+100*up,50+100*up)); o+=wm+counter()
    for k,(x0,c) in enumerate([(1180,FAB[1]),(1330,FAB[3])]):
        x=x0-430*ease(P(lt,0.3+k*0.4,2+k*0.4)); sw=math.sin(lt*10+k)*22*(1-P(lt,1.8+k*0.4,2+k*0.4))
        cs,_,_=stick(x,G,1.0,aL=(-20,-10),aR=(25,5),lL=(-sw,0),lR=(sw,0),face='happy'); o+=cs+f'<rect x="{x+38}" y="{G-185}" width="50" height="60" rx="6" fill="{c}" stroke="{CREAM}" stroke-width="3"/>'
    return o
def s7(lt,L): return cta(lt,['Run a business?','There is a track','for you.'],'for the full 30 days · 30 minutes a day',['Day 1 free','Small business track','7-day money-back'],'aimadesimpleschool.com')
N=lambda s:(NV,'+5%','+0Hz',s)  # narrator here is male Abeo for variety
NM=lambda s:(MV,'+5%','+0Hz',s)
AM=lambda s:(NV,'+0%','+4Hz',s)
beats=[dict(say=NM("Meet Amaka. She sells fabrics and ready-to-wear in Abuja."),draw=s1,post=0.4),
 dict(say=NM("Every day, over a hundred WhatsApp messages. How much? Do you deliver? Is it still available?"),draw=s2,post=0.3),
 dict(say=NM("And her sales records?"),draw=s3,scene='nb',post=0.1),
 dict(say=AM("Ah! Who even paid last week?"),draw=lambda lt,L:s3(lt+1.6,L),scene='nb',pre=0.1,post=0.5),
 dict(say=NM("So Amaka joined the 30-Day AI Sprint, on the small business track."),draw=s4,post=0.4),
 dict(say=NM("Now AI drafts her customer replies, writes her Instagram captions, and turns her notebook into a clean sales spreadsheet."),draw=s5,post=1.6),
 dict(say=AM("Thirty minutes a day. My customers get fast answers, and I finally know my numbers."),draw=s6,post=0.6),
 dict(say=NM("Running a business? The 30-Day AI Sprint has a track for you. Ten thousand naira for thirty days, and Day one is free. Visit aimadesimpleschool.com today."),draw=s7,post=1.5,min=8)]
if __name__=='__main__':
    if len(sys.argv)>1: build('Video2-Amaka-Small-Business',beats,[[45,52,57,60],[41,53,57,60],[48,55,60,64],[43,55,59,62]],0.4,stills=[float(x) for x in sys.argv[1:]])
    else: build('Video2-Amaka-Small-Business',beats,[[45,52,57,60],[41,53,57,60],[48,55,60,64],[43,55,59,62]],0.4)
