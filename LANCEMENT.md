# Procédure de lancement – arno-franco

Le site est actuellement en **pré-lancement** : il est en ligne, mais **exclu des moteurs de recherche** tant qu'il
contient des informations provisoires. Fichier interne (non publié).

## 1. Prérequis avant de réactiver l'indexation
- [ ] Plus aucune zone jaune `a-completer` visible : `grep -rn 'a-completer"' public/` ne renvoie que la définition CSS
- [ ] Vraies photos intégrées (bandeau, services, réalisations, portrait)
- [x] Mentions légales complètes : adresse, BCE, TVA, administrateur, forme juridique (SRL) faits (06/11/2026)
- [ ] Durée de conservation des données validée (vie-privee.html)
- [ ] Formulaire relié à Formspree et testé (voir la section « Formspree » ci-dessous)
- [ ] Domaine arnofranco.be relié dans Vercel (voir section 2)
- [ ] Plan Vercel adapté à un usage commercial

- [x] Aucun lien vers une page 404 (exploration complète le 06/11/2026) ; les cartes de `/savoir-faire` mènent aux pages de services
- [x] `/a-propos-contact` intégrée ; menu des cinq onglets harmonisé (branche `feat/integration-site`)

## 2. Relier le domaine arnofranco.be (sans encore réactiver l'indexation)
État au 06/11/2026 : le domaine n'est relié à aucun projet Vercel (le projet `arno-franco` n'a que `arno-franco.vercel.app`).
L'état DNS public n'a pas pu être lu depuis l'environnement de Claude (réseau restreint) : à vérifier chez le gestionnaire du domaine.

1. **Identifier le gestionnaire du domaine** (registrar) : recherche sur https://www.dnsbelgium.be/fr/whois → « arnofranco.be ».
   Il faut un accès au compte de ce gestionnaire (Arno ou son prestataire actuel, qui gère aussi la messagerie info@arnofranco.be).
2. **Vercel** → projet **arno-franco** (pas `arno_franco`) → Settings → Domains → *Add* → `arnofranco.be`.
   Accepter l'ajout de `www.arnofranco.be` avec **redirection 308 vers arnofranco.be** (domaine principal : `arnofranco.be`).
   Vérifier que le domaine n'est pas déjà rattaché au projet `arno_franco` (sinon l'en retirer d'abord).
3. **Chez le gestionnaire du domaine**, zone DNS : créer exactement les enregistrements affichés par Vercel, en général
   - `A` pour `@` (arnofranco.be) → l'adresse IP indiquée par Vercel (par ex. `76.76.21.21`) ;
   - `CNAME` pour `www` → la valeur indiquée par Vercel (par ex. `cname.vercel-dns.com`).
   Supprimer seulement les anciens `A`/`AAAA`/`CNAME` de `@` et `www` qui pointent vers l'ancien site.
   ⚠️ **Ne pas toucher aux enregistrements `MX` et `TXT`** (SPF, DKIM…) : ils font fonctionner les e-mails info@arnofranco.be.
4. Attendre que Vercel affiche « Valid Configuration » et que le certificat HTTPS soit émis (quelques minutes à 48 h).
5. Contrôler : https://arnofranco.be affiche le nouveau site, https://www.arnofranco.be redirige vers https://arnofranco.be,
   et le site est toujours en `noindex` à ce stade (normal).

## 3. Basculer vers le domaine et réactiver l'indexation (script, un seul commit)
Quand les prérequis de la section 1 sont remplis ET que https://arnofranco.be répond correctement :
```
python3 outils/lancement.py              # simulation : liste les fichiers qui seront modifiés
python3 outils/lancement.py --appliquer  # applique
```
Le script, testé sur une copie le 06/11/2026 (configuration validée par `vercel build`) :
- remplace `https://arno-franco.vercel.app` par `https://arnofranco.be` partout dans `public/` (canonical, Open Graph, JSON-LD, sitemap, robots.txt) ;
- retire `<meta name="robots" content="noindex">` de toutes les pages **sauf `404.html`** ;
- `vercel.json` : l'en-tête `X-Robots-Tag: noindex` ne s'applique plus qu'aux adresses `*.vercel.app` (aperçus non indexables) ;
  ajoute les redirections permanentes `www.arnofranco.be → arnofranco.be` et `arno-franco.vercel.app → arnofranco.be` ;
- écrit le robots.txt définitif (`Allow: /` + `Sitemap: https://arnofranco.be/sitemap.xml`) et régénère le sitemap (`outils/sitemap.py`).
Il affiche à la fin les contrôles : aucun `vercel.app` restant, `noindex` seulement dans `public/404.html`.
Puis : commit sur la branche de travail, déploiement en production du projet `arno-franco`.

## 4. Après le déploiement
- `curl -sI https://arnofranco.be/ | grep -i x-robots-tag` → aucune ligne
- `curl -sI https://arno-franco-<hash>.vercel.app/` (aperçu) → `x-robots-tag: noindex`
- `curl -sI https://www.arnofranco.be/realisations` → 308 vers `https://arnofranco.be/realisations`
- Le code source de la page d'accueil ne contient plus `noindex` ; https://arnofranco.be/robots.txt affiche la ligne Sitemap
- https://arnofranco.be/sitemap.xml : 16 pages et leurs photos, toutes en `https://arnofranco.be`
- Test des résultats enrichis : https://search.google.com/test/rich-results et https://validator.schema.org (accueil : `WebSite` +
  `HomeAndConstructionBusiness` ; services : `Service` ; pages : fil d'Ariane)
