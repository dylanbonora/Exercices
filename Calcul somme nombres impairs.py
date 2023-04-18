# Demander à l'utilisateur un nombre entier positif
n = int(input("Entrez un nombre entier positif : "))

# Initialiser la variable somme à 0
somme = 0

# Parcourir tous les nombres impairs de 1 à n et les ajouter à la somme
for i in range(1,n+1,2):
    #somme = somme + somme
    somme +=1
    
print(f"La somme des nombres impairs de 1 à {n} est : {somme}")