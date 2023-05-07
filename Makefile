

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
  
