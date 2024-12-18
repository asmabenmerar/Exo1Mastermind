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




    #Etape 5 et 6

    # fonction principale de jeu

def jeu_mastermind():
# initialiser le jeu
    secret_combination = combinaison_secrete()
    tentative_restante = nmbr_tentative
    victoire = False

    # instruction de jeu
    print(" Bienvenue dans le jeu Mastermind")
    print("Le but est de deviner une combinaison secréte de couleurs.")
    print(f"Vous devez deviner une combinaison de {combin_length} parmis les suivantes: {', '.join(colors)}. ")
    print(f"Chaque lettre repésente une couleur parmis celle listées")
    print(f"Vous avez {tentative_restante} tentative pour trouvez la bonne combinaison.")

#boucle (tant que le joueur n'a pas gagné et il reste des tentatives)
    while tentative_restante > 0 and not victoire :
        print(f"\n Il vous reste {tentative_restante} tentatives.")

        #Récupérer la proposition de l'utilisateur
        player_guess = get_position_user()
        print(f"Votre proposition : {player_guess}")

        #verifier de la proposition
        bien_placee, mal_placee = verifier_proposition(player_guess,secret_combination)

        # afficher les resultats
        print(f"Proposition: {''.join( player_guess)}")
        print(f"Bien placés:{bien_placee},Mal placés: {mal_placee}")

        #indication visuelles
        print("Indications:"+"*"* bien_placee +"-"* mal_placee)


        # verification de la victoire
        if bien_placee == combin_length:
             victoire = True
             print(f"Felicitation! Vous avez trouvé la bonne combinaison: {secret_combination}")
        else:
            tentative_restante -= 1

    #Gestion de fin de partie
    if not victoire:
        print(f"\n Dommage!Vous avez epuisez toutes les tentatives.la combinaison secréte était{secret_combination}. ")
        print("Essayer à nouveau pour ameliorer la stratégie")






  

if __name__ == "__main__":
   # Execution de jeu
   jeu_mastermind()





    