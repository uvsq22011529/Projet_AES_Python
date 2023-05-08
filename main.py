print("Le mode interactif est en cours de chargement, veuillez patienter un instant.")

from Chiffrement import encrypt
from Chiffrement import printStateInverse
from Dechiffrement import decrypt
from Attaque import attaque, generate_key, setup


def interactive_mode():
    print("Bienvenue dans le mode intéractif!")
    choix = input("Que souhaitez-vous faire?\n Tapez 'c' pour chiffrer\n Tapez 'd' pour déchiffrer\n Tapez 'a' pour lancer une attaque\n Tapez 'q' pour quitter\n ")
    while choix not in ['c', 'd', 'a', 'q']:
        choix = input("Choix invalide.")
    if choix == 'q':
        return
    
    if choix == 'a':
        # Génére une clé aléatoire
        generate_key()
        with open("key.txt", "r") as f:
            cle = f.readline()

        # Crée les delta sets nécessaires pour lancer l'attaque
        deltats = [setup(cle) for _ in range(10)]

        # Lance l'attaque et affiche la clé retrouvée
        cle_trouvee = attaque(deltats)
        print("Clé trouvée par l'attaque :", cle_trouvee)
        return
    
    if choix == 'c':
        message = input("Entrez le message : ")
        cle = input("Entrez la clé : ")
        print('Le message chiffré obtenu est :', printStateInverse(encrypt(message, cle)))

    if choix == 'd':
        message = input("Entrez le message : ")
        cle = input("Entrez la clé : ")
        print(decrypt(message, cle))

    relancer = input("Voulez-vous relancer une commande ?\n Tapez Oui/Non.\n ")
    while relancer not in ['Oui', 'Non']:
        relancer = input("Choix invalide.")
    if relancer == 'Non':
        return
     
    interactive_mode()

if __name__ == '__main__':
    interactive_mode()
