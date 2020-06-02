import os
import json
 
dossier_courant = os.path.dirname(__file__)

chemin_liste = os.path.join(dossier_courant, "liste.json")
if os.path.exists(chemin_liste):
    f = open(chemin_liste,"r")
    liste_de_course = json.load(f)
    f.close()
else:
    liste_de_course = []

