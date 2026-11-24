import math, subprocess, sys, html, cairosvg
W,H,FPS=1080,1920,24; DUR=38.0
BG='#0E0E10'; GOLD='#C9A84C'; CREAM='#F0EDE6'; GREY='#8A877F'; CARD='#17171A'; RED='#E07A5F'
E=html.escape
def cl(x,a=0,b=1): return max(a,min(b,x))
def ease(t): t=cl(t); return t*t*(3-2*t)
def back(t): t=cl(t); c=1.7; return 1+(c+1)*(t-1)**3+c*(t-1)**2
def P(t,a,b): return cl((t-a)/(b-a))
def T(x,y,s,size,fill=CREAM,w=400,fam='Inter',anchor='middle',op=1):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-family="{fam}" font-weight="{w}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" opacity="{op:.3f}">{E(s)}</text>'
def seg(p,a,L): return (p[0]+L*math.sin(math.radians(a)), p[1]+L*math.cos(math.radians(a)))
def line(*pts,c=CREAM,w=11): return '<polyline points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in pts)+f'" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
def stick(x,y,s=1,aL=(-20,-10),aR=(20,10),lL=(-12,0),lR=(12,0),face='neutral',tilt=0,c=CREAM,sit=False,extra=''):
    hip=(x,y-120*s); sh=(x+tilt*0.6*s,y-240*s); head=(x+tilt*s,y-295*s); r=44*s
    o=''
    for (a1,a2) in (lL,lR):
        k=seg(hip,a1,62*s); f=seg(k,a2,62*s); o+=line(hip,k,f,c=c,w=11*s)
    o+=line(hip,sh,c=c,w=11*s)
    for (a1,a2) in (aL,aR):
        e=seg(sh,a1,58*s); h=seg(e,a2,56*s); o+=line(sh,e,h,c=c,w=10*s)
    o+=f'<circle cx="{head[0]:.1f}" cy="{head[1]:.1f}" r="{r:.1f}" fill="{BG}" stroke="{c}" stroke-width="{10*s:.1f}"/>'
    hx,hy=head
    o+=f'<circle cx="{hx-15*s:.1f}" cy="{hy-6*s:.1f}" r="{5*s:.1f}" fill="{c}"/><circle cx="{hx+15*s:.1f}" cy="{hy-6*s:.1f}" r="{5*s:.1f}" fill="{c}"/>'
    if face=='happy': o+=f'<path d="M{hx-17*s:.1f} {hy+12*s:.1f} Q{hx:.1f} {hy+30*s:.1f} {hx+17*s:.1f} {hy+12*s:.1f}" fill="none" stroke="{c}" stroke-width="{5*s:.1f}" stroke-linecap="round"/>'
    elif face=='sad': o+=f'<path d="M{hx-15*s:.1f} {hy+22*s:.1f} Q{hx:.1f} {hy+8*s:.1f} {hx+15*s:.1f} {hy+22*s:.1f}" fill="none" stroke="{c}" stroke-width="{5*s:.1f}" stroke-linecap="round"/>'
    else: o+=line((hx-12*s,hy+16*s),(hx+12*s,hy+16*s),c=c,w=5*s)
    return o, head, sh
def bubble(x,y,w,h,text_lines,op,size=40,tail='left',fill=CARD,tc=CREAM,stroke=GOLD):
    if op<=0: return ''
    sc=0.6+0.4*back(op)
    tx= x+60 if tail=='left' else x+w-60
    o=f'<g opacity="{cl(op*1.5):.3f}" transform="translate({x+w/2:.1f},{y+h:.1f}) scale({sc:.3f}) translate({-(x+w/2):.1f},{-(y+h):.1f})">'
    o+=f'<path d="M{tx-20} {y+h-2} L{tx+(-30 if tail=="left" else 30)} {y+h+50} L{tx+25} {y+h-2}Z" fill="{fill}" stroke="{stroke}" stroke-width="3"/>'
    o+=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="34" fill="{fill}" stroke="{stroke}" stroke-width="3"/>'
    o+=f'<rect x="{tx-18}" y="{y+h-6}" width="40" height="10" fill="{fill}"/>'
    n=len(text_lines); y0=y+h/2-(n-1)*size*0.62+size*0.35
    for i,l in enumerate(text_lines): o+=T(x+w/2,y0+i*size*1.24,l,size,tc,600)
    return o+'</g>'
