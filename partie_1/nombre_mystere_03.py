import random

nombre_mystere = random.randint(0, 1)

a = int(input("Devinez le nombre mystère. Entrez un nombre: "))

print(a == nombre_mystere)