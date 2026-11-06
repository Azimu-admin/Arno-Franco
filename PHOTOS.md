# Photos publiées sur le site (traçabilité) – fichier interne, non publié

Règle (voir CLAUDE.md) : uniquement de vraies photos de chantiers d'Arno ; retouches légères seulement ; originaux intacts
dans `photos-originales/` (branche `photos/originales`). Numérotation Pxxx : inventaire photo du 05/11/2026.

**06/11/2026 – noms de fichiers web descriptifs** : les copies web ont été renommées (code Pxxx conservé en tête, ex.
`bandeau-p021-1280.webp` → `p021-terrasse-pelouse-amenagees-autour-grands-oliviers-1280.webp`). Les noms cités plus bas
sont les anciens : la table complète ancien → nouveau est dans `outils/correspondance-images.csv`.

## Retouche douce appliquée (validée le 05/11/2026)
Identique pour toutes les photos de l'accueil, sans modification du contenu :
niveaux sur la luminance (0,6 % écrêté), gamma automatique pour les photos ternes, chaleur +3,5 %, contraste ×1,06,
saturation ×1,10, accentuation légère à l'export. Exports WebP sans métadonnées.

## Page d'accueil (maquette E validée le 05/11/2026)
| Emplacement | Photo | Fichiers | Recadrage | Particularité |
|---|---|---|---|---|
| Bandeau | P021 | `public/img/photos/bandeau-p021-{1280,1824,mobile-750,mobile-1080}.webp` | 16:9 (ordinateur), 4:3 (téléphone/tablette) | taille max. 1824 px (pas d'agrandissement) |
| Jardins & plantations | P193 | `jardins-p193-{360,540}.webp` | 3:4 | saturation ×1,04 |
| Entretien & arbres | P202 | `arbres-p202-{360,540}.webp` | 3:4 | |
| Piscines | P256 | `piscines-p256-{360,540}.webp` | 3:4 | |
| Terrassement | P070 | `terrassement-p070-{360,540}.webp` | 3:4 | |
| Terrasses & allées | P105 | `terrasses-p105-{360,540}.webp` | 3:4 | |
| Portails & clôtures | P137 | `portails-p137-{360,540}.webp` | 3:4 | **numéro de maison flouté** ; chaleur +5 %, gamma 0,92 |

## Section « Nos savoir-faire » (cartes, sans retouche couleur)
`public/img/cartes/carte-pXXX-{480,640,800}.webp` : P132, P191, P202, P194, P256, P109, P082, P137 (numéro flouté),
P179, P175, P129, P223.

## Page « Piscines & abords » (`/savoir-faire/piscines`, validée le 05/11/2026)
Retouche douce identique (réglages par défaut, aucun masquage nécessaire). Fichiers dans `public/img/piscines/`.
| Emplacement | Photo | Fichiers | Recadrage | Chantier (inventaire) |
|---|---|---|---|---|
| Bandeau | P254 | `p254-bandeau-{960,1440}`, `p254-mobile16x10-{750,1080}` | 16:9 (ordinateur), 16:10 (téléphone/tablette) | B, piscine corten |
| Galerie 1 | P243 | `p243-mosaique-{720,1080}` | 3:4 (case haute) | A, grandes dalles |
| Galerie 2 | P142 | `p142-mosaique-large-{800,1200}` | 12:5 (case large) | C (probable, à confirmer) |
| Galerie 3 | P120 | `p120-mosaique-carre-{720,1080}` | 4:3 | D |
| Galerie 4 | P140 | `p140-mosaique-720` | 4:3 (768 px max, pas d'agrandissement) | E |
| Chantier | P256 | `p256-chantier-{480,720}` | 1:1 | B |
| Chantier | P260 | `p260-chantier-{480,720}` | 1:1 | B |

Section « Chantier » : aucune chronologie publiée tant qu'Arno ne l'a pas confirmée.

## Page « Nos savoir-faire » (`/savoir-faire`, maquette validée le 05/11/2026)
Retouche douce identique (P137 : numéro de maison flouté, chaleur +5 %, gamma 0,92). Fichiers dans `public/img/savoir-faire/`.
Cartes : carré 1:1 (`-400`, `-640`, ordinateur et tablette) et 16:10 (`-m480`, `-m720`, téléphone).
| Emplacement | Source | Fichiers | Remarque |
|---|---|---|---|
| Bandeau | P125 | `bandeau-p125-{520,768}` | recadrage du haut de la photo (feuillage et soleil) : voiture et maison exclues ; 768 px max |
| Jardins & plantations | P132 | `jardins-plantations-p132-*` | |
| Entretien des espaces verts | P191 | `entretien-espaces-verts-p191-*` | |
| Élagage & abattage | P202 | `elagage-abattage-p202-*` | |
| Piscines & abords | P256 | `piscines-p256-*` | |
| Terrassement & soutènement | P194 | `terrassement-soutenement-p194-*` | |
| Terrasses & allées | P109 | `terrasses-allees-p109-*` | |
| Portails & clôtures | P137 | `portails-clotures-p137-*` | numéro de maison masqué |
| Sports & loisirs | **illustration générée (IA)** | `sports-loisirs-illustration-ia-*` | **exception validée par l'équipe (05/11/2026)** : pas une photo de chantier ; texte alternatif « Illustration… » ; ne jamais la légender comme une réalisation d'Arno ni la placer dans une galerie de chantiers |
| Espaces publics & professionnels | P134 | `espaces-professionnels-publics-p134-*` | personne de dos, non identifiable |
| Aménagements intérieurs | P223 | `amenagements-interieurs-p223-*` | |

## Page « Réalisations » (`/realisations`, direction artistique validée le 05/11/2026)
Fichiers : `public/img/realisations/<pxxx>-<largeur>.webp` (480/640/800/1280 + native < 1280). Retouche douce standard,
sans IA. Originaux intacts (contrôle MD5). Ordre = ordre d'affichage ; la 1re photo de chaque chantier est la dominante (provisoire).

| Chantier (titre provisoire) | Photos | Particularités |
|---|---|---|
| 01 – Grande propriété paysagée, piscine et oliviers | P023, P020, P021, P047, P038, P024, P039, P051, P052, P022, P041, P057 |  |
| 04 – Terrasse en bois construite autour d'un arbre | P086, P074, P080, P077 |  |
| 02 – Piscine et aménagement des abords | P254, P256, P255, P258, P259, P257, P260, P261 |  |
| 03 – Piscine et plage dallée | P243, P244, P245, P242 |  |
| 21 – Piscine, citerne et gazon | P084, P081, P078, P082, P083 |  |
| 05 – Maison en pente, terrasse et murs en pierre | P093, P095, P090 |  |
| 06 – Escalier et allée en granit | P105, P108, P109 |  |
| 08 – Soutènement et escalier, maison en pierre | P200, P194, P197, P199 |  |
| 10 – Jardin avec grand saule, clôture et piscine | P160, P156, P141 |  |
| 10b – Piscine en cours de réalisation | P163, P162 |  |
| 07 – Portail anthracite et piliers en pierre | P137, P126, P123 | P137 numéro masqué (flou); P126 recadrée (haut retiré : voitures et plaques) |
| 09 – Allées drainantes | P206, P198, P205 |  |
| 11 – Terrasse, pergola et gabions | P017, P018 |  |
| 12 – Maison contemporaine, empierrement et dalles alvéolées | P065, P063, P067, P068 |  |
| 13 – Plantation de massif sur talus | P118, P114 |  |
| 14 – Cour en pavés anciens | P151, P155, P158 |  |
| 15 – Clôture composite et arbres palissés | P216, P221 |  |
| 16 – Cour gravillonnée et pas en dalles | P234, P232, P233 | P234 recadrée (bord droit retiré : voitures); P232 recadrée (gauche retirée : voitures) |
| 17 – Terrasse en grandes dalles | P238, P239 |  |
| 18 – Allée pavée et marches | P252, P253 |  |
| 19 – Jardin et clôture anthracite | P012, P011a, P011b | P011a moitié haute du montage P011 (avant); P011b moitié basse du montage P011 (après) |
| 20 – Entretien des topiaires | P191, P189, P190 |  |
| 22 – Aménagement intérieur : sol en béton dans un bâtiment ancien | P223, P213, P220, P219 |  |

Écartées de la sélection de l'équipe : P204 (voiture au centre), P117, P161, P094, P064 (vues faibles) ;
P089, P195, P016, P214 (appartenance au chantier à confirmer). Séries complémentaires non retenues : P069–P076, P085 (terre nue,
personnes, ouvrier torse nu P076), P211 (quasi identique à P223), P209 (travail non identifiable), P025–P032, P111–P115, élagage.

## Page « À propos & Contact » (`/a-propos-contact`)
- `img/a-propos/portrait-arno-*.webp` : P001 (« Arno Franco.jpg »), recadrage seul, aucune retouche.
- `img/a-propos/equipe-*.webp` : P224 (fichier identique à celui fourni par l'équipe le 05/11/2026),
  recadrée au-dessus du bandeau de vœux ; aucune retouche.

## Page « Travaux publics » (`/travaux-publics`, V3 validée le 05/11/2026)
Retouche douce standard sur les originaux ; plaques masquées (flou) : P227. Bandeau : P092.

| Chantier (titre provisoire) | Photos | Particularités |
|---|---|---|
| Grand mur de soutènement | P097, P092, P091, P088 |  |
| Restauration d'un ensemble patrimonial | P187, P188b, P185, P181b, P186, P182b, P183b, P188a | visionneuse seule : P183a, P182a, P181a ; vues extraites des montages P181–P188 par simple recadrage (a = vue gauche, b = vue droite), sans retouche couleur ; P184b écartée (doublon de P187), P184a écartée (voile) |
| Passerelle en bois dans la fagne | P134, P129, P124 |  |
| Plantations et aménagements en voirie | P227, P226, P225 |  |
| Ancienne bâtisse et grande vasque en pierre | P002 |  |

Montages P181–P188 : aucun original séparé trouvé (dépôt et fichiers accessibles, comparaison d'empreintes). Les vues
extraites sont des recadrages des photos réelles d'Arno (conforme à la règle photo). À remplacer par les originaux HD dès réception.

## Pages de services (`/savoir-faire/<catégorie>`, 06/11/2026)
Retouche douce standard, recadrage seul, aucune IA ; images dans `public/img/<catégorie>/` (jardins : `img/jardins/`).
P137 : numéro de maison masqué (flou). Ordre : bandeau, puis galeries dans l'ordre d'affichage.

| Page | Bandeau | Photos |
|---|---|---|
| jardins-plantations | P146 | P154, P087, P052, P049, P043, P059 ; plan d'eau P008 |
| entretien-espaces-verts | P191 | P190, P127, P189, P171 |
| elagage-abattage | P202 | P196, P203, P230, P005, P009, P006, P004, P007, P010, P168, P172 |
| terrassement-soutenement | P200 | P194, P197, P058, P199, P030, P096, P082, P081 |
| terrasses-allees | P139 | P144, P165, P150, P153, P027, P025, P166, P113, P108, P195, P068 |
| portails-clotures | P128 | P137, P012, P123, P037, P216, P214, P046 |
| sports-loisirs | P179 | P062, P056, P180, P176, P178, P175 |
| amenagements-interieurs | P223 | P213, P220, P219, P211 |

Écartées : P125 (haie, pas une souche), P124/P134 (passerelle publique), P048 (pas une pétanque), P040 (gazon), P028
(ombre du photographe), P173/P204 (voiture), P177 (capture d'écran), P106 (soudure), P221 (= P216), P209 (travail non
identifiable), P013 et P170 (intervention non lisible ou prestation non confirmée). Réserve Piscines : P257, P259, P047, P084.

## Accueil – compléments (06/11/2026)
- Galerie « Quelques chantiers » (`img/accueil/`, retouche douce) : P154 (jardin, haute), P058 (pierre), P006 (abattage),
  P047 (piscine), P012 (clôture), P052 (jardin), P238 (terrasse), P196 (élagage, haute), P153 (terrasse), P105 (pierre).
  Aucun « avant/après » : pas de paire confirmée retenue.
- « À propos » : P262 = « Arno sur chantier.jpg » (ajoutée à la photothèque le 06/11/2026), recadrage 4:5, sans retouche.
- Carte « Espaces publics » : P134 (passerelle terminée, même chantier TP2) remplace P129 (état antérieur).
- Terrassement & soutènement, encart « Notre matériel » : P263 = « 789446273_…_n (1).jpg » (pelle Takeuchi), recadrée sous
  la vitre arrière (l'inscription « location de conteneurs », prestation non confirmée, n'est pas visible), sans retouche.

## Décisions
- P132 écartée du bandeau (05/11/2026) ; P147 non retenue ; P238 envisagée pour une future page « Terrasses ».
- Les visuels IA de la référence graphique (maquette D) ne sont jamais une source photographique.
