import random

 

# Définition d'une fonction qui génère 5 numéros principaux et 2 étoiles

def generate_numbers():

    numbers = []  # Crée une liste vide qui sera utilisée pour stocker les 5 numéros principaux générés

    while len(numbers) < 5:  # Boucle tant que la longueur de la liste est inférieure à 5

        number = random.randint(1,50)  # Génère un nombre aléatoire entre 1 et 50

        if number not in numbers:  # Vérifie si le nombre n'est pas déjà présent dans la liste

            numbers.append(number)  # Si le nombre n'est pas déjà présent, l'ajoute à la liste

    numbers.sort()  # Trie les nombres dans l'ordre croissant

    stars = []  # Crée une autre liste vide pour stocker les 2 étoiles générées

    while len(stars) < 2:  # Boucle tant que la longueur de la liste est inférieure à 2

        number = random.randint(1,12)  # Génère un nombre aléatoire entre 1 et 12

        if number not in stars:  # Vérifie si le nombre n'est pas déjà présent dans la liste des étoiles

            stars.append(number)  # Si le nombre n'est pas déjà présent, l'ajoute à la liste des étoiles

    stars.sort()  # Trie les étoiles dans l'ordre croissant

    return numbers + stars  # Retourne une liste contenant les 5 numéros principaux et les 2 étoiles

 

# Définition d'une fonction pour afficher les numéros générés

def display(numbers):

    #print("Vos numéros sont: {} {} {} {} {}. Étoiles: {} {}".format(*numbers))

    print(f"Vos numéros sont: {numbers[0]} {numbers[1]} {numbers[2]} {numbers[3]} {numbers[4]}. Étoiles: {numbers[5]} {numbers[6]}")

 

# Définition de la fonction principale

def main():

    numbers = generate_numbers()  # Appelle la fonction pour générer les numéros

    display(numbers)  # Appelle la fonction pour afficher les numéros générés

 

# Vérifie si ce module est exécuté en tant que programme principal

if __name__ ==  "__main__":

    main()  # Appelle la fonction principale si ce module est exécuté en tant que programme principal