# Projet_AES_Python

## Implémentation du chiffrement et déchiffrement de l’AES avec une clé de 128 bits, ainsi que de sa cryptanalyse.

Nous avons implémenté le chiffrement par bloc AES qui prend en entrée un message de 256 bits et retourne en sortie un message chiffré de 256 bits également.

Ainsi qu'une attaque intégrale (également appelée attaque par saturation ou square attack) sur 4 tours de ce chiffrement, car il n'existe pas d'attaques "efficaces" connues sur l'AES complet. (contre 10 tours au total)

Le code a été écrit avec la version 3.9 de python, il est donc conseillé d'utiliser une version semblable ou ultérieure.

## Prérequis : 

Il faudra installer la bibliothèque numpy avec la commande __make install__ afin de pouvoir exécuter le code.


## Utilisation
Afin d'exécuter le code, voici les commandes pour effectuer les tests avec Makefile : 

* make install > installe les librairies utilisées
* make encrypt > lance le chiffrement 
* make decrypt > lance le dechiffrement 
* make attack > lance l'attaque
* make clean > efface les fichiers cache

Notre programme dispose également d'un mode interactif permettant à l'utilisateur de choisir la commande qu'il souhaite lancer.

* 'c' > afin de lancer un chiffrement
* 'd' > afin de lancer un déchiffrement
* 'a' > afin de lancer une attaque 
* 'q' > afin de quitter l'interface interactive

Des arguments lui sont également demandés (Texte et Clé à utiliser) s'il souhaite lancer un Chiffrement/Déchiffrement. Dans le cas où il souhaite lancer une attaque, la clé utilisée pour le chiffrement est générée aléatoirement et stockée dans le fichier 'key'.
