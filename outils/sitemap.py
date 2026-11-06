#!/usr/bin/env python3
"""Régénère public/sitemap.xml (pages + photos) à partir des pages HTML.
Usage : python3 outils/sitemap.py            (domaine lu dans la balise canonical de l'accueil)
Seules les pages indexables (sans noindex définitif) et les vraies photos de chantiers sont listées ;
l'illustration générée « sports-loisirs-illustration-ia » est volontairement exclue. Pas de lastmod (pas de fausse date)."""
import re, os, glob, html
from xml.sax.saxutils import escape
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'public')
PAGES = ['index.html', 'savoir-faire/index.html'] + [f'savoir-faire/{n}.html' for n in (
  'piscines','jardins-plantations','entretien-espaces-verts','elagage-abattage','terrassement-soutenement',
  'terrasses-allees','portails-clotures','sports-loisirs','amenagements-interieurs')] + [
  'realisations.html','a-propos-contact.html','travaux-publics.html','mentions-legales.html','vie-privee.html']
EXCLURE = re.compile(r'logo|monogramme|favicon|apple-touch|illustration-ia')
def largeur(u): m = re.search(r'-m?(\d{3,4})\.\w+$', u); return int(m.group(1)) if m else 0
base = re.search(r'<link rel="canonical" href="(https://[^/"]+)', open(f'{R}/index.html').read()).group(1)
lignes = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
total = 0
for p in PAGES:
  s = open(f'{R}/{p}').read()
  loc = re.search(r'<link rel="canonical" href="([^"]+)"', s).group(1)
  vus = {}
  for tag in re.findall(r'<img\b[^>]*>', re.sub(r'<noscript>.*?</noscript>', '', s, flags=re.S)):
    alt = re.search(r'\balt="([^"]*)"', tag)
    if not alt or not alt.group(1).strip(): continue
    urls = re.findall(r'(?<![\w.])/?img/[^\s"\',]+', tag)
    urls = ['/' + u.lstrip('/') for u in urls if not EXCLURE.search(u)]
    if not urls: continue
    grand = max(urls, key=largeur)
    cle = re.sub(r'-m?\d{3,4}\.\w+$', '', grand)
    if cle not in vus: vus[cle] = grand
  lignes.append(f'  <url><loc>{escape(loc)}</loc>')
  for u in vus.values(): lignes.append(f'    <image:image><image:loc>{escape(base + u)}</image:loc></image:image>')
  lignes.append('  </url>'); total += len(vus)
lignes.append('</urlset>')
open(f'{R}/sitemap.xml', 'w').write('\n'.join(lignes) + '\n')
print(f'{len(PAGES)} pages, {total} photos → public/sitemap.xml ({base})')
