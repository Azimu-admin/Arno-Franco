# Projet : site web Arno Franco – Naturellement Professionnel

## Entreprise
- Nom : Arno Franco – Naturellement Professionnel
- Gérant : Arno Franco (fondateur et gérant)
- Lieu : Theux / La Reid, province de Liège
- GSM : +32 479 18 42 82
- E-mail : info@arnofranco.be
- Facebook : https://www.facebook.com/p/Arno-Franco-Naturellement-Professionnel-100064242990785/
- LinkedIn : https://www.linkedin.com/in/arno-franco-606a30115/
- Domaine visé : arnofranco.be (aucun site existant trouvé)

## Activités (10 familles, toutes confirmées le 05/11/2026)
1. **Création et aménagement de jardins** : création de jardins ; aménagement de jardins et d'espaces extérieurs ;
   fourniture et plantation d'arbres et d'arbustes ; fourniture et pose de gazon en rouleaux ; réalisation de plans d'eau
2. **Entretien de jardins et d'espaces verts** : entretien ponctuel ou sous contrat ; pour particuliers, entreprises et copropriétés
3. **Travaux arboricoles** : élagage ; abattage d'arbres, y compris dangereux ; évacuation des chutes d'arbres ; fraisage de souches
4. **Terrassement et travaux de sol** : terrassement ; préparation de terrains ; pose de citernes ; terrassements liés aux aménagements
5. **Piscines et aménagements aquatiques** : réalisation et construction complète de piscines ; aménagement des abords ; plans d'eau
6. **Terrasses, allées et pierre naturelle** : terrasses (dont terrasses Horeca) ; allées ; travaux et aménagements en pierre naturelle
7. **Portails et clôtures** : pose de clôtures (fourniture à confirmer) ; pose de portails ; délimitation d'espaces extérieurs
8. **Terrains de sport et aires de jeux** : pétanque ; tennis ; terrains de jeux ; fourniture et installation de plaines de jeux ; espaces de loisirs
9. **Aménagements professionnels et travaux publics** : espaces publics ; travaux publics ; espaces extérieurs d'entreprises ;
   espaces verts de copropriétés ; terrasses pour établissements Horeca
10. **Aménagements intérieurs** : travaux d'aménagement intérieur

- Encore à confirmer : la **fourniture** des clôtures (point 7) ; l'**égouttage** (écrit sur la camionnette, absent de la liste).
- Toujours non confirmés : devis gratuit, liste des communes desservies, horaires.
- Inventaire photo (261 photos, présélection de 29) : réalisé le 05/11/2026, hors dépôt (livré à l'équipe).

## Logo (fourni le 05/11/2026)
- Source : logo-source/Arno_franco_Logo_final_10x10.pdf (Illustrator, 10 x 10 cm, vectoriel)
- Vectoriel : logo-source/logo-arno-franco.svg
- Pour le web : public/img/logo-arno-franco.png (complet, fond transparent),
  public/img/monogramme.png (« AF » seul), public/img/favicon.png, public/img/apple-touch-icon.png
- Couleurs : vert foncé #153e35 · vert moyen #609e4b · vert clair #b8eea4

## Infos à confirmer (reçues via une autre session, non vérifiées)
- Téléphone fixe : 087 71 16 00
- Code postal : 4910 Theux
- Intro Facebook (activités confirmées, texte lui-même non utilisé tel quel) : « Spécialiste en aménagement
  extérieur et entretien d'espaces verts. Création de jardins, terrasses, allées, clôtures, élagage et
  entretien : nous valorisons vos extérieurs avec expertise et passion. »

## Encore à obtenir d'Arno
Photos de chantiers (originaux, avant/après) · texte de présentation · horaires ·
zone d'intervention · devis gratuit ? · n° d'entreprise BCE/TVA · 3 à 5 vrais avis clients

## Fichiers
- `public/` : **seul dossier publié par Vercel** (vercel.json → outputDirectory). Tout ce qui est hors de public/ reste interne.
  - index.html : le site, une page
  - mentions-legales.html, vie-privee.html : pages légales (BCE, TVA, adresse, forme juridique à compléter)
  - 404.html : page introuvable
  - robots.txt, sitemap.xml, img/
- vercel.json : dossier publié, adresses sans .html, en-tête X-Robots-Tag (pré-lancement)
- .vercelignore : deuxième protection pour les fichiers internes
- LANCEMENT.md : procédure pour réactiver l'indexation et finaliser la mise en ligne
- Les adresses https://arno-franco.vercel.app sont à remplacer par https://arnofranco.be une fois le domaine relié
  (public/index.html : canonical, og:*, JSON-LD ; public/sitemap.xml ; ligne Sitemap de robots.txt)

## Formulaire de devis
- Prêt pour Formspree : un seul réglage, l'attribut `action` de `<form id="form-devis">` (procédure : LANCEMENT.md, section Formspree).
- Tant qu'il vaut `mailto:info@arnofranco.be`, l'envoi ouvre la messagerie du visiteur (avec ou sans JavaScript).

## Ajouter une photo de réalisation
1. Mettre le fichier dans `public/img/realisations/` (JPG, ~1600 px de large, < 400 Ko).
2. Dans la galerie de public/index.html, remplacer un cadre par :
   `<div class="photo" data-c="jardin"><img src="img/realisations/xxx.jpg" alt="description" loading="lazy"><span>Légende – commune</span></div>`
   (data-c : jardin, pierre, abattage, cloture, piscine)

## Hébergement
- Vercel, relié au dépôt GitHub Azimu-admin/Arno-Franco (branche main : chaque push redéploie)
- Projet Vercel : arno-franco (compte AZM, plan Hobby)
- Adresse de production stable : https://arno-franco.vercel.app
- Déploiement automatique vérifié le 05/11/2026 (commit d820b8c déployé)
- Décision (05/11/2026) : on reste sur Vercel.
- À faire : relier arnofranco.be · prévoir le plan Pro pour l'usage professionnel
  (le plan Hobby est réservé à un usage non commercial)
