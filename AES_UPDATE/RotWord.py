import numpy as np

def RotWord(tab):
    """Fait une rotation des 4 octets

    Args:
        tab (int): valeur de 4 octets

    Returns:
        int: rotation des 4 octets
    """
    return np.roll(tab,-1)
