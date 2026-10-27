import sys,os,glob,json
from playwright.sync_api import sync_playwright
R=os.path.abspath('.');pages=sys.argv[1:] or ['index.html']
J="""()=>{const o={ov:document.documentElement.scrollWidth-innerWidth,small:[],tap:[],sec:[],imgs:[]};
for(const e of document.querySelectorAll('body *')){const t=[...e.childNodes].some(n=>n.nodeType==3&&n.textContent.trim());if(!t)continue;const cs=getComputedStyle(e);if(cs.display=='none'||e.offsetWidth==0)continue;if(parseFloat(cs.fontSize)<15.99)o.small.push(e.tagName+'.'+e.className+':'+cs.fontSize)}
for(const e of document.querySelectorAll('a,button')){const r=e.getBoundingClientRect();if(r.width==0)continue;if(r.height<43.5||r.width<43.5)o.tap.push((e.textContent.trim()||e.className).slice(0,25)+' '+Math.round(r.width)+'x'+Math.round(r.height))}
document.querySelectorAll('main>section').forEach(s=>o.sec.push(Math.round(s.getBoundingClientRect().height/innerHeight*100)));
for(const i of document.images){if(i.naturalWidth&&Math.abs(i.naturalWidth/i.naturalHeight-i.width/i.height)<0.01&&0)o.imgs.push(i.src);}
const q=x=>document.querySelector(x).getBoundingClientRect(),nv=document.getElementById('nav'),bg=document.querySelector('.burger');o.hdr=[];
if(getComputedStyle(bg).display!='none'){if(innerWidth>980)o.hdr.push('burger>980')}else{if(innerWidth<=980)o.hdr.push('menu complet<=980');const B=q('.brand'),N=q('.nav'),C=q('.call');if(B.right>N.left+0.5||N.right>C.left+0.5||C.right>innerWidth||N.height>60)o.hdr.push('chevauchement nav '+Math.round(B.right)+'/'+Math.round(N.left)+'-'+Math.round(N.right)+'/'+Math.round(C.left)+' h'+Math.round(N.height))}
o.h1=document.querySelectorAll('h1').length;o.title=document.title.length;return o}"""
with sync_playwright() as p:
    b=p.chromium.launch()
    for pg in pages:
        for w,h in [(360,740),(414,800),(768,1024),(821,800),(980,800),(981,800),(1280,800),(1920,1000)]:
            c=b.new_page(viewport={'width':w,'height':h});c.goto('file://'+R+'/'+pg);c.wait_for_timeout(300)
            o=c.evaluate(J);bad=[]
            if o['ov']>0:bad.append('débordement %d'%o['ov'])
            if o['small']:bad.append('texte<16 '+str(sorted(set(o['small']))[:4]))
            if o['tap']:bad.append('cibles<44 '+str(o['tap'][:4]))
            if o['hdr']:bad.append(o['hdr'])
            if o['h1']!=1:bad.append('h1=%d'%o['h1'])
            print(pg,w,'OK' if not bad else bad,'sections%',o['sec'])
            c.close()
    b.close()
for f in glob.glob('images/*'):
    k=os.path.getsize(f)/1024
    if k>250:print('IMG>250Ko',f,round(k))
print('poids images',round(sum(os.path.getsize(f) for f in glob.glob('images/*'))/1024),'Ko')
