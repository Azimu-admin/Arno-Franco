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
- Couleurs : #153e35 (foncé), #609e4b (moyen), #b8eea4 (clair). Le logo est dans `public/img/` et `logo-source/`.
- **Seul `public/` est publié** (vercel.json → outputDirectory). Ne jamais mettre de fichier interne dans `public/`.
- Le site est en pré-lancement (noindex). Pour lancer : suivre `LANCEMENT.md`.

## Règles de collaboration (validées le 05/11/2026)
- **Répartition des rôles** : la direction artistique et la sélection définitive des photos sont décidées par l'équipe
  (avec ChatGPT). Claude fournit les éléments techniques, puis développe les pages selon les choix validés.
- **Accueil figé** : la page d'accueil validée par Arno (maquette E, bandeau P021) est la référence graphique. Ne jamais
  modifier son apparence, ses photos, ses couleurs, sa typographie, ses textes, ses pictogrammes ou sa composition sans
  demande explicite.
- **Pas de choix artistique** : ne pas proposer de photo de couverture, de sélection artistique définitive ni d'ordre de
  galerie pour les catégories. Une photo de la mosaïque d'accueil ne devient pas automatiquement la couverture de sa catégorie.
- **Planches-contact** : uniquement pour visualiser les photos disponibles (ordre de numéro), sans cadre ni mention
  désignant une couverture recommandée, sans classement artistique.
- **Inventaire photo P001–P261** : base documentaire à conserver et tenir à jour (dimensions, rattachement aux catégories,
  regroupements par chantier, alertes techniques). L'inventaire neutre des 10 catégories de « Nos savoir-faire » en fait partie.
- **Contraintes à signaler** (rôle de Claude) : résolution insuffisante, cadrage techniquement difficile, personnes
  identifiables, plaques ou numéros à masquer, doublons, performances, accessibilité.
- **Contenus** : toujours distinguer les prestations confirmées des points à valider par Arno. Ne jamais transformer ce qui
  est visible ou supposé sur une photo en prestation annoncée.
- **Pages de catégories** : attendre la maquette validée et les instructions d'intégration de l'équipe avant de développer
  (aucune maquette Piscines ou autre sans demande).
- **Aucune modification, fusion ou déploiement sans accord explicite** de l'équipe.
