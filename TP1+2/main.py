from exercice1.chiffre import chiffreVigenere
from exercice2.dechiffre import dechiffreVigenere
from exercice3.kasiski import kasiski

if __name__ == "__main__":
    texte_clair = "Bonjour"
    cle = "CLE"

    texte_chiffre = chiffreVigenere(texte_clair, cle)
    print(texte_chiffre)
    print(dechiffreVigenere(texte_chiffre, cle))

    texte_clair = "Je suis un chat rouge"
    cle = "FRAISE"

    texte_chiffre = chiffreVigenere(texte_clair, cle)
    print(texte_chiffre)
    print(dechiffreVigenere(texte_chiffre, cle))

    texte_clair = "La cle n'existe pas"
    cle = ""

    texte_chiffre = chiffreVigenere(texte_clair, cle)
    print(texte_chiffre)
    print(dechiffreVigenere(texte_chiffre, cle))

    texte_chiffre = "kasiski.txt"
    print(kasiski(texte_chiffre))