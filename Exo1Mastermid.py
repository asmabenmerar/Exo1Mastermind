import random


# Etape 1 : Preparation
# Constantes du jeu
combin_length = 4
nmbr_tentative = 10
colors = ['R', 'G', 'B', 'Y', 'O', 'P']




#Etape 2 :Génération de la Combinaison Secrète
# Fonction pour générer la combinaison secrète
def combinaison_secrete():
    return random.choices(colors, k=combin_length)  # Utilisation de random.choices


#Etape 3 : Interaction Joueur 
# Fonction pour récupérer la proposition de l'utilisateur
def get_position_user():
    while True:
        # Demande la saisie de l'utilisateur et la convertit en majuscules
        saisie_uti = input(f"Entrez votre combinaison ({combin_length} lettres parmi {', '.join(colors)}): ").upper()

        # Vérification de la longueur
        if len(saisie_uti) != combin_length:
            print(f"Erreur: Vous devez entrer exactement {combin_length} lettres.")
            continue  # Demande à nouveau la saisie

        # Vérification des caractères valides
        if not all(color in colors for color in saisie_uti):
            print(f"Erreur: Votre combinaison ne doit contenir que les lettres parmi {', '.join(colors)}.")
            continue  # Demande à nouveau la saisie

        # Si tout est valide, on retourne la combinaison sous forme de liste
        return list(saisie_uti)


#Etape 4 : Vérification de la Proposition
def verifier_proposition(proposition,solution):
    # compter les biens placés

    bien_placee = sum([1 for index in range (combin_length) if proposition[index] == solution[index]])

    # identifier les mal placés
    proposition_mal_placee = []
    solution_mal_placee = []

    for index in range (combin_length):
        if proposition[index] != solution[index]:
            proposition_mal_placee.append(proposition[index])
            solution_mal_placee.append(solution[index])

    # calculer les mal placés
    mal_placee = 0
    for color in proposition_mal_placee :
        if color in solution_mal_placee:
            mal_placee +=1
            solution_mal_placee.remove(color) # retirer l'element de la solution pour eviter de le compter flsr fois
    return bien_placee, mal_placee