def factorielle(n):
    if n < 0:
       return print( "Entrez un nombre valide.")
    elif n == 0 or n == 1:
        return 1
    else:
        r = 1
        for i in range(2, n + 1):
            r *= i
        return r
nombre = int(input("Entrez un nombre : "))
print(f"La factorielle de" ,nombre, "est :" ,factorielle(nombre))
