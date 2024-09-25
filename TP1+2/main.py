from exercice1.chiffre import chiffreVigenere
from exercice2.dechiffre import dechiffreVigenere

if __name__ == "__main__":
    texte_clair = "Bonjour"
    cle = "CLE"

    texte_chiffre = chiffreVigenere(texte_clair, cle)
    print(texte_chiffre)
    print(dechiffreVigenere(texte_chiffre, cle))