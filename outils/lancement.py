#!/usr/bin/env python3
"""Bascule du site vers le domaine définitif arnofranco.be et réactivation de l'indexation.

  python3 outils/lancement.py              → simulation : affiche ce qui serait modifié, ne touche à rien
  python3 outils/lancement.py --appliquer  → applique les modifications (à faire UNIQUEMENT quand
                                             https://arnofranco.be répond et affiche le bon site, voir LANCEMENT.md)

Ce que fait --appliquer :
 1. remplace https://arno-franco.vercel.app par https://arnofranco.be (canonical, Open Graph, JSON-LD, sitemap, robots.txt) ;
 2. retire <meta name="robots" content="noindex"> et le commentaire PRÉ-LANCEMENT de toutes les pages, sauf 404.html ;
 3. vercel.json : l'en-tête X-Robots-Tag: noindex ne s'applique plus qu'aux adresses *.vercel.app (aperçus) ;
    ajoute les redirections permanentes www.arnofranco.be → arnofranco.be et arno-franco.vercel.app → arnofranco.be ;
 4. robots.txt définitif (Allow + Sitemap) et sitemap régénéré.
"""
import re, sys, os, glob, json, subprocess
ICI = os.path.dirname(os.path.abspath(__file__)); RACINE = os.path.dirname(ICI); PUB = os.path.join(RACINE, 'public')
ANCIEN, NOUVEAU = 'https://arno-franco.vercel.app', 'https://arnofranco.be'
APPLIQUER = '--appliquer' in sys.argv
modifs = []
def ecrire(chemin, avant, apres):
  if avant != apres:
    modifs.append(os.path.relpath(chemin, RACINE))
    if APPLIQUER: open(chemin, 'w').write(apres)

for f in sorted(glob.glob(PUB + '/**/*.html', recursive=True)):
  s = open(f).read(); t = s.replace(ANCIEN, NOUVEAU)
  t = re.sub(r'\n<!-- Adresse du site :[^>]*-->', '', t)
  if not f.endswith('/404.html'):
    t = re.sub(r'\n<!-- PRÉ-LANCEMENT[^>]*-->', '', t)
    t = t.replace('\n<meta name="robots" content="noindex">', '')
  ecrire(f, s, t)

f = os.path.join(PUB, 'robots.txt'); s = open(f).read()
ecrire(f, s, f'User-agent: *\nAllow: /\n\nSitemap: {NOUVEAU}/sitemap.xml\n')

f = os.path.join(RACINE, 'vercel.json'); s = open(f).read(); cfg = json.loads(s)
for h in cfg['headers']:
  if h['source'] == '/(.*)' and any(x['key'] == 'X-Robots-Tag' for x in h['headers']):
    h['has'] = [{'type': 'host', 'value': r'(?<sousdomaine>.*)\.vercel\.app'}]
cfg['redirects'] = [
  {'source': '/:chemin*', 'has': [{'type': 'host', 'value': 'www.arnofranco.be'}], 'destination': NOUVEAU + '/:chemin*', 'permanent': True},
  {'source': '/:chemin*', 'has': [{'type': 'host', 'value': 'arno-franco.vercel.app'}], 'destination': NOUVEAU + '/:chemin*', 'permanent': True},
]
ecrire(f, s, json.dumps(cfg, ensure_ascii=False, indent=2) + '\n')

f = os.path.join(PUB, 'sitemap.xml'); s = open(f).read(); ecrire(f, s, s.replace(ANCIEN, NOUVEAU))

print(('Modifié' if APPLIQUER else 'Serait modifié') + f' ({len(modifs)} fichiers) :'); print('  ' + '\n  '.join(modifs))
if APPLIQUER:
  subprocess.run([sys.executable, os.path.join(ICI, 'sitemap.py')], check=True)
  reste = subprocess.run(['grep', '-rln', 'vercel.app', PUB], capture_output=True, text=True).stdout.split()
  noidx = subprocess.run(['grep', '-rl', 'noindex', PUB], capture_output=True, text=True).stdout.split()
  print('Contrôle vercel.app restant :', reste or 'aucun')
  print('Contrôle noindex restant    :', [os.path.relpath(x, RACINE) for x in noidx], '(attendu : public/404.html uniquement)')
else:
  print('\nSimulation uniquement. Relancer avec --appliquer le jour du lancement.')
