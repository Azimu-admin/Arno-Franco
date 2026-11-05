# Procédure de lancement – arno-franco

Le site est actuellement en **pré-lancement** : il est en ligne, mais **exclu des moteurs de recherche** tant qu'il
contient des informations provisoires. Fichier interne (non publié).

## 1. Prérequis avant de réactiver l'indexation
- [ ] Plus aucune zone jaune `a-completer` visible : `grep -rn 'a-completer"' public/` ne renvoie que la définition CSS
- [ ] Vraies photos intégrées (bandeau, services, réalisations, portrait)
- [ ] Mentions légales complètes : adresse, n° BCE, n° TVA, forme juridique
- [ ] Durée de conservation des données validée (vie-privee.html)
- [ ] Formulaire relié à Formspree et testé (voir la section « Formspree » ci-dessous)
- [ ] Domaine arnofranco.be relié dans Vercel (Settings → Domains)
- [ ] Plan Vercel adapté à un usage commercial

- [ ] Aucun lien vers une page 404 : les 10 cartes de `/savoir-faire` doivent mener à des pages existantes
- [ ] `/a-propos-contact` intégrée (cible du menu et de « Demander un devis » sur `/realisations`)
- [ ] Menu des cinq onglets définitifs harmonisé sur toutes les pages

## 2. Remplacer l'adresse provisoire par le domaine
Remplacer `https://arno-franco.vercel.app` par `https://arnofranco.be` dans :
- `public/index.html` : `<link rel="canonical">`, balises `og:url` et `og:image`, bloc JSON-LD (`url`, `logo`, `image`)
- `public/sitemap.xml` : toutes les balises `<loc>`
- `public/savoir-faire/*.html` et `public/realisations.html` : `<link rel="canonical">`

Contrôle : `grep -rn "vercel.app" public/` ne doit plus rien renvoyer.

## 3. Réactiver l'indexation (les 3 éléments, dans le même commit)
1. **Balises meta** : supprimer le commentaire « PRÉ-LANCEMENT » et la ligne
   `<meta name="robots" content="noindex">` dans `public/index.html`, `public/mentions-legales.html`, `public/vie-privee.html`
   `public/realisations.html` et toutes les pages de `public/savoir-faire/`.
   ⚠️ Ne PAS la retirer de `public/404.html` (la page d'erreur doit rester non indexée).
2. **En-tête HTTP** : dans `vercel.json`, supprimer uniquement l'entrée `"source": "/(.*)"` qui ajoute `X-Robots-Tag: noindex`
   (garder l'entrée `/fonts/(.*)` qui gère le cache des polices).
3. **robots.txt** : remplacer le contenu de `public/robots.txt` par :
   ```
   User-agent: *
   Allow: /

   Sitemap: https://arnofranco.be/sitemap.xml
   ```

Contrôle avant commit : `grep -rn noindex public/ vercel.json` ne doit renvoyer que `public/404.html`.

## 4. Après le déploiement
- `curl -sI https://arnofranco.be/ | grep -i x-robots-tag` → aucune ligne
- Le code source de la page d'accueil ne contient plus `noindex`
- https://arnofranco.be/robots.txt affiche la ligne Sitemap
- Google Search Console : ajouter le domaine, envoyer `sitemap.xml`, demander l'indexation de la page d'accueil
- Vérifier https://arnofranco.be/PROJET.md → doit renvoyer 404

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
