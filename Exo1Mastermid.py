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

