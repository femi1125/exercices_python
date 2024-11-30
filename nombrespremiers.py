def prem(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):  
        if a % i == 0:
            return False
    return True
nbrprem = [x for x in range(1, 101) if prem(x)]

print("Les nombres premiers entre 1 et 100 sont :", nbrprem)
