import os

dossier_courant = os.path.dirname(__file__)

d = {"Films": ["Le seigneur des anneaux",
			   "Harry Potter",
			   "Moon",
			   "Forrest Gump"],
	 "Employes": ["Paul",
	 		      "Pierre",
				  "Marie"],
	 "Exercices": ["les_variables",
	 			   "les_fichiers",
				   "les_boucles"]}
for cle,valeur in d.items():
    for val in valeur:
        dossier = os.path.join(dossier_courant,cle,val)
        if not os.path.exists(dossier):
            os.makedirs(dossier)