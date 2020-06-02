# strip() permet d'enlever une série de caractère au début ou à la fin d'une chaine de caractères
import os

dossier_courant = os.path.dirname(__file__)
fichier_source = os.path.join(dossier_courant,"prenoms.txt")
fichier_dest = os.path.join(dossier_courant,"prenoms_tries.txt")

with open(fichier_source,"r",encoding="utf-8") as f:
    contenu_fichier = f.read()

lignes = contenu_fichier.splitlines()

liste_prenoms = []    

for ligne in lignes:
    liste_prenoms.extend(ligne.split())
    
prenoms_clean = [prenom.strip(", .") for prenom in liste_prenoms]
prenoms_clean.sort()

with open(fichier_dest,"w",encoding="utf-8") as f:
    f.write("\n".join(prenoms_clean))
        
    