import os
from glob import glob
import shutil

# Trier les fichiers se trouvant dans ./tri_fichiers_sources
# Créer des sous-répertoires par extension
# mp3, wav : Musique
# mp4, mov : Videos
# jpg, jpeg, png : Images
# pdf : Documents

dossier_courant = os.path.dirname(__file__)

# Créer les 4 répertoires de tri dans dossier_dest
dossier_dest = os.path.join(dossier_courant,"dossier_tri")
dossier_mus = os.path.join(dossier_dest,"Musique")
os.makedirs(dossier_mus,exist_ok=True)
dossier_doc = os.path.join(dossier_dest,"Documents")
os.makedirs(dossier_doc,exist_ok=True)
dossier_vid = os.path.join(dossier_dest,"Videos")
os.makedirs(dossier_vid,exist_ok=True)
dossier_img = os.path.join(dossier_dest,"Images")
os.makedirs(dossier_img,exist_ok=True)

# Faire la liste des fichiers
chemin = os.path.join(dossier_courant,"tri_fichiers_sources","*")
liste_fichiers = glob(chemin)

for f in liste_fichiers:
    if f.endswith(".pdf"):
        shutil.copy(f,dossier_doc)
    elif f.endswith(".mp3") or f.endswith(".wav"):
        shutil.copy(f,dossier_mus)
    elif f.endswith(".mp4") or f.endswith(".mov"):
        shutil.copy(f,dossier_vid)
    elif f.endswith(".jpeg") or f.endswith(".jpg") or f.endswith(".png"):
        shutil.copy(f,dossier_img)
