import random

nombre_mystere = random.randint(0, 50)

for i in range(5):
    nombre = input("Quel est le nombre mystère ? ")
    
    if nombre.isdigit() :
        nombre = int(nombre)
    
        if nombre > nombre_mystere:
            print(f"Le nombre mystère est plus petit que {nombre}")
            continue
        elif nombre < nombre_mystere:
            print(f"Le nombre mystère est plus grand que {nombre}")
            continue
        else:
            print("Bravo, vous avez trouvé le nombre mystère !")
            exit()
    else :
        print("Vous n'avez pas entré un nombre!")
        continue

print(f"Vous avez perdu. Le nombre mystère était {nombre_mystere}")