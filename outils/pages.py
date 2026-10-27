import re
s=open('index.html',encoding='utf-8').read()
HDR=re.search(r'<header class="hdr">.*?</header>',s,re.S).group(0)
FTR=re.search(r'<footer class="ftr">.*?</footer>',s,re.S).group(0)
FTR=FTR.replace('<a href="contact.html">Contact</a>','<a href="entreprise.html">L’entreprise</a>\n      <a href="contact.html">Contact</a>')
HEAD=re.search(r'<link rel="icon".*?<link rel="stylesheet" href="css/style.css">',s,re.S).group(0)
def hdr(cur):
    h=HDR.replace(' aria-current="page"','')
    return h.replace('<a href="%s">'%cur,'<a href="%s" aria-current="page">'%cur)
def ic(d):return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>'%d
RING=ic('<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1"/>')
TREE=ic('<path d="M12 21V9M12 9l-5-4M12 12l5-4M12 15l-4-3"/><circle cx="12" cy="4" r="1.5"/>')
AXE=ic('<path d="M4 20l8-8M14 4l6 6-3 3-6-6zM12 12l-2 2"/>')
UP=ic('<path d="M12 3v18M7 8l5-5 5 5M5 21h14"/>')
BUG=ic('<ellipse cx="12" cy="14" rx="4" ry="6"/><path d="M12 8V4M8 11L4 9M16 11l4-2M8 16l-4 1M16 16l4 1"/>')
LEAF=ic('<path d="M5 19C5 10 11 5 20 5c0 9-5 15-14 15M5 19l8-8"/>')
SAW=ic('<path d="M3 17h18M3 17l2-4 2 4 2-4 2 4 2-4 2 4 2-4 2 4M7 8h10"/>')
EYE=ic('<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>')
GRASS=ic('<path d="M4 20c0-5 2-9 4-12M12 20c0-6 0-10 0-14M20 20c0-5-2-9-4-12"/>')
FENCE=ic('<path d="M5 21V8l2-3 2 3v13M13 21V8l2-3 2 3v13M3 12h18M3 17h18"/>')
SUN=ic('<circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/>')
HOME=ic('<path d="M3 11l9-8 9 8M5 10v10h14V10"/>')
BLD=ic('<path d="M4 21V5l8-2v18M12 9h8v12M7 9h2M7 13h2M7 17h2M15 13h2M15 17h2"/>')
FLAG=ic('<path d="M5 21V4M5 4h12l-2 4 2 4H5"/>')
PHONE=ic('<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>')
def page(fn,cur,title,desc,body):
    h='<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n<title>%s</title>\n<meta name="description" content="%s">\n<meta name="robots" content="noindex, nofollow">\n%s\n</head>\n<body>\n%s\n\n<main>\n%s\n</main>\n\n%s\n<script src="js/main.js" defer></script>\n</body>\n</html>\n'%(title,desc,HEAD,hdr(cur),body,FTR)
    open(fn,'w',encoding='utf-8').write(h)
CALL='<a class="btn btn-rope" href="tel:+33663204922">Appeler le 06 63 20 49 22</a>'