CAP=[]
def caption(lines,op,y=330,size=66,gold=()):
    if op<=0: return ''
    CAP.append(_cap(lines,op,y,size,gold)); return ''
def _cap(lines,op,y,size,gold):
    dy=(1-ease(op))*30; o=''
    for i,l in enumerate(lines): o+=T(W/2,y+i*size*1.18+dy,l,size,GOLD if i in gold else CREAM,800,'Inter Display',op=ease(op))
    return o
def desk(x,y):  # desk top at y
    return (f'<rect x="{x}" y="{y}" width="520" height="22" rx="6" fill="{GOLD}" opacity="0.9"/>'
            +line((x+40,y+22),(x+40,y+240),c=GOLD,w=10)+line((x+480,y+22),(x+480,y+240),c=GOLD,w=10))
def laptop(x,y,glow=0):
    o=f'<path d="M{x} {y} L{x+40} {y-150} L{x+230} {y-150} L{x+200} {y} Z" fill="#26262B" stroke="{CREAM}" stroke-width="6" stroke-linejoin="round"/>'
    o+=f'<rect x="{x-20}" y="{y-6}" width="260" height="14" rx="5" fill="{CREAM}"/>'
    if glow: o+=f'<path d="M{x+20} {y-15} L{x+52} {y-138} L{x+218} {y-138} L{x+188} {y-15} Z" fill="{GOLD}" opacity="{0.35*glow:.2f}"/>'
    return o
def papers(x,y,n,t):
    o=''
    for i in range(int(n)):
        rot=((i*37)%11-5)*1.4+math.sin(t*3+i)*0.6
        o+=f'<g transform="rotate({rot:.1f} {x+80} {y-i*18})"><rect x="{x}" y="{y-i*18-16}" width="160" height="16" rx="3" fill="{CREAM}" opacity="0.92"/><line x1="{x+15}" y1="{y-i*18-8}" x2="{x+120}" y2="{y-i*18-8}" stroke="{GREY}" stroke-width="3"/></g>'
    return o
def envelope(x,y,num,op=1):
    return (f'<g opacity="{op:.2f}"><rect x="{x}" y="{y}" width="120" height="84" rx="10" fill="none" stroke="{CREAM}" stroke-width="6"/>'
            +line((x,y+4),(x+60,y+48),(x+120,y+4),w=6)
            +f'<circle cx="{x+120}" cy="{y}" r="36" fill="{RED}"/>'+T(x+120,y+13,str(num),34,'#fff',800)+'</g>')
def clock(x,y,r,hh,mm,op=1):
    o=f'<g opacity="{op:.2f}"><circle cx="{x}" cy="{y}" r="{r}" fill="{CARD}" stroke="{GOLD}" stroke-width="7"/>'
    for i in range(12):
        a=math.radians(i*30); o+=line((x+math.sin(a)*(r-12),y-math.cos(a)*(r-12)),(x+math.sin(a)*(r-22),y-math.cos(a)*(r-22)),c=GREY,w=4)
    ah=math.radians((hh%12+mm/60)*30); am=math.radians(mm*6)
    o+=line((x,y),(x+math.sin(ah)*r*0.5,y-math.cos(ah)*r*0.5),w=9)+line((x,y),(x+math.sin(am)*r*0.75,y-math.cos(am)*r*0.75),c=GOLD,w=6)
    return o+'</g>'
def check_item(x,y,text,p):
    if p<=0: return ''
    s=back(p); o=f'<g opacity="{cl(p*2):.2f}"><circle cx="{x}" cy="{y}" r="{30*s:.1f}" fill="{GOLD}"/>'
    o+=line((x-13,y+1),(x-3,y+12),(x+15,y-11),c=BG,w=7)
    o+=T(x+55,y+14,text,44,CREAM,600,anchor='start')+'</g>'
    return o
