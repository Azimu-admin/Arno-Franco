# Photos publiées sur le site (traçabilité) – fichier interne, non publié

Règle (voir CLAUDE.md) : uniquement de vraies photos de chantiers d'Arno ; retouches légères seulement ; originaux intacts
dans `photos-originales/` (branche `photos/originales`). Numérotation Pxxx : inventaire photo du 05/11/2026.

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

## Page « Nos savoir-faire » (`/savoir-faire`, en cours de validation)
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

## Décisions
- P132 écartée du bandeau (05/11/2026) ; P147 non retenue ; P238 envisagée pour une future page « Terrasses ».
- Les visuels IA de la référence graphique (maquette D) ne sont jamais une source photographique.
