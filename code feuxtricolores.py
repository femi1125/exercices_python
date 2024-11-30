couleur= str( input("entrez la couleur de feux tricolores dont vous voulez savoir la signification. \n Vous avez le choix entre:\n vert \n orange \n rouge"))
if couleur == "vert" :
    print("vous pouvez circuler")
elif couleur == "orange":
    print("RALENTISSEZ!!")
elif couleur == "rouge":
    print("ARRETEZ-VOUS!!!")
else:
    print("veuillez svp entrer une couleur valide!")
