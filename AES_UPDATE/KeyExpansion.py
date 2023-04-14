import numpy as np
from Rcon import Rcon
from RotWord import RotWord
from SubWord import SubWord
from XordWord import XorWord
import Affiche



def keyExpansion(key):
    """S'occupe de cree l'expansion d'une cle en fonction des tours"""
    expended_key = np.array([int(key[i:i+2], 16) for i in range(0, len(key), 2)]).reshape((4,4), order='F')
    for i in range(1, 11):
        x = expended_key[:, -1] #Recuperre la derniere colonne de la cle
        x = RotWord(x)
        x = SubWord(x)
        x = XorWord(x, expended_key[:, -4])
        x = XorWord(x, Rcon(i))
        expended_key = np.c_[expended_key, x]
        for _ in range(3):
            expended_key = np.c_[expended_key, XorWord(expended_key[:, -1], expended_key[:, -4])]
    return expended_key