# ---------- ARBORICULTURE ----------
page('arboriculture.html','arboriculture.html','Arboriculture à Étampes : élagage, abattage, dessouchage | Au Cœur de l’Arbre','Élagage, abattage, dessouchage, haubanage et interventions spécifiques à Étampes (91) avec Au Cœur de l’Arbre, arboristes grimpeurs. Devis gratuit.','''<section class="sec phead dark rings" aria-labelledby="h1">
  <div class="wrap">
    <div>
      <span class="eyebrow">Arboriculture · Étampes (91)</span>
      <h1 id="h1">Des arbres bien taillés, bien tenus, bien abattus quand il le faut</h1>
      <p class="lead">Les arboristes grimpeurs d’Au Cœur de l’Arbre interviennent à Étampes et dans l’Essonne : élagage, abattage, dessouchage, haubanage et gestion des rémanents.</p>
      <div class="actions"><a class="btn btn-rope" href="contact.html">Demander un devis gratuit</a><a class="btn btn-line" href="tel:+33663204922">Appeler le 06 63 20 49 22</a></div>
    </div>
    <div class="mos3">
      <img src="images/hero-chene.jpg" width="1376" height="768" alt="Arboriste grimpeur dans la ramure d’un grand chêne (image d’illustration)">
      <img src="images/equipe-elagage.jpg" width="800" height="436" alt="Équipe et matériel d’élagage sur un chantier (image d’illustration)">
      <img src="images/elagage-urgence.jpg" width="800" height="436" alt="Chantier d’élagage en urgence (image d’illustration)">
    </div>
  </div>
</section>

<section class="sec s-cream" aria-labelledby="h-el">
  <div class="wrap">
    <div class="row">
      <img src="images/etetage.jpg" width="800" height="436" alt="Arbre étêté après une taille de réduction (image d’illustration)" loading="lazy">
      <div>
        <span class="eyebrow">Élagage</span>
        <h2 id="h-el">Tailler pour garder l’arbre en bonne santé</h2>
        <p>Taille de réduction, entretien de la ramure, arbre trop proche d’une maison ou d’une ligne : le grimpeur accède à la cime sans abîmer votre terrain.</p>
        <ul class="tick"><li>Conseil sur le geste de taille adapté à l’arbre</li><li>Travail en hauteur par des arboristes grimpeurs</li><li>Branches et rémanents pris en charge</li></ul>
      </div>
    </div>
    <div class="row rev">
      <img src="images/abattage-demontage.jpg" width="800" height="436" alt="Abattage d’un arbre par démontage (image d’illustration)" loading="lazy">
      <div>
        <span class="eyebrow">Abattage</span>
        <h2>Démonter l’arbre morceau par morceau</h2>
        <p>Quand un arbre ne peut plus être conservé ou que l’espace est trop étroit pour le faire tomber, l’abattage par démontage permet de le descendre en sécurité.</p>
        <ul class="tick"><li>Démontage depuis la cime, par sections</li><li>Dessouchage possible dans la foulée</li><li>Gestion des rémanents</li></ul>
      </div>
    </div>
  </div>
</section>

<section class="sec s-sage" aria-labelledby="h-more">
  <div class="wrap">
    <div class="head"><span class="eyebrow">Après la coupe, et pour les cas délicats</span><h2 id="h-more">Dessouchage, haubanage, rémanents</h2></div>
    <div class="cards3">
      <article class="card c-leaf">'''+RING+'''<h3>Dessouchage</h3><p>Retirer la souche pour récupérer le terrain et replanter ou aménager.</p></article>
      <article class="card c-rope">'''+UP+'''<h3>Haubanage et travaux spéciaux</h3><p>Soutenir un arbre fragile ou intervenir là où l’accès est difficile.</p></article>
      <article class="card c-bark">'''+SAW+'''<h3>Gestion des rémanents</h3><p>Branches, bois et copeaux évacués ou valorisés : le chantier est laissé net.</p></article>
    </div>
    <div class="row rev" style="margin-top:2.6rem">
      <img src="images/bois-chauffage.jpg" width="800" height="446" alt="Bois coupé et empilé après un chantier (image d’illustration)" loading="lazy">
      <div><h3 style="margin-bottom:.6rem">Des chantiers propres, du bois bien rangé</h3><p>L’équipe s’engage à vous accompagner du premier conseil jusqu’au suivi, et à respecter vos demandes comme les délais convenus.</p></div>
    </div>
  </div>
</section>

<section class="sec dark rings" aria-labelledby="h-spe">
  <div class="wrap">
    <div class="head"><span class="eyebrow">Interventions spécifiques</span><h2 id="h-spe">Chenilles, frelons, expertise</h2><p>Au-delà de la taille, l’équipe intervient sur des situations particulières. Décrivez la vôtre, elle vous indique la bonne approche.</p></div>
    <div class="cards4">
      <article class="card c-forest">'''+BUG+'''<h3>Chenilles processionnaires</h3><p>Une intervention adaptée selon la situation de vos arbres.</p></article>
      <article class="card c-forest">'''+LEAF+'''<h3>Lutte biologique</h3><p>Des solutions respectueuses du végétal et de son environnement.</p></article>
      <article class="card c-forest">'''+EYE+'''<h3>Travaux d’expertise</h3><p>Un regard de professionnel sur l’état et l’avenir de vos arbres.</p></article>
      <article class="card c-forest">'''+SAW+'''<h3>Frelons et scierie mobile</h3><p>Deux sujets à aborder directement avec l’équipe pour votre chantier.</p></article>
    </div>
    <div class="band b-rope"><div><h2>Un arbre vous inquiète ?</h2><p>Racontez votre situation, le devis est gratuit.</p></div><div class="actions"><a class="btn btn-green" href="contact.html">Écrire à l’équipe</a></div></div>
  </div>
</section>''')

