import time
import os
from os import walk
import pathlib
import string

print(" - TACHE 1 - ")

# 1.1
'''
Nous avons ici deux fonctions, une étant f(x) qui retourne la valeur de x multipliée par 2 et dont on ajoute
1. La fonction g() quant à elle retourne juste 7. On teste ensuite les fonctions entre elles pour voir si elles fonctionnent.
Affichage 1 : 5 (f(2) = 2 * 2 + 1 = 5)
Affichage 2 : 18 ('f(5) = 2 * 5 + 1 = 11' + 'g() = 7' = 18)
'''
def f(x) :
    return 2 * x + 1
def g() :
    return 7
y = f(2)
print(y)
y = f(5) + g()
print(y)

# 1.2
def bread() :
    print("<////////// >")
def lettuce() :
    print("~~~~~~~~~~~~")
def tomato() :
    print ("O O O O O O")
def ham() :
    print ("============")

print("--------------------------------")
print("Création du Sandwich double viande avec salade tomate :")

bread()
lettuce()
tomato()
ham()
ham()
bread()

print("--------------------------------")

# 1.3
def sandwich_simulator():
    bread()
    lettuce()
    tomato()
    ham()
    ham()
    bread()
    print("Sandwich prêt !")

for i in range(0, 41):
    sandwich_simulator()
print("Bravo, vous avez créé 42 sandwiches. Vous vous êtes bien nourris.")
print("--------------------------------")

# 1.4
def sandwich_simulator_2(number_of_sandwiches):
    if number_of_sandwiches <= 0 :
        print("Je ne peux pas créer de sandwiches négatifs.")
    else: 
        for i in range(0, number_of_sandwiches):
            sandwich_simulator()

number_of_sandwiches = int(input("Combien voulez-vous de sandwiches ? "))
sandwich_simulator_2(number_of_sandwiches)
print("--------------------------------")

# 1.5
def vegan_sandwich_simulator():
    bread()
    lettuce()
    tomato()
    lettuce()
    lettuce()
    lettuce()
    bread()
    print("Sandwich Vegan prêt !")

def sandwich_simulator_2(number_of_sandwiches, vegan_type):
    if number_of_sandwiches <= 0 :
        print("Je ne peux pas créer de sandwiches négatifs.")
    else: 
        if vegan_type == "Oui":
            for i in range(0, number_of_sandwiches):
                vegan_sandwich_simulator()
        else :
            for i in range(0, number_of_sandwiches):
                sandwich_simulator()

sandwich_numbers = int(input("Combien voulez-vous de sandwiches ? "))
sandwich_type = str(input("Voulez-vous qu'il soit vegan ? Dites 'Oui' pour valider la commande."))
sandwich_simulator_2(sandwich_numbers, sandwich_type)

print("--------------------------------")

print("CHALLENGE")
def calcul_rapide(a, b):
    startingTime = time.time()
    result = 1
    while b > 0:
        if b % 2 == 1:  # Si b est impair, on multiplie par a
            result *= a
        a *= a  # a devient a^2
        b //= 2  # On divise b par 2
    return result

# Mesure le temps de calcul pour 42^84
def calcul_rapide_function():
    startingTime = time.time()
    print(calcul_rapide(42, 84))
    duration = time.time()- startingTime
    print(f"Temps pour 42^84 : {duration} secondes")

calcul_rapide_function()
print("--------------------------------")

# 2.1
def is_palindrome(a):
    is_palindrome = 0
    for i in range(len(a)//2):
        if a[i] != a[-i-1]:
            is_palindrome = 0
        else:
            is_palindrome = 1
    if is_palindrome == 1:
        print("Je suis un Palindrome !")
    else:
        print("Je suis pas du tout un Palindrome !")

is_palindrome("kayak")
is_palindrome("brume")

print("--------------------------------")

# 2.2
def lister_fichiers_repertoires():
    # Chemin du répertoire à lister
    chemin = "C:/Users/utilisateur/Desktop/SUJETS MSCPRO/T-PRE-500_days/T-PRE-500_day6"
    
    print(f"Voici le contenu du répertoire auquel je travaille : {chemin}")
    
    # Afficher tous les fichiers et répertoires récursivement
    for dirpath, dirnames, filenames in os.walk(chemin):
        # Affiche le répertoire actuel
        print(f"Répertoire: {dirpath}")
        
        # Affiche les sous-répertoires
        if dirnames:
            print("Sous-répertoires :")
            for dirname in dirnames:
                print(f"  - {dirname}")
        
        # Affiche les fichiers
        if filenames:
            print("Fichiers :")
            for filename in filenames:
                print(f"  - {filename}")
        
        print()  # Saut de ligne pour séparer chaque répertoire
    
lister_fichiers_repertoires()
print("--------------------------------")

print(" - TACHE 3 - ")

# 3.1
def functions_regrouped():
    phrase = "Camembert au Poulet Rôti 123 !"
    nombre = 3
    print(function_a(phrase, nombre))
    print(function_b(phrase, nombre))
    print(function_c(phrase, nombre))
    print(function_d(phrase, nombre))
    print(function_e(phrase, nombre))
    
def function_a(n, s):
    minuscules = [char for char in n if char.islower()]
    if len(minuscules) == s:
        return True
    else: 
        return False

def function_b(n, s):
    majuscules = [char for char in n if char.isupper()]
    if len(majuscules) == s:
        return True
    else: 
        return False
def function_c(n, s):
    if len(n) == s :
        return True
    else:
        return False

def function_d(n, s):
    # Récupérer les caractères spéciaux dans la chaîne `n`
    caracteres_speciaux = [char for char in n if char in string.punctuation]
    if len(caracteres_speciaux) == s:
        return True
    else:
        return False
    
def function_e(n, s):
    chiffres = [char for char in n if char.isdigit()]
    if len(chiffres) == s :
        return True
    else:
        return False
    
functions_regrouped()
print("--------------------------------")

# 3.2, 3.3
def check_password(type, number, password):
    caracteres = 0
    if not password:
        print("Mot de passe vide...")
    elif not type : 
        print("Pas de type renseigné...")
    elif not isinstance(number, int):
        print("Pas de valeur renseigné...")
    else:
        if type == "lower":
            caracteres = [char for char in password if char.islower()]
        elif type == "upper":
            caracteres = [char for char in password if char.isupper()]
        elif type == "special":
            caracteres = [char for char in password if char in string.punctuation]
        elif type == "count":
            caracteres = len(password)
        elif type == "numbers":
            caracteres = [char for char in password if char.isdigit()]

        if len(caracteres) >= number:
            print("Mot de passe Valide !")
        else :
            print("Mot de passe invalide !")

check_password("lower", 4, "mysecretpassword") 
check_password("special", 2, "mysecretpassword")
check_password("", 2, "mysecretpassword")
check_password("special", "mysecretpassword", 0)
print("--------------------------------")
