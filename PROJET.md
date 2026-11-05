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

## Services (confirmés le 05/11/2026)
Création de jardins · Entretien de jardins et d'espaces verts (particuliers et professionnels) ·
Élagage · Abattage d'arbres dangereux · Terrassement · Terrasses et allées · Pierre naturelle ·
Clôtures · Espaces piscine
- À demander à Arno : évacuation des déchets verts, broyage, dessouchage, pose de gazon, arrosage automatique ?

## Logo (fourni le 05/11/2026)
- Source : logo-source/Arno_franco_Logo_final_10x10.pdf (Illustrator, 10 x 10 cm, vectoriel)
- Vectoriel : logo-source/logo-arno-franco.svg
- Pour le web : img/logo-arno-franco.png (complet, fond transparent),
  img/monogramme.png (« AF » seul), img/favicon.png, img/apple-touch-icon.png
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
- index.html : le site, une page (zones jaunes = à compléter)
- mentions-legales.html, vie-privee.html : pages légales (BCE, TVA, adresse, forme juridique à compléter)
- 404.html : page introuvable
- vercel.json (adresses sans .html), robots.txt, sitemap.xml
- Les adresses https://arno-franco.vercel.app sont à remplacer par https://arnofranco.be une fois le domaine relié
  (index.html : canonical, og:*, JSON-LD ; robots.txt ; sitemap.xml)

## Formulaire de devis
- Prêt pour Formspree : mettre l'identifiant dans `data-formspree="..."` sur `<form id="form-devis">`.
- Tant qu'il est vide, l'envoi ouvre un e-mail prérempli vers info@arnofranco.be.

## Ajouter une photo de réalisation
1. Mettre le fichier dans `img/realisations/` (JPG, ~1600 px de large, < 400 Ko).
2. Dans la galerie de index.html, remplacer un cadre par :
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