def phone(cx,cy,sc,op):
    if op<=0: return ''
    w,h=420,780
    o=f'<g opacity="{op:.2f}" transform="translate({cx},{cy}) scale({sc:.3f}) translate({-w/2},{-h/2})">'
    o+=f'<rect x="0" y="0" width="{w}" height="{h}" rx="56" fill="#1D1D21" stroke="{CREAM}" stroke-width="8"/>'
    o+=f'<rect x="22" y="22" width="{w-44}" height="{h-44}" rx="38" fill="{BG}" stroke="{GOLD}" stroke-opacity="0.4" stroke-width="2"/>'
    o+=f'<rect x="{w/2-50}" y="40" width="100" height="16" rx="8" fill="#2a2a2f"/>'
    o+=T(w/2,140,'// 30_DAY_AI_SPRINT',22,GOLD,700,'JetBrains Mono')
    o+=T(w/2,230,'Use AI to be',46,CREAM,800,'Inter Display')+T(w/2,285,'better at',46,CREAM,800,'Inter Display')+T(w/2,340,'your job.',46,GOLD,800,'Inter Display')
    for i,t in enumerate(['30 min a day','Lessons for your field','Real work from Day 1']):
        y=420+i*72; o+=f'<rect x="50" y="{y-40}" width="{w-100}" height="58" rx="16" fill="{CARD}" stroke="{GOLD}" stroke-opacity="0.35"/>'+T(w/2,y-2,t,26,CREAM,600)
    o+=f'<rect x="60" y="{h-140}" width="{w-120}" height="70" rx="35" fill="{GOLD}"/>'+T(w/2,h-94,'Start Day 1 free →',28,BG,800)
    return o+'</g>'
def sweat(x,y,t):
    p=(t*1.4)%1
    return f'<path d="M{x} {y+p*60} q-12 22 0 30 q12 -8 0 -30z" fill="#7FB3D5" opacity="{1-p:.2f}"/>'

