import subprocess, os, json
P=os.environ['HTTPS_PROXY']
N='en-NG-EzinneNeural'; M='en-NG-AbeoNeural'
lines=[
 ('01',0.3, N,'+8%','+0Hz',"Meet Tunde. Forty-seven emails. Three reports. And it's already nine p.m."),
 ('02',5.6, N,'+8%','+0Hz',"Sound familiar?"),
 ('03',7.0, M,'+5%','+8Hz',"Guy, why not just use AI?"),
 ('04',9.0, M,'+0%','-6Hz',"Abeg, I tried it. The answers were too generic."),
 ('05',11.3,N,'+8%','+0Hz',"So Tunde tried the 30-Day AI Sprint from AI Made Simple. Thirty minutes a day, with lessons written for his field."),
 ('06',17.6,N,'+8%','+0Hz',"From Day 1, he used AI on real work. Reports in twenty minutes. Emails answered. Proposals drafted. Receipts turned into spreadsheets."),
 ('07',26.2,N,'+8%','+0Hz',"Same job. Less stress. More done."),
 ('08',28.2,M,'+0%','-12Hz',"Tunde! This report is excellent!"),
 ('09',31.8,N,'+8%','+0Hz',"Use AI to be better at your job. The 30-Day AI Sprint is ten thousand naira for the full thirty days. Day one is free, and you get a seven-day money-back guarantee. Visit aimadesimpleschool.com, or message us on WhatsApp today."),
]
out=[]
for k,t,v,r,p,txt in lines:
    f=f'vo/{k}.mp3'
    subprocess.run(['edge-tts','--proxy',P,'--voice',v,f'--rate={r}',f'--pitch={p}','--text',txt,'--write-media',f],check=True,env=dict(os.environ,SSL_CERT_FILE='/root/.ccr/ca-bundle.crt'),capture_output=True)
    d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f],capture_output=True,text=True).stdout)
    out.append((k,t,d)); print(k,t,round(d,2),'ends',round(t+d,2))
json.dump(out,open('vo/timing.json','w'))