# ---------- PAYSAGE ----------
page('paysage.html','paysage.html','Travaux paysagers à Étampes : terrasses, clôtures, pelouse | Au Cœur de l’Arbre','Pose de terrasses et clôtures, tonte de pelouse, débroussaillage, création et entretien d’espaces verts à Étampes (91) avec Au Cœur de l’Arbre.','''<section class="sec phead light" aria-labelledby="h1">
  <div class="wrap">
    <div>
      <span class="eyebrow">Travaux paysagers · Essonne</span>
      <h1 id="h1">Un espace vert à la hauteur de vos attentes</h1>
      <p class="lead">Terrasses, clôtures, pelouse, débroussaillage, création et entretien : les paysagistes d’Au Cœur de l’Arbre transforment votre extérieur en véritable havre de paix.</p>
      <div class="actions"><a class="btn btn-green" href="contact.html">Demander un devis gratuit</a><a class="btn btn-rope" href="tel:+33663204922">Appeler le 06 63 20 49 22</a></div>
    </div>
    <div class="fan">
      <img src="images/allee-paves.jpg" width="800" height="436" alt="Allée en pavés de pierre dans un jardin (image d’illustration)">
      <img src="images/terrasse-bois.jpg" width="800" height="436" alt="Pose d’une terrasse en bois devant une maison en pierre (image d’illustration)">
      <img src="images/maconnerie.jpg" width="800" height="436" alt="Muret de pierre et escalier dans un jardin (image d’illustration)">
    </div>
  </div>
</section>

<section class="sec s-cream" aria-labelledby="h-serv">
  <div class="wrap">
    <div class="head"><span class="eyebrow">Les prestations</span><h2 id="h-serv">Quatre façons de soigner votre jardin</h2></div>
    <div class="cards4">
      <article class="card c-white">'''+FENCE+'''<h3>Terrasses et clôtures</h3><p>Pose de terrasses en bois et de clôtures pour délimiter et prolonger votre maison.</p></article>
      <article class="card c-white">'''+GRASS+'''<h3>Pelouse et gazon</h3><p>Tonte régulière ou ponctuelle pour une pelouse nette toute la saison.</p></article>
      <article class="card c-white">'''+SUN+'''<h3>Débroussaillage</h3><p>Reprendre un terrain envahi et rendre l’espace à nouveau praticable.</p></article>
      <article class="card c-white">'''+LEAF+'''<h3>Espaces verts</h3><p>Création et entretien : plantations, massifs et suivi dans la durée.</p></article>
    </div>
    <div class="row" style="margin-top:3rem">
      <img src="images/terrasse-bois.jpg" width="800" height="436" alt="Terrasse en bois en cours de pose (image d’illustration)" loading="lazy">
      <div><span class="eyebrow">Terrasse bois</span><h2>Le bois, côté jardin</h2><p>Une terrasse bien posée prolonge le salon dehors. L’équipe vous conseille sur l’implantation et suit le chantier.</p></div>
    </div>
  </div>
</section>

<section class="sec s-sand" aria-labelledby="h-gal">
  <div class="wrap">
    <div class="row rev">
      <img src="images/espace-vert.jpg" width="800" height="436" alt="Espace vert créé autour d’une maison (image d’illustration)" loading="lazy">
      <div><span class="eyebrow">Création et entretien</span><h2 id="h-gal">Du terrain nu au jardin vivant</h2><p>Pelouse, plantations, ensemble paysager : la même équipe crée l’espace vert puis l’entretient, pour un résultat qui dure.</p><ul class="tick"><li>Conseil avant le chantier</li><li>Suivi après les travaux</li><li>Respect du végétal existant</li></ul></div>
    </div>
    <div class="gal3" aria-label="Ambiances de jardin (images d’illustration)">
      <img src="images/allee-dallee.jpg" width="800" height="436" alt="Allée dallée entre pelouse et massifs (image d’illustration)" loading="lazy">
      <img src="images/robot-tonte.jpg" width="800" height="436" alt="Robot de tonte sur une pelouse entretenue (image d’illustration)" loading="lazy">
      <img src="images/taille-haies.jpg" width="800" height="598" alt="Haie taillée au cordeau (image d’illustration)" loading="lazy">
    </div>
    <div class="band b-leaf"><div><h2>Parlons de votre jardin</h2><p>Un appel suffit pour décrire votre projet.</p></div><div class="actions"><a class="btn btn-rope" href="tel:+33663204922">Appeler maintenant</a><a class="btn btn-line" href="contact.html">Devis en ligne</a></div></div>
  </div>
</section>''')

