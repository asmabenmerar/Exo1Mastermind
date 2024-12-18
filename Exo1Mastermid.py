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
