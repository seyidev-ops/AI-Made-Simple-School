import os, sys, math, json, subprocess, textwrap, numpy as np, wave, cairosvg
from video import cl,ease,back,P,T,seg,line,stick,bubble,check_item,laptop,papers,sweat,clock,_cap,W,H,FPS,BG,GOLD,CREAM,GREY,CARD,RED,E
PROXY=os.environ.get('HTTPS_PROXY','')
NV='en-NG-EzinneNeural'; MV='en-NG-AbeoNeural'
def wrap(s,n): return textwrap.wrap(s,n)
def cap(lines,op,y=300,size=68,gold=()): return _cap(lines,op,y,size,gold) if op>0 else ''
def base():
    return (f'<rect width="{W}" height="{H}" fill="{BG}"/><defs><pattern id="g" width="60" height="60" patternUnits="userSpaceOnUse"><path d="M60 0H0V60" fill="none" stroke="{GOLD}" stroke-opacity="0.06"/></pattern>'
      f'<radialGradient id="r" cx="0.8" cy="0.05" r="0.8"><stop offset="0" stop-color="{GOLD}" stop-opacity="0.18"/><stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></radialGradient></defs>'
      f'<rect width="{W}" height="{H}" fill="url(#g)"/><rect width="{W}" height="{H}" fill="url(#r)"/><rect width="{W}" height="8" fill="{GOLD}"/>')
def foot(): return T(80,H-90,'AI Made Simple',40,GOLD,800,'Inter Display',anchor='start')+T(W-80,H-90,'aimadesimpleschool.com',30,GREY,500,anchor='end')
def card(x,y,w,h,op=1,stroke=GOLD,fill=CARD,r=28): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-opacity="{0.45*op:.2f}" stroke-width="3" opacity="{op:.2f}"/>'
def textblock(x,y,s,n,size,fill=CREAM,w=500,lh=1.3,op=1,anchor='start'):
    return ''.join(T(x,y+i*size*lh,l,size,fill,w,anchor=anchor,op=op) for i,l in enumerate(wrap(s,n)))
def pop(p): return f'opacity="{cl(p*2):.2f}"'
def cta(lt,head,sub,pills,button,foot2='or WhatsApp 0703 313 4979',tag='// 30-DAY PROFESSIONAL AI SPRINT'):
    a=ease(P(lt,0,0.6)); o=T(W/2,330,tag,32,GOLD,700,'JetBrains Mono',op=a)
    for i,l in enumerate(head): o+=T(W/2,520+i*130,l,120,GOLD if i==len(head)-1 else CREAM,800,'Inter Display',op=ease(P(lt,0.2+i*0.2,0.8+i*0.2)))
    y0=520+len(head)*130+80
    b=ease(P(lt,1.4,2)); o+=T(W/2,y0+60,'₦10,000',180,GOLD,800,'Inter Display',op=b)+T(W/2,y0+130,sub,40,CREAM,500,op=b)
    c=ease(P(lt,2.2,2.8)); tw=[len(p)*17+70 for p in pills]; x=(W-sum(tw)-20*(len(pills)-1))/2
    for p,wd in zip(pills,tw):
        o+=f'<g opacity="{c:.2f}"><rect x="{x}" y="{y0+190}" width="{wd}" height="70" rx="35" fill="none" stroke="{GOLD}" stroke-width="3"/>'+T(x+wd/2,y0+236,p,32,CREAM,600)+'</g>'; x+=wd+20
    d=ease(P(lt,3,3.6)); pulse=1+0.03*math.sin(lt*6); yb=y0+340
    o+=f'<g opacity="{d:.2f}" transform="translate(540,{yb+52}) scale({pulse:.3f}) translate(-540,{-(yb+52)})"><rect x="140" y="{yb}" width="800" height="104" rx="52" fill="{GOLD}"/>'+T(540,yb+68,button,46,BG,800)+'</g>'
    o+=T(W/2,yb+190,foot2,42,CREAM,600,op=d)
    return o

def tts(text,voice,rate,pitch,f):
    if not os.path.exists(f+'.wav'):
        subprocess.run(['edge-tts','--proxy',PROXY,'--voice',voice,f'--rate={rate}',f'--pitch={pitch}','--text',text,'--write-media',f+'.mp3'],check=True,capture_output=True,env=dict(os.environ,SSL_CERT_FILE='/root/.ccr/ca-bundle.crt'))
        subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f+'.mp3','-af','silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse','-ar','44100',f+'.wav'],check=True)
    return float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f+'.wav'],capture_output=True,text=True).stdout)

