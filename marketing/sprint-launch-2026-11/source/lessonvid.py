import sys, os, math, subprocess, cairosvg
from engine import *
REPO='/home/user/AI-Made-Simple-School'
ns={}; exec(open(f'{REPO}/tools/sprint/short.py').read(),ns)
import json
d=json.loads(subprocess.run(['node','-e',"global.window={};require('%s/sprint-content.js');console.log(JSON.stringify(window.AMS_SPRINT))"%REPO],capture_output=True,text=True).stdout)
OUTDIR=f'{REPO}/videos/sprint'; os.makedirs(OUTDIR,exist_ok=True)
G=1650
def lessons():
    out=[]
    for k,v in ns['SHORT'].items(): out.append((f'd{k:02d}',k,d['days'][str(k)],v,None))
    for t,days in ns['TRACK_SHORT'].items():
        for k,v in days.items(): out.append((f'{t}-d{k:02d}',k,d['trackDays'][t][str(k)],v,d['tracks'][t]['name']))
    return out
def wl(x,y,s,n,size,fill=CREAM,w=600,lh=1.22,anchor='start',op=1,fam='Inter'):
    return ''.join(T(x,y+i*size*lh,l,size,fill,w,fam,anchor=anchor,op=op) for i,l in enumerate(wrap(s,n)))
