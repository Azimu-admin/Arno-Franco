"""Pied de page commun : une seule source (outils/pied-de-page*.html) recopiée dans toutes les pages de public/.
Usage : python3 outils/pied-de-page.py          (applique)
        python3 outils/pied-de-page.py --verifier (échoue si une page diffère)"""
import glob,re,sys,os
R=os.path.dirname(os.path.abspath(__file__));PUB=os.path.join(R,'..','public')
long_=open(os.path.join(R,'pied-de-page.html')).read().strip();court=open(os.path.join(R,'pied-de-page-court.html')).read().strip()
COURT={'mentions-legales.html','vie-privee.html','404.html'};ko=[]
for f in sorted(glob.glob(PUB+'/**/*.html',recursive=True)):
  s=open(f).read();m=re.search(r'<footer>.*?</footer>',s,re.S)
  if not m: continue
  ref=court if os.path.basename(f) in COURT else long_
  if m.group(0)!=ref:
    if '--verifier' in sys.argv: ko.append(os.path.relpath(f,PUB))
    else: open(f,'w').write(s[:m.start()]+ref+s[m.end():]);print('mis à jour :',os.path.relpath(f,PUB))
if ko: print('pieds de page différents :',ko);sys.exit(1)
if '--verifier' in sys.argv: print('pieds de page identiques sur toutes les pages')
