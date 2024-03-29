
# Definition des variables
PIP := pip3
PYTHON := python3

# Installation des dépendances
install:
	$(PIP) install numpy

# Exécution du script python
attack:
	$(PYTHON) Attaque.py

encrypt:
	$(PYTHON) Chiffrement.py

decrypt:
	$(PYTHON) Dechiffrement.py

# Nettoyage des fichiers générés
clean:
	rm -rf __pycache__
	rm key.txt
  
# Faire une archive
LADIR=Projet_AES_Python

# Commande pour installer zip
#sudo apt-get install zip unzip

zip: 
	rm -rf ${LADIR}
	mkdir ${LADIR}
	cp Makefile ${LADIR}
	cp Attaque.py ${LADIR}
	cp Chiffrement.py ${LADIR}
	cp Dechiffrement.py ${LADIR}
	cp main.py ${LADIR}
	cp README.md ${LADIR}
	rm -f ${LADIR}.zip
	zip -r ${LADIR}.zip ${LADIR}
	rm -rf ${LADIR}
