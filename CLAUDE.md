# Instructions pour Claude

- Projet : site web d'Arno Franco (aménagement de jardins, Theux). Répondre en français.
- Lire `PROJET.md` en début de session : il contient toutes les infos de l'entreprise, les couleurs du logo,
  les éléments non vérifiés et ce qu'il reste à obtenir. Le tenir à jour quand une info change.
- Ne jamais inventer d'avis clients, de chiffres (années d'expérience, nombre de chantiers) ni de photos de réalisations :
  laisser une zone `.a-completer` tant que l'info réelle n'est pas fournie.
- **Règle photo définitive (05/11/2026)** : aucune photo de réalisation générée par IA, jamais. Toutes les photos publiées
  viennent des vrais chantiers d'Arno (`photos-originales/`, branche `photos/originales`). L'IA ou la retouche est autorisée
  seulement pour : masquer numéros et plaques, supprimer un objet gênant sans toucher au travail réalisé, lumière, couleurs,
  contraste, netteté, bruit, redressement, recadrage, optimisation web. Interdit : ajouter, inventer ou transformer
  réalisations, plantations, matériaux, constructions ou équipements. Toujours travailler sur des copies ; originaux intacts.
- **Exception unique à la règle photo** (validée le 05/11/2026) : la carte « Sports & loisirs » de la page « Nos savoir-faire »
  utilise une illustration générée de pétanque (`public/img/savoir-faire/sports-loisirs-illustration-ia-*`), documentée dans
  PHOTOS.md. Ne jamais la présenter comme une réalisation d'Arno ni l'utiliser ailleurs sans accord.
- Couleurs : #153e35 (foncé), #609e4b (moyen), #b8eea4 (clair). Le logo est dans `public/img/` et `logo-source/`.
- **Seul `public/` est publié** (vercel.json → outputDirectory). Ne jamais mettre de fichier interne dans `public/`.
- Le site est en pré-lancement (noindex). Pour lancer : suivre `LANCEMENT.md`.
