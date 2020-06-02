# Ce script doit gérer 2 types d'erreur à l'ouverture d'un fichier
# 1) le fichier ne peut pas être lu
# 2) le fichier n'existe pas

fichier = input("Veuillez introduire un nom complet de fichier à ouvrir: ")
try:
    f = open(fichier,"r")
except FileNotFoundError:
    print("Le fichier n'existe pas !")
else:
    try:
        contenu = f.read()
    except:
        print("Le fichier ne peut pas être lu !")
    else:
        print(contenu)
    finally:
        f.close()