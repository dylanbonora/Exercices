
# valeur = input("Entrez une température en degré Celsius :")

#input retourne une chaine de caractère, Si vous voulez utiliser la valeur entrée par l'utilisateur comme un nombre, 
# vous devez la convertir en utilisant les fonctions de conversion de type comme int() ou float().


# Demander à l'utilisateur la température en Celsius
celsius = int(input("Entrez la température en Celsius : "))

# Convertir la température en Fahrenheit
fahrenheit = (celsius * 9/5) + 32

#print("Convertion Celsius en Farhenheit : ", celsius)

# Afficher le résultat
print(f"{celsius} degrés Celsius équivalent à {fahrenheit} degrés Fahrenheit.")
