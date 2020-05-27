nombre_mystere = 7

nombre_utilisateur = int(input("Devinez le nombre mystère. Entrez un nombre: "))

if nombre_utilisateur > nombre_mystere:
    print(f"{nombre_utilisateur} est plus grand que le nombre mystère.")
elif nombre_utilisateur < nombre_mystere:
    print(f"{nombre_utilisateur} est plus petit que le nombre mystère.")
else:
    print(f"Vous avez deviné le nombre mystère {nombre_utilisateur}!")