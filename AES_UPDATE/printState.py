from Affiche import format_hex
import numpy as np

def printState(text):
    """Transforme un texte en cle et le met sous format 4*4"""
    key = ""
    for i in text:
        key+= format_hex(ord(i))
    return np.array([key[i:i+2] for i in range(0, len(key), 2)]).reshape((4,4), order='F')

def printStateInverse(message_chiffre):
    text = ""
    message_chiffre = message_chiffre.reshape(16, order='F')
    for i in message_chiffre:
        text+= chr(int(i, 16))
    return text

print(printState('this is one text'))