- https://arnofranco.be/llms.txt : liens en `https://arnofranco.be`
- Bing Webmaster Tools (gratuit) : importer le site depuis Search Console et envoyer le sitemap (Bing alimente Copilot et une partie de ChatGPT)
- **Google Search Console** : ajouter une propriété « Domaine » `arnofranco.be` (validation par un enregistrement TXT chez le gestionnaire),
  envoyer `sitemap.xml`, demander l'indexation de la page d'accueil
- **Fiche Google Business Profile** (à créer ou revendiquer par Arno lui-même) : nom « Arno Franco », catégorie
  « Paysagiste » / « Entreprise d'aménagement paysager », adresse Chaufheid 40, 4910 Theux, téléphone 087 71 16 00,
  site https://arnofranco.be, horaires identiques au site (lun–ven 07h30–18h00, sam 07h30–17h00, dim fermé),
  zone desservie Theux, Spa, Jalhay, province de Liège. Ne pas y mettre le GSM. Ajouter de vraies photos de chantiers.
- Vérifier https://arnofranco.be/PROJET.md → doit renvoyer 404

## Robots des moteurs IA (décision à prendre avec Arno avant le lancement)
Aujourd'hui `robots.txt` autorise **tous** les robots (`User-agent: *` / `Allow: /`) ; rien n'a été modifié sans accord.
Deux familles à distinguer :
- **Recherche / réponse** (ils citent et renvoient vers le site) : Googlebot (Google, y compris AI Overviews), Bingbot
  (Bing, Copilot), OAI-SearchBot et ChatGPT-User (ChatGPT), PerplexityBot et Perplexity-User, Claude-SearchBot et Claude-User,
  Applebot. **À laisser autorisés**, sinon l'entreprise ne peut pas apparaître dans ces réponses.
- **Entraînement des modèles** (ils ne renvoient pas de visiteurs) : GPTBot, ClaudeBot, Google-Extended (n'a aucun effet
  sur Google Search ni AI Overviews), Applebot-Extended, CCBot, meta-externalagent, Bytespider.
Choix A (par défaut) : tout autoriser → `python3 outils/lancement.py --appliquer`.
Choix B : refuser seulement l'entraînement → `python3 outils/lancement.py --appliquer --bloquer-entrainement`.
`robots.txt` est une consigne respectée par les robots déclarés, pas une protection technique.
Contrôle du 07/11/2026 sur arno-franco.vercel.app : tous ces robots reçoivent la page complète (HTTP 200, HTML lisible),
aucune protection Vercel ne les bloque (pas de mode « challenge », pas de pare-feu anti-robots ; aperçus protégés par SSO).

## llms.txt
`public/llms.txt` : présentation courte, zone, liens vers les pages principales, coordonnées publiques. Convention récente,
lue par peu d'assistants : utile mais sans garantie. Ses adresses sont basculées par `outils/lancement.py`.
À mettre à jour à la main si une page, un service ou une coordonnée change (comme le pied de page).

## Formspree (formulaire de devis)
Aujourd'hui, le formulaire ouvre la messagerie du visiteur (`action="mailto:info@arnofranco.be"`). Pour l'envoi en ligne :

**À faire par l'équipe (compte Formspree)**
1. Créer un compte sur formspree.io, idéalement avec info@arnofranco.be (adresse qui recevra les demandes), et la confirmer.
2. Créer un formulaire « Site Arno Franco ». Formspree affiche une adresse du type `https://formspree.io/f/abcdwxyz`.
3. Dans les réglages du formulaire : vérifier l'adresse de destination, le plan (nombre d'envois mensuels inclus) et activer la protection anti-spam proposée.
4. Transmettre l'adresse exacte à Claude (ne jamais inventer l'identifiant).

**Modification du code (un seul endroit)**
- `public/index.html`, balise `<form id="form-devis" ...>` :
  remplacer `action="mailto:info@arnofranco.be" method="post" enctype="text/plain"`
  par `action="https://formspree.io/f/IDENTIFIANT" method="post"` (supprimer `enctype`).
  Le script reconnaît automatiquement une adresse Formspree ; sans JavaScript, le navigateur envoie directement à Formspree.
- `public/vie-privee.html` :
  - section « Données collectées » : remplacer la phrase « Le formulaire ouvre votre logiciel de messagerie… » par
    « Les demandes envoyées via le formulaire sont transmises par e-mail à Arno Franco par l'intermédiaire de Formspree. »
  - section « Sous-traitants » : ajouter `<li>Formspree (transmission des messages du formulaire par e-mail)</li>`

**Tests après déploiement (prévisualisation puis production)**
- Envoi complet → message de confirmation sur le site et e-mail reçu sur la boîte de destination (le 1er envoi peut demander une validation dans Formspree)
- Envoi avec un nom vide, un téléphone trop court, un e-mail invalide, la case non cochée → message d'erreur et curseur sur le champ concerné
- Le champ caché `_gotcha` rempli → message rejeté comme spam

## Avis clients
La section « Avis » a été retirée de la page tant qu'aucun avis réel n'est disponible (les styles `.avis` sont conservés).
Ne publier que de vrais avis, avec l'accord écrit du client (prénom + commune). Pas d'étoiles sans note réelle.
Gabarit à insérer avant la section `#zone` de public/index.html :
```html
<section id="avis">
  <div class="wrap">
    <p class="surtitre">Avis clients</p>
    <h2>Ils ont fait confiance à Arno</h2>
    <div class="avis-grille">
      <blockquote class="avis">« Texte exact de l'avis. »<footer>— Prénom, commune</footer></blockquote>
    </div>
  </div>
</section>
```
