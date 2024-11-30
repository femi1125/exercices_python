def calc(a, b):
    minval = min(a, b)
    pgcd = 1
    for i in range (1, minval ):  
        if a % i == 0 and b % i == 0:
            pgcd = i
    return pgcd
num1 = int(input("Entrez le premier nombre : "))
num2 = int(input("Entrez le deuxième nombre : "))

pgcd = calc(num1, num2)
print("Le PGCD est :" ,pgcd)
