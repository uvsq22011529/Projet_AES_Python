from Chiffrement import encrypt
from Chiffrement import printStateInverse
from Dechiffrement import decrypt
from Attaque import attaque

def interactive_mode():
    print("Bienvenue dans le mode intératif!")
    choix = input("Que souhaitez-vous faire?\n Tapez 'c' pour chiffrer\n Tapez 'd' pour déchiffrer\n Tapez 'q' pour quitter\n ")
    while choix not in ['c', 'd', 'q']:
        choix = input("Choix invalide.")
    if choix == 'q':
        return
    
    message = input("Entrez le message : ")
    cle = input("Entrez la clé : ")
    
    if choix == 'c':
        print('Le message chiffré obtenu est :', printStateInverse(encrypt(message, cle)))

    if choix == 'd':
        print(decrypt(message, cle))

if __name__ == '__main__':
    interactive_mode()
