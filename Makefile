

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
	$(PYTHON) Déchiffrement.py

# Nettoyage des fichiers générés
clean:
	rm -rf __pycache__
  
# Faire une archive
LADIR="Projet_Crypto_AES"

zip:
	rm -rf ${LADIR}
	mkdir ${LADIR}
	cp Makefile ${LADIR}
	cp Attaque.py ${LADIR}
	cp Chiffrement.py ${LADIR}
	cp Déchiffrement.py ${LADIR}
	rm -f ${LADIR}.zip
	zip -r ${LADIR}.zip ${LADIR}
	rm -rf ${LADIR}