# ---------- ENTREPRISE ----------
page('entreprise.html','entreprise.html','L’entreprise : arboristes et paysagistes depuis 2009 à Étampes | Au Cœur de l’Arbre','Au Cœur de l’Arbre, installée à Étampes (91) depuis 2009 : une équipe d’arboristes grimpeurs et de paysagistes pour particuliers, professionnels et collectivités.','''<section class="sec dark rings" aria-labelledby="h1">
  <div class="wrap story">
    <img class="badge" src="images/logo.png" width="141" height="150" alt="Logo Au Cœur de l’Arbre, arboriste grimpeur">
    <div>
      <span class="eyebrow">L’entreprise</span>
      <h1 id="h1">Au Cœur de l’Arbre, installée à Étampes depuis 2009</h1>
      <p style="margin-top:1.2rem">Professionnelle et qualifiée, l’équipe d’arboristes grimpeurs et de paysagistes met son savoir-faire à votre service, du conseil au suivi, pour prendre soin de votre parc arboré et de vos espaces verts tout en respectant l’environnement.</p>
      <p class="sig">Florent Breugnot, dirigeant</p>
      <div class="actions"><a class="btn btn-rope" href="contact.html">Nous contacter</a></div>
    </div>
  </div>
</section>

<section class="sec s-sage" aria-labelledby="h-who">
  <div class="wrap">
    <div class="head"><span class="eyebrow">Nos clients</span><h2 id="h-who">Pour qui travaille l’équipe</h2><p>Les interventions s’adressent aussi bien aux particuliers qu’aux professionnels et aux administrations territoriales.</p></div>
    <div class="cards3">
      <article class="card c-white">'''+HOME+'''<h3>Particuliers</h3><p>Un arbre à tailler, un jardin à créer ou à entretenir : une réponse claire et un devis gratuit.</p></article>
      <article class="card c-white">'''+BLD+'''<h3>Professionnels</h3><p>Des chantiers réguliers ou ponctuels, menés dans les délais prévus.</p></article>
      <article class="card c-white">'''+FLAG+'''<h3>Administrations territoriales</h3><p>Entretien des arbres et des espaces verts publics de l’Essonne.</p></article>
    </div>
    <div class="row rev" style="margin-top:3rem">
      <img src="images/conception.jpg" width="800" height="436" alt="Étude d’un projet d’aménagement sur plan (image d’illustration)" loading="lazy">
      <div><h3 style="margin-bottom:.6rem">Un chantier se prépare</h3><p>Avant de grimper ou de creuser, l’équipe écoute, conseille et cadre le projet avec vous.</p></div>
    </div>
  </div>
</section>

<section class="sec s-cream" aria-labelledby="h-eng">
  <div class="wrap">
    <div class="head"><span class="eyebrow">Nos engagements</span><h2 id="h-eng">Ce que vous pouvez attendre de nous</h2></div>
    <div class="cards3">
      <article class="card c-leaf">'''+LEAF+'''<h3>Respect du végétal</h3><p>Prendre soin de vos arbres en respectant l’environnement.</p></article>
      <article class="card c-rope">'''+PHONE+'''<h3>Disponible et à l’écoute</h3><p>Une équipe qui tient compte de vos demandes et de vos désirs.</p></article>
      <article class="card c-bark">'''+FLAG+'''<h3>Délais respectés</h3><p>Les délais définis ensemble sont ceux du chantier.</p></article>
    </div>
    <div class="band b-bark"><div><h2>Un projet à confier ?</h2><p>Florent Breugnot et son équipe vous répondent.</p></div><div class="actions">'''+CALL+'''</div></div>
  </div>
</section>''')

