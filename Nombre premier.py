def est_premier(n):
    """
    Vérifie si un nombre est premier ou non.

    Arguments :
    - n : int, le nombre à vérifier.

    Renvoie :
    - bool, True si n est premier, False sinon.
    """
    if n < 2:  # 0 et 1 ne sont pas des nombres premiers
        return False
    for i in range(2, int(n**0.5)+1):  # parcours des diviseurs potentiels
        if n % i == 0:  # si n est divisible par i, ce n'est pas un nombre premier
            return False
    return True  # n'est divisible que par 1 et par lui-même, donc est premier
