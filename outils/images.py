import sys
from PIL import Image
S='/mnt/user-data/uploads/Maquettes/Images/Paysagiste/'
D='/home/claude/au-coeur-de-l-arbre/images/'
M={'hero-chene':'imgi_1_hero-elagage-chene','taille-haies':'imgi_1_taille-haies','espace-vert':'imgi_4_creation-espace-vert','abattage-demontage':'Abattage par démontage','allee-paves':'alléé pavés carrelage extérieure','bois-chauffage':'Bois de chauffage','allee-dallee':'chantier allée dallée','terrasse-bois':'chantier terrasse en bois','conception':'conception chantier','equipe-elagage':'Équipe et matériel elagage','etetage':'Étêtage taille de réduction','maconnerie':'maçonerie paysagère','elagage-urgence':'photo de chantier élégage urgence','robot-tonte':'robot tonte de pelouse'}
for k,v in M.items():
    im=Image.open(S+v+'.jpg').convert('RGB');w,h=im.size
    W=1600 if k=='hero-chene' else 1000
    if w>W: im=im.resize((W,round(h*W/w)),Image.LANCZOS)
    im.save(D+k+'.jpg',quality=80,optimize=True,progressive=True)
    print(k,im.size,round(__import__('os').path.getsize(D+k+'.jpg')/1024),'Ko')
sheet=Image.new('RGB',(1200,600),'white')
for i,k in enumerate(['terrasse-bois','allee-dallee','maconnerie','robot-tonte','etetage','hero-chene']):
    t=Image.open(D+k+'.jpg');t.thumbnail((400,300));sheet.paste(t,((i%3)*400,(i//3)*300))
sheet.save('/tmp/claude-0/s/sheet.jpg',quality=70)
