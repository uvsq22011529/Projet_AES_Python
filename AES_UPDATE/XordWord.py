import numpy as np

def XorWord(tab1, tab2):
    """Retourne le Xor entre les 2 element"""
    return np.array([tab1[i]^tab2[i] for i in range(4)])