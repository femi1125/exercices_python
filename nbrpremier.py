def prem(nombre):  
    if nombre <= 1:
        return False
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            return False

    return True
nombre = int(input("Entrez un nombre entier  : "))

if prem(nombre):
    print(nombre, "est un nombre premier.")
else:
    print(nombre, "n'est pas un nombre premier.")  


