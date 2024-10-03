def dechiffreVigenere(texte_chiffre : str, cle : str) -> str:
    """Déchiffre un texte chiffré avec le chiffre de Vigenère

    Args:
        texte_chiffre (str): le texte chiffré
        cle (str): la clé de chiffrement

    Returns:
        str: le texte déchiffré
    """
    texte_clair : str
    char : str
    charCle : str
    max_ascii : int
    min_ascii : int
    intervalle : int

    max_ascii = 126
    min_ascii = 32
    intervalle = max_ascii - min_ascii + 1

    texte_clair = ""

    if len(cle) == 0:
        return "/!\\ La clé ne peut pas être vide /!\\"

    for i in range(0, len(texte_chiffre)):
        char = texte_chiffre[i]
        charCle = cle[i % len(cle)]

        texte_clair += chr((ord(char) - ord(charCle) + intervalle) % intervalle + min_ascii)

    return texte_clair

if __name__ == "__main__":
    print(dechiffreVigenere("e<4.<;6", "CLE"))