# ---------- CONTACT ----------
page('contact.html','contact.html','Contact et devis gratuit à Étampes | Au Cœur de l’Arbre','Contactez Au Cœur de l’Arbre à Étampes (91) : appelez le 06 63 20 49 22 ou préparez votre demande de devis gratuit en ligne.','''<section class="sec s-cream" style="padding-top:clamp(2.5rem,6vw,4rem);min-height:min(92svh,900px)" aria-labelledby="h1">
  <div class="wrap">
    <div class="head"><span class="eyebrow">Contact · Étampes (91)</span><h1 id="h1">Parlons de votre projet</h1><p>Décrivez votre besoin en quelques lignes. Vous obtenez un message prêt à envoyer par SMS à l’équipe, ou vous pouvez appeler directement.</p></div>
    <div class="cgrid">
      <form class="form" id="devis" novalidate aria-label="Demande de devis">
        <div class="field"><label for="f-nom">Votre nom</label><input id="f-nom" name="nom" type="text" autocomplete="name" required aria-describedby="e-nom"><span class="msg" id="e-nom" role="alert"></span></div>
        <div class="field"><label for="f-tel">Votre téléphone</label><input id="f-tel" name="tel" type="tel" autocomplete="tel" inputmode="tel" required aria-describedby="e-tel"><span class="msg" id="e-tel" role="alert"></span></div>
        <div class="field"><label for="f-commune">Votre commune</label><input id="f-commune" name="commune" type="text" autocomplete="address-level2" required aria-describedby="e-commune"><span class="msg" id="e-commune" role="alert"></span></div>
        <div class="field"><label for="f-besoin">Votre besoin</label>
          <select id="f-besoin" name="besoin" required aria-describedby="e-besoin">
            <option value="">Choisir dans la liste</option><option>Élagage</option><option>Abattage</option><option>Dessouchage</option><option>Haubanage ou travaux spéciaux</option><option>Chenilles processionnaires ou frelons</option><option>Terrasse ou clôture</option><option>Pelouse, gazon ou débroussaillage</option><option>Création ou entretien d’espaces verts</option><option>Autre demande</option>
          </select><span class="msg" id="e-besoin" role="alert"></span></div>
        <div class="field"><label for="f-msg">Votre message <small>(facultatif)</small></label><textarea id="f-msg" name="message" rows="4"></textarea></div>
        <button class="btn btn-rope" type="submit">Préparer ma demande</button>
        <div class="recap" id="recap" tabindex="-1" hidden>
          <h3>Votre demande est prête</h3>
          <pre></pre>
          <div class="actions"><a class="btn btn-green sms" href="sms:+33663204922">Envoyer par SMS</a><button class="btn btn-line copy" type="button" style="color:var(--forest)">Copier le message</button><a class="btn btn-rope" href="tel:+33663204922">Appeler</a></div>
        </div>
      </form>
      <aside>
        <div class="info"><h3>Appeler l’équipe</h3><p>Mobile</p><a href="tel:+33663204922">06 63 20 49 22</a><p style="margin-top:.6rem">Fixe</p><a href="tel:+33187222211">01 87 22 22 11</a></div>
        <div class="info" style="background:var(--leaf)"><h3>Où nous trouver</h3><p>Étampes, Essonne (91). L’équipe se déplace chez vous pour étudier votre projet.</p></div>
        <div class="info" style="background:var(--bark)"><h3>Devis gratuit</h3><p>Arbres, jardins, espaces verts : décrivez votre besoin, vous recevez des conseils clairs.</p></div>
      </aside>
    </div>
  </div>
</section>''')
