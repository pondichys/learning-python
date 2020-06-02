employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
            "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
            }
            
# Enlever Patrick du dictionnaire
del employes["id03"]
# Mettre à jour âge de Julie
employes["id02"]["age"] = 26
# Afficher âge de Paul
age_paul = employes["id01"]["age"]
print(age_paul)
print(employes)