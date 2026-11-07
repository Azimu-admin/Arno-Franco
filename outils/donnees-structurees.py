#!/usr/bin/env python3
"""(Ré)écrit les données structurées JSON-LD à partir du contenu visible des pages. Idempotent.
 - accueil : @graph WebSite + entreprise (HomeAndConstructionBusiness) avec le catalogue des pages de services ;
 - pages de services et Travaux publics : un nœud Service (nom = titre H1, description = phrase d'introduction visible),
   relié à l'entreprise par son @id. Aucun prix, avis, note ni certification.
L'adresse du site est lue dans la balise canonical (bascule de domaine gérée par outils/lancement.py)."""
import re, os, json, html, glob
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'public')
SERVICES = ['jardins-plantations', 'entretien-espaces-verts', 'elagage-abattage', 'piscines', 'terrassement-soutenement',
            'terrasses-allees', 'portails-clotures', 'sports-loisirs', 'amenagements-interieurs']
def lire(p): return open(os.path.join(R, p)).read()
def propre(x): return re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', '', x))).strip()
def h1_et_intro(s):
  m = re.search(r'<h1[^>]*>(.*?)</h1>.*?<p[^>]*>(.*?)</p>', s, re.S); return propre(m.group(1)), propre(m.group(2))
def bloc(s, ident, donnees):
  s = re.sub(r'\n<script type="application/ld\+json" id="%s">.*?</script>' % ident, '', s, flags=re.S)
  return s.replace('</head>', f'<script type="application/ld+json" id="{ident}">\n' + json.dumps(donnees, ensure_ascii=False, indent=1) + '\n</script>\n</head>', 1)
accueil = lire('index.html')
B = re.search(r'<link rel="canonical" href="(https://[^/"]+)', accueil).group(1)
ENT = B + '/#entreprise'
ZONE = [{"@type": "City", "name": "Theux"}, {"@type": "City", "name": "Spa"}, {"@type": "City", "name": "Jalhay"},
        {"@type": "AdministrativeArea", "name": "Province de Liège"}]
catalogue = []
for n in SERVICES + ['travaux-publics']:
  p = f'savoir-faire/{n}.html' if n != 'travaux-publics' else 'travaux-publics.html'
  s = lire(p); nom, intro = h1_et_intro(s)
  url = re.search(r'<link rel="canonical" href="([^"]+)"', s).group(1)
  img = re.search(r'<meta property="og:image" content="([^"]+)"', s).group(1)
  serv = {"@context": "https://schema.org", "@type": "Service", "@id": url + '#service', "name": nom, "serviceType": nom,
          "description": intro, "url": url, "image": img, "areaServed": ZONE,
          "provider": {"@type": "HomeAndConstructionBusiness", "@id": ENT, "name": "Arno Franco", "url": B + '/'}}
  open(os.path.join(R, p), 'w').write(bloc(s, 'ld-service', serv))
  catalogue.append({"@type": "Offer", "itemOffered": {"@type": "Service", "@id": url + '#service', "name": nom, "url": url}})
# accueil : entreprise existante + site + catalogue
m = re.search(r'<script type="application/ld\+json">(.*?)</script>', accueil, re.S)
ent = json.loads(m.group(1))
if '@graph' in ent: ent = next(x for x in ent['@graph'] if x.get('@id') == ENT)
ent.pop('@context', None)
ent['hasOfferCatalog'] = {"@type": "OfferCatalog", "name": "Savoir-faire d'Arno Franco", "itemListElement": catalogue}
site = {"@type": "WebSite", "@id": B + '/#site', "url": B + '/', "name": "Arno Franco", "alternateName": "Arno Franco – Naturellement Professionnel",
        "inLanguage": "fr-BE", "publisher": {"@id": ENT}}
graphe = {"@context": "https://schema.org", "@graph": [site, ent]}
accueil = accueil[:m.start(1)] + '\n' + json.dumps(graphe, ensure_ascii=False, indent=2) + '\n' + accueil[m.end(1):]
open(os.path.join(R, 'index.html'), 'w').write(accueil)
print(f'{len(catalogue)} services, base {B}')
