import numpy as np

def format_hex(entier):
    "fonction qui met en format str notre hexa"
    temp = hex(entier)[2:]
    if len(temp) == 1:
        temp = '0' + temp
    return temp

def affiche_mat(matrice):
    ligne = []
    for elem in matrice:
        colonne = []
        for i in elem:
            colonne.append(format_hex(i))
        ligne.append(colonne.copy())

    print(np.array(ligne))