def music(path,dur,prog,bpm_step=0.5,bar=4.0):
    sr=44100; t=np.arange(int(sr*dur))/sr; hz=lambda n:440*2**((n-69)/12); x=np.zeros_like(t)
    for k in range(int(dur/bar)+1):
        a=k*bar; idx=(t>=a)&(t<a+bar+0.4); tt=t[idx]-a; ch=prog[k%len(prog)]
        env=np.minimum(1,tt/0.8)*np.minimum(1,np.maximum(0,(bar+0.4-tt)/0.8))
        for n in ch: f=hz(n); x[idx]+=env*(np.sin(2*np.pi*f*tt)+0.25*np.sin(2*np.pi*2*f*tt))*0.18
        nb=int(bar/bpm_step)
        for b in range(nb):
            bt=a+b*bpm_step; j=(t>=bt)&(t<bt+0.4); u=t[j]-bt; n=ch[[3,2,3,1,3,2,3,0][b%8]]+12
            x[j]+=0.12*np.exp(-u*9)*np.sin(2*np.pi*hz(n)*u)
    x*=np.minimum(1,t/1.5)*np.minimum(1,(dur-t)/2.5); x=x/np.max(np.abs(x))*0.9
    w=wave.open(path,'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((x*32767).astype('<i2').tobytes()); w.close()

def build(name,beats,prog,step=0.5,stills=None):
    os.makedirs(f'{name}_vo',exist_ok=True)
    t=0.0; tl=[]
    for i,b in enumerate(beats):
        d=0
        if b.get('say'):
            v,r,p,txt=b['say']; d=tts(txt,v,r,p,f'{name}_vo/{i:02d}')
        pre=b.get('pre',0.3); L=max(b.get('min',0),pre+d+b.get('post',0.5))
        tl.append(dict(start=t,len=L,vo=(t+pre) if d else None,scene=b.get('scene',i),draw=b['draw'])); t+=L
    total=t; print(name,'total',round(total,1))
    bounds=[tl[i]['start'] for i in range(1,len(tl)) if tl[i]['scene']!=tl[i-1]['scene']]
    def frame(tt):
        k=max(i for i in range(len(tl)) if tl[i]['start']<=tt or i==0)
        b=tl[k]; o=base()+b['draw'](tt-b['start'],b['len'])+foot()
        for c in bounds:
            f=1-abs(tt-c)/0.25
            if f>0: o+=f'<rect width="{W}" height="{H}" fill="{BG}" opacity="{cl(f):.2f}"/>'
        return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">{o}</svg>'
    if stills is not None:
        for s in stills: cairosvg.svg2png(bytestring=frame(s*total).encode(),write_to=f'{name}_still_{s}.png',output_width=360)
        return
    ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate',str(FPS),'-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','20','-preset','medium',f'{name}_silent.mp4'],stdin=subprocess.PIPE)
    for i in range(int(total*FPS)): ff.stdin.write(cairosvg.svg2png(bytestring=frame(i/FPS).encode()))
    ff.stdin.close(); ff.wait()
    music(f'{name}_vo/music.wav',total,prog,step)
    ins=[];fl=[];labs=[]
    for i,b in enumerate(tl):
        if b['vo'] is None: continue
        ins+=['-i',f'{name}_vo/{i:02d}.wav']; n=len(labs); ms=int(b['vo']*1000)
        fl.append(f'[{n}:a]aformat=sample_rates=44100:channel_layouts=stereo,adelay={ms}|{ms},volume=1.6[v{n}]'); labs.append(f'[v{n}]')
    m=len(labs); ins+=['-i',f'{name}_vo/music.wav']
    fc=';'.join(fl)+f';{"".join(labs)}amix=inputs={m}:normalize=0,apad=whole_dur={total},asplit[a1][a2];[{m}:a]aformat=sample_rates=44100:channel_layouts=stereo,volume=0.13[mu];[mu][a2]sidechaincompress=threshold=0.05:ratio=6:attack=20:release=400[md];[md][a1]amix=inputs=2:normalize=0,alimiter=limit=0.95,atrim=0:{total}[out]'
    subprocess.run(['ffmpeg','-y','-loglevel','error']+ins+['-filter_complex',fc,'-map','[out]','-c:a','aac','-b:a','160k',f'{name}_vo/mix.m4a'],check=True)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'{name}_silent.mp4','-i',f'{name}_vo/mix.m4a','-c','copy','-shortest','-movflags','+faststart',f'out/{name}.mp4'],check=True)
    print('wrote',name)