def nlines(s,n): return len(wrap(s,n))
def chatwin(x,y,w,h): return card(x,y,w,h)+f'<circle cx="{x+40}" cy="{y+40}" r="9" fill="{RED}"/><circle cx="{x+70}" cy="{y+40}" r="9" fill="{GOLD}"/><circle cx="{x+100}" cy="{y+40}" r="9" fill="#5FA36B"/>'+T(x+w-40,y+50,'AI chat',24,GREY,600,'JetBrains Mono',anchor='end')
def ground(): return line((-50,G),(W+50,G),c=GREY,w=4)
def make(lid,n,full,sh,trackname):
    title=full['t']; tool=full['tool']
    def s_title(lt,L):
        o=T(W/2,330,'// 30-DAY AI SPRINT · VIDEO CLASS',30,GOLD,700,'JetBrains Mono',op=ease(P(lt,0,0.4)))
        p=back(P(lt,0.1,0.7)); o+=f'<g transform="translate(540,600) scale({max(0.01,p):.3f}) translate(-540,-600)">'+T(W/2,640,f'DAY {n}',220,GOLD,800,'Inter Display')+'</g>'
        if trackname: o+=T(W/2,730,f'Week 2 · {trackname}',38,GREY,600,op=ease(P(lt,0.4,0.9)))
        o+=wl(W/2,860,title,20,82,CREAM,800,1.15,'middle',ease(P(lt,0.5,1.1)),'Inter Display')
        y=860+nlines(title,20)*82*1.15+40
        o+=wl(W/2,y,'Tools: '+tool,42,34,GREY,500,1.3,'middle',ease(P(lt,0.8,1.3)))
        wave=math.sin(lt*7)*25
        sp,_,_=stick(540,G,1.0,aL=(-25,-10),aR=(150+wave,175+wave),face='happy'); return o+sp+ground()
    vo_win=f"Today's win: {sh['win']} {sh['why']}"; fw=len("Today's win: "+sh['win'])/len(vo_win)
    def s_win(lt,L):
        o=T(80,340,"TODAY'S WIN",34,GOLD,700,'JetBrains Mono',anchor='start',op=ease(P(lt,0,0.4)))
        o+=wl(80,470,sh['win'],21,82,CREAM,800,1.15,op=ease(P(lt,0.1,0.6)),fam='Inter Display')
        y=470+nlines(sh['win'],21)*82*1.15+60
        o+=f'<rect x="80" y="{y-50}" width="120" height="8" rx="4" fill="{GOLD}" opacity="{ease(P(lt,(L-0.6)*fw,(L-0.6)*fw+0.4)):.2f}"/>'
        o+=wl(80,y+40,sh['why'],34,48,'#CFCBC2',500,1.32,op=ease(P(lt,(L-0.6)*fw,(L-0.6)*fw+0.5)))
        cx,cy=540,1450; a=ease(P(lt,0.3,0.9))
        o+=f'<g opacity="{a:.2f}">'+''.join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{GOLD}" stroke-width="10" opacity="{0.5+0.25*i:.2f}"/>' for i,r in enumerate((110,72,34)))
        ar=ease(P(lt,0.6,1.1)); ax=cx+260-260*ar; ay=cy-200+200*ar
        o+=line((ax+120,ay-90),(ax,ay),c=CREAM,w=10)+f'<path d="M{ax+110} {ay-110} l40 -10 l-10 40 z" fill="{CREAM}"/></g>'
        return o
    ask=sh['demo']['ask']; ans=sh['demo']['ans']
    def s_demo(lt,L):
        o=T(80,330,'EXAMPLE',34,GOLD,700,'JetBrains Mono',anchor='start')
        o+=chatwin(60,380,960,1180)
        k=wrap(ask,30); typed=ask[:int(len(ask)*cl(P(lt,0.3,2.0)))]
        tl=wrap(typed,30) if typed else []
        bh=60+len(k)*52
        if typed:
            o+=f'<rect x="200" y="470" width="780" height="{bh}" rx="26" fill="{GOLD}"/>'+''.join(T(950,520+i*52,l,40,BG,700,anchor='end') for i,l in enumerate(tl))
        y=470+bh+90
        if lt>2.2:
            o+=T(110,y,'AI',28,GOLD,700,'JetBrains Mono',anchor='start'); y+=70
            for i,a in enumerate(ans):
                p=P(lt,2.4+i*0.7,2.8+i*0.7)
                if p>0:
                    o+=f'<g {pop(p)}>'+wl(110,y,a,34,44,CREAM,600,1.25)+'</g>'
                y+=nlines(a,34)*44*1.25+34
        if lt>2.4+3*0.7: o+=check_item(130,1480,'Now try it yourself',P(lt,2.4+2.1,2.9+2.1))
        return o
    st=sh['do']; vo_do=f"Do it now. One: {st[0]} Two: {st[1]} Three: {st[2]}"
    marks=[vo_do.index('One:'),vo_do.index('Two:'),vo_do.index('Three:')]
    def s_do(lt,L):
        o=T(80,330,'DO IT NOW',34,GOLD,700,'JetBrains Mono',anchor='start')+T(1000,330,'about 15 minutes',30,GREY,500,anchor='end')
        for i,s in enumerate(st):
            t0=(L-0.8)*marks[i]/len(vo_do)+0.2; p=P(lt,t0,t0+0.5)
            if p<=0: continue
            y=400+i*400
            o+=f'<g opacity="{ease(p):.2f}" transform="translate({(1-ease(p))*120:.0f},0)">'+card(60,y,960,360)
            o+=f'<circle cx="150" cy="{y+90}" r="50" fill="{GOLD}"/>'+T(150,y+110,str(i+1),56,BG,800,'Inter Display')
            o+=wl(230,y+100,s,27,50,CREAM,600,1.25)+'</g>'
        return o
    def s_watch(lt,L):
        a=ease(P(lt,0,0.5)); o=f'<g opacity="{a:.2f}"><path d="M540 420 L700 700 L380 700 Z" fill="none" stroke="{RED}" stroke-width="16" stroke-linejoin="round"/>'+T(540,670,'!',150,RED,800,'Inter Display')+'</g>'
        o+=T(W/2,830,'WATCH OUT',40,RED,700,'JetBrains Mono',op=a)
        o+=wl(W/2,960,sh['watch'],24,66,CREAM,700,1.2,'middle',ease(P(lt,0.3,0.9)),'Inter Display')
        return o
    def s_go(lt,L):
        o=T(W/2,420,'YOUR TURN',130,GOLD,800,'Inter Display',op=ease(P(lt,0,0.5)))
        o+=wl(W/2,560,sh['task'],26,56,CREAM,700,1.25,'middle',ease(P(lt,0.4,1.0)))
        y=560+nlines(sh['task'],26)*56*1.25+60; b=ease(P(lt,1.2,1.8))
        o+=card(90,y,900,60+nlines(sh['proof'],34)*44*1.25+50,op=b)+T(130,y+60,'SAVE FOR YOUR PORTFOLIO',26,GOLD,700,'JetBrains Mono',anchor='start',op=b)
        o+=wl(130,y+120,sh['proof'],34,44,CREAM,600,1.25,op=b)
        c=ease(P(lt,2.2,2.8)); bob=math.sin(lt*5)*10
        o+=f'<g opacity="{c:.2f}"><rect x="140" y="1340" width="800" height="104" rx="52" fill="{GOLD}"/>'+T(540,1408,"Copy today's prompt below",42,BG,800)
        o+=line((540,1480+bob),(540,1580+bob),c=GOLD,w=10)+f'<path d="M500 {1560+bob} L540 {1610+bob} L580 {1560+bob}" fill="none" stroke="{GOLD}" stroke-width="10" stroke-linecap="round"/></g>'
        return o
    voice=NV if n%2 else MV; R='+4%'
    spoken=title.replace('&','and').replace(':',',')
    V=lambda s:(voice,R,'+0Hz',s)
    beats=[dict(say=V(f"Day {n}. {spoken}."),draw=s_title,min=4.2,post=0.9),
           dict(say=V(vo_win),draw=s_win,post=0.8),
           dict(say=V("Here's an example."),draw=s_demo,min=6.8,post=0.3),
           dict(say=V(vo_do),draw=s_do,post=1.0),
           dict(say=V(f"Watch out. {sh['watch']}"),draw=s_watch,post=0.8),
           dict(say=V(f"Your turn. {sh['task']} Copy today's prompt below this video, then mark the day complete."),draw=s_go,post=1.6,min=6)]
    return beats