GROUND=1380
def frame(t):
    o=f'<rect width="{W}" height="{H}" fill="{BG}"/>'
    o+=f'<defs><pattern id="g" width="60" height="60" patternUnits="userSpaceOnUse"><path d="M60 0H0V60" fill="none" stroke="{GOLD}" stroke-opacity="0.06"/></pattern>'
    o+=f'<radialGradient id="r" cx="0.8" cy="0.05" r="0.8"><stop offset="0" stop-color="{GOLD}" stop-opacity="0.18"/><stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></radialGradient></defs>'
    o+=f'<rect width="{W}" height="{H}" fill="url(#g)"/><rect width="{W}" height="{H}" fill="url(#r)"/><rect width="{W}" height="8" fill="{GOLD}"/>'
    CAP.clear(); base=o; o=''
    if t<31.5: o+=line((-200,GROUND),(W+200,GROUND),c=GREY,w=4)
    # ---------- S1: overwhelmed
    if t<11:
        o+=caption(['Meet Tunde.','47 emails. 3 reports.','It\'s 9 pm.'],P(t,0.2,1.0) if t<5.5 else 1-P(t,5.2,5.6),gold=(2,))
        if t>=5.5: o+=caption(['Sound familiar?'],P(t,5.7,6.3),y=360,size=76)
        n=2+8*ease(P(t,0.5,4.5))
        typ=math.sin(t*28)*8
        sp,head,sh=stick(330,GROUND,1.05,aL=(70+typ,100),aR=(80-typ,105),lL=(90,0),lR=(85,5),face='sad',tilt=8)
        # seated: shift whole stick so hip at stool height
        o+=f'<g transform="translate(0,{-0})">{sp}</g>' if False else ''
        o+=desk(380,1150)+laptop(470,1150,glow=0.4)
        # seated stickman (hip at 1250)
        sp,head,sh=stick(330,1370,1.05,aL=(75+typ,110),aR=(85-typ,112),lL=(88,2),lR=(92,-2),face='sad',tilt=10)
        o+=sp+f'<rect x="260" y="1250" width="140" height="18" rx="6" fill="{GREY}"/>'+line((280,1268),(280,GROUND),c=GREY,w=8)+line((380,1268),(380,GROUND),c=GREY,w=8)
        o+=papers(720,1150,n,t)
        o+=envelope(560,820,int(12+35*ease(P(t,0.5,4))),op=ease(P(t,0.3,1)))
        o+=clock(860,760,90,9,int(60*((t*0.15)%1)),op=ease(P(t,0.6,1.4)))
        o+=sweat(head[0]+58,head[1]-30,t)
        # friend enters
        if t>=5.5:
            fx=1180-250*ease(P(t,5.5,7.0)); walk=math.sin(t*10)*25*(1-P(t,6.6,7.0))
            fs,fh,_=stick(fx,GROUND,1.0,aL=(-20-walk*0.5,-10),aR=(20+walk*0.5,10),lL=(-walk,0),lR=(walk,0),face='happy')
            o+=fs
            o+=bubble(520,440,440,170,['Why not just','use AI?'],P(t,7.0,7.5)-P(t,8.9,9.2),tail='right')
            o+=bubble(120,440,520,170,['I tried. The answers','were too generic.'],P(t,9.0,9.5),tail='left')
    # ---------- S2: phone
    elif t<17:
        o+=caption(['So he tried the','30-Day AI Sprint.'],P(t,11.1,11.8),gold=(1,))
        sp,head,sh=stick(300,GROUND,1.05,aL=(-25,-5),aR=(40,20),face='neutral' if t<14 else 'happy')
        o+=sp
        fs,_,_=stick(820,GROUND,1.0,aL=(-60,-90),aR=(20,10),face='happy'); o+=fs
        p=ease(P(t,11.4,12.6)); o+=phone(560+0*p,1000,0.25+0.75*p,cl(P(t,11.3,11.6)))
    # ---------- S3: progress
    elif t<26:
        o+=caption(['30 minutes a day.','Real work from Day 1.'],P(t,17.1,17.8),gold=(1,))
        day=1+int(29*ease(P(t,17.5,25)))
        o+=T(W/2,590,f'DAY {day}',120,GOLD,800,'Inter Display')
        o+=f'<rect x="240" y="640" width="600" height="14" rx="7" fill="{CARD}"/><rect x="240" y="640" width="{600*day/30:.0f}" height="14" rx="7" fill="{GOLD}"/>'
        typ=math.sin(t*22)*7
        o+=desk(380,1150)+laptop(470,1150,glow=1)
        sp,head,_=stick(330,1370,1.05,aL=(75+typ,110),aR=(85-typ,112),lL=(88,2),lR=(92,-2),face='happy',tilt=4)
        o+=sp+f'<rect x="260" y="1250" width="140" height="18" rx="6" fill="{GREY}"/>'+line((280,1268),(280,GROUND),c=GREY,w=8)+line((380,1268),(380,GROUND),c=GREY,w=8)
        o+=papers(720,1150,max(0,10-10*ease(P(t,18,24))),t)
        items=['Report done in 20 min','Emails answered','Proposal drafted','Receipts → spreadsheet']
        for i,it in enumerate(items): o+=check_item(170,710+i*72,it,P(t,18.5+i*1.5,19.0+i*1.5))
    # ---------- S4: relief
    elif t<31.5:
        o+=caption(['Same job.','Less stress. More done.'],P(t,26.1,26.8),gold=(1,))
        up=ease(P(t,26.2,27.2))
        sp,head,_=stick(330,GROUND,1.1,aL=(-30-100*up,-40-110*up),aR=(30+100*up,40+110*up),face='happy'); o+=sp
        o+=clock(330,660,80,5,0,op=ease(P(t,26.3,27)))
        bs,_,_=stick(800,GROUND,1.0,aL=(-20,-10),aR=(120,175),face='happy'); o+=bs
        o+=bubble(500,560,440,170,['This report is','excellent!'],P(t,27.6,28.1),tail='right')
        for k in range(10):
            ph=(t*0.9+k*0.37)%1; x=120+k*95; y=900-ph*300
            if t>27: o+=f'<circle cx="{x}" cy="{y:.0f}" r="{6+k%3*3}" fill="{GOLD}" opacity="{(1-ph)*0.7:.2f}"/>'
    if t<31.5:
        o=base+'<g transform="translate(540,1250) scale(1.2) translate(-540,-1100)">'+o+'</g>'+''.join(CAP)
    # ---------- S5: CTA
    else:
        o=base
        a=ease(P(t,31.6,32.3))
        o+=T(W/2,330,'// 30-DAY PROFESSIONAL AI SPRINT',32,GOLD,700,'JetBrains Mono',op=a)
        for i,l in enumerate(['Use AI to be','better at','your job.']):
            o+=T(W/2,520+i*130,l,124,GOLD if i==2 else CREAM,800,'Inter Display',op=ease(P(t,31.8+i*0.2,32.4+i*0.2)))
        b=ease(P(t,33,33.6))
        o+=T(W/2,1040,'₦10,000',190,GOLD,800,'Inter Display',op=b)
        o+=T(W/2,1110,'for the full 30 days · 30 minutes a day',40,CREAM,500,op=b)
        c=ease(P(t,33.8,34.4)); labels=['Day 1 free','No coding','7-day money-back']; xs=[115,385,635]; ws=[250,230,330]
        for x,wd,l in zip(xs,ws,labels):
            o+=f'<g opacity="{c:.2f}"><rect x="{x-20}" y="1180" width="{wd}" height="70" rx="35" fill="none" stroke="{GOLD}" stroke-width="3"/>'+T(x-20+wd/2,1226,l,32,CREAM,600)+'</g>'
        d=ease(P(t,34.6,35.2)); pulse=1+0.03*math.sin(t*6)
        o+=f'<g opacity="{d:.2f}" transform="translate(540,1380) scale({pulse:.3f}) translate(-540,-1380)"><rect x="140" y="1330" width="800" height="104" rx="52" fill="{GOLD}"/>'+T(540,1398,'aimadesimpleschool.com',46,BG,800)+'</g>'
        o+=T(W/2,1520,'or WhatsApp 0703 313 4979',42,CREAM,600,op=d)
    o+=T(80,H-90,'AI Made Simple',40,GOLD,800,'Inter Display',anchor='start')+T(W-80,H-90,'aimadesimpleschool.com',30,GREY,500,anchor='end')
    # scene fades
    for cut in (11,17,26,31.5):
        f=1-abs(t-cut)/0.25
        if f>0: o+=f'<rect width="{W}" height="{H}" fill="{BG}" opacity="{cl(f):.2f}"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">{o}</svg>'

if __name__=='__main__':
    if len(sys.argv)>1:
        for tt in sys.argv[1:]: cairosvg.svg2png(bytestring=frame(float(tt)).encode(),write_to=f'still_{tt}.png',output_width=540)
        sys.exit()
    ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate',str(FPS),'-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','20','-preset','medium','video_silent.mp4'],stdin=subprocess.PIPE)
    A=[(0,0),(6.9,5.5),(7.0,5.7),(8.3,7.0),(10.2,9.0),(14.3,11.0),(14.5,11.3),(21.7,17.0),(22.0,17.6),(33.0,25.0),(33.5,26.0),(33.7,26.2),(37.5,28.2),(40.7,31.5),(40.9,31.8),(57.0,38.0)]
    def vt(r):
        for (r0,v0),(r1,v1) in zip(A,A[1:]):
            if r<=r1: return v0+(v1-v0)*(r-r0)/(r1-r0)
        return A[-1][1]
    for i in range(int(57.0*FPS)):
        ff.stdin.write(cairosvg.svg2png(bytestring=frame(vt(i/FPS)).encode()))
    ff.stdin.close(); ff.wait(); print('done')
