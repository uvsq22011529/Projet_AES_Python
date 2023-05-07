# Projet_AES_Python

## Implémenter le chiffrement et le déchiffrement de l’AES avec une clé de 128 bits.

## Implementation de l'attaque intégrale (ou encore attaque par saturation ou square attack) sur 4 tours de ce chiffrement, car il n'existe pas d'attaques "efficaces" connues sur l'AES complet.


Nous avons implementé le chiffrement par bloc de l'AES qui prend en entrée un message de 128 bits et retourne en sortie un chiffré de 128 bits également.

Le code a été fait avec la version 3.9 de python, il est donc conseillé d'utiliser une version semblable ou ulterieure.

## Prérequis : 

Il faudra installer la bibliothéque numpy afin d'executer le code avec la commande __make install__.


## Utilisation
Afin d'executer le code, voici les commandes pour teste avec Makefile : 

* make install > installe les librairies utilisées
* make attack > lance l'attaque
* make encrypt > lance le chiffrement 
* make decrypt > lance le dechiffrement 
* make clean > efface les fichiers cache
