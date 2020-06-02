import glob
import json

dossier = "c:/Users/sebastien/git/learning-python/partie_2/chercher_un_mot/dossier_exemple/**"
# Créer une liste de fichiers 
files = glob.glob(dossier, recursive=True)

num_compte = ""
num_soc = ""

for f in files:
    if f.endswith(".json"):
        with open(f,"r") as f:
            contenu_fichier = json.load(f)
            if "Credit Mutuel" in contenu_fichier:
                num_compte = contenu_fichier ["Credit Mutuel"] ["Numero de compte"]
    elif f.endswith(".txt"):
        with open(f,"r",encoding="utf-8") as f:
            contenu_fichier = f.read()
            if "Numéro de sécurité sociale" in contenu_fichier:
                num_soc = contenu_fichier.split(":") [-1]

print(f"Numéro de compte: {num_compte}")
print(f"Numéro de sécurité sociale: {num_soc}")