def render(lid,beats,ow=720):
    work=f'lv/{lid}'; os.makedirs(work,exist_ok=True)
    t=0.0; tl=[]
    for i,b in enumerate(beats):
        v,r,p,txt=b['say']; dd=tts(txt,v,r,p,f'{work}/{i:02d}')
        pre=b.get('pre',0.3); L=max(b.get('min',0),pre+dd+b.get('post',0.5))
        tl.append(dict(start=t,len=L,vo=t+pre,draw=b['draw'])); t+=L
    total=t
    def frame(tt):
        k=max([i for i in range(len(tl)) if tl[i]['start']<=tt] or [0]); b=tl[k]
        o=base()+b['draw'](tt-b['start'],b['len'])+foot()
        for c in [x['start'] for x in tl[1:]]:
            f=1-abs(tt-c)/0.22
            if f>0: o+=f'<rect width="{W}" height="{H}" fill="{BG}" opacity="{cl(f):.2f}"/>'
        return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">{o}</svg>'
    cairosvg.svg2png(bytestring=frame(2.0).encode(),write_to=f'{work}/poster.png',output_width=540)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'{work}/poster.png','-q:v','5',f'{OUTDIR}/{lid}.jpg'],check=True)
    ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate','15','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','28','-preset','medium',f'{work}/silent.mp4'],stdin=subprocess.PIPE)
    for i in range(int(total*15)): ff.stdin.write(cairosvg.svg2png(bytestring=frame(i/15).encode(),output_width=ow))
    ff.stdin.close(); ff.wait()
    music(f'{work}/music.wav',total,[[48,55,60,64],[45,52,57,60],[41,53,57,60],[43,55,59,62]],0.5)
    ins=[];fl=[];labs=[]
    for i,b in enumerate(tl):
        ins+=['-i',f'{work}/{i:02d}.wav']; ms=int(b['vo']*1000)
        fl.append(f'[{i}:a]aformat=sample_rates=44100:channel_layouts=stereo,adelay={ms}|{ms},volume=1.6[v{i}]'); labs.append(f'[v{i}]')
    m=len(labs); ins+=['-i',f'{work}/music.wav']
    fc=';'.join(fl)+f';{"".join(labs)}amix=inputs={m}:normalize=0,apad=whole_dur={total},asplit[a1][a2];[{m}:a]aformat=sample_rates=44100:channel_layouts=stereo,volume=0.09[mu];[mu][a2]sidechaincompress=threshold=0.05:ratio=6:attack=20:release=400[md];[md][a1]amix=inputs=2:normalize=0,alimiter=limit=0.95,atrim=0:{total}[out]'
    subprocess.run(['ffmpeg','-y','-loglevel','error']+ins+['-filter_complex',fc,'-map','[out]','-c:a','aac','-b:a','96k',f'{work}/mix.m4a'],check=True)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'{work}/silent.mp4','-i',f'{work}/mix.m4a','-c','copy','-shortest','-movflags','+faststart',f'{OUTDIR}/{lid}.mp4'],check=True)
    return total

if __name__=='__main__':
    L=lessons(); args=sys.argv[1:]
    if args and args[0]=='stills':
        lid=args[1]; x=[l for l in L if l[0]==lid][0]; beats=make(*x)
        # quick stills: one per scene at mid-point, no audio
        for i,b in enumerate(beats):
            for frac in (0.85,):
                svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">{base()}{b["draw"](frac*7,7.5)}{foot()}</svg>'
                cairosvg.svg2png(bytestring=svg.encode(),write_to=f'lvs_{lid}_{i}.png',output_width=300)
        sys.exit()
    w,nw=int(args[0]),int(args[1]); mine=[l for i,l in enumerate(L) if i%nw==w]
    for x in mine:
        if os.path.exists(f'{OUTDIR}/{x[0]}.mp4') and '--force' not in args: continue
        tt=render(x[0],make(*x)); print(x[0],round(tt,1),flush=True)
