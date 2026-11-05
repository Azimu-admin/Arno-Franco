# Procédure de lancement – arno-franco

Le site est actuellement en **pré-lancement** : il est en ligne, mais **exclu des moteurs de recherche** tant qu'il
contient des informations provisoires. Fichier interne (non publié).

## 1. Prérequis avant de réactiver l'indexation
- [ ] Plus aucune zone jaune `a-completer` visible : `grep -rn 'a-completer"' public/` ne renvoie que la définition CSS
- [ ] Vraies photos intégrées (bandeau, services, réalisations, portrait)
- [ ] Mentions légales complètes : adresse, n° BCE, n° TVA, forme juridique
- [ ] Durée de conservation des données validée (vie-privee.html)
- [ ] Formulaire relié à Formspree et testé (puis ajouter Formspree dans les sous-traitants de vie-privee.html)
- [ ] Domaine arnofranco.be relié dans Vercel (Settings → Domains)
- [ ] Plan Vercel adapté à un usage commercial

## 2. Remplacer l'adresse provisoire par le domaine
Remplacer `https://arno-franco.vercel.app` par `https://arnofranco.be` dans :
- `public/index.html` : `<link rel="canonical">`, balises `og:url` et `og:image`, bloc JSON-LD (`url`, `logo`, `image`)
- `public/sitemap.xml` : toutes les balises `<loc>`

Contrôle : `grep -rn "vercel.app" public/` ne doit plus rien renvoyer.

## 3. Réactiver l'indexation (les 3 éléments, dans le même commit)
1. **Balises meta** : supprimer le commentaire « PRÉ-LANCEMENT » et la ligne
   `<meta name="robots" content="noindex">` dans `public/index.html`, `public/mentions-legales.html` et `public/vie-privee.html`.
   ⚠️ Ne PAS la retirer de `public/404.html` (la page d'erreur doit rester non indexée).
2. **En-tête HTTP** : dans `vercel.json`, supprimer tout le bloc `"headers": [ ... ]` (X-Robots-Tag: noindex).
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
