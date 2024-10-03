def chiffreVigenere(texte_clair : str, cle: str) -> str:
    """Chiffre un texte en utilisant le chiffre de Vigenère

    Args:
        texte_clair (str): le texte à chiffrer
        cle (str): la clé de chiffrement

    Returns:
        str: le texte chiffré
    """
    texte_chiffre : str
    char : str
    charCle : str
    max_ascii : int
    min_ascii : int
    intervalle : int

    max_ascii = 126
    min_ascii = 32
    intervalle = max_ascii - min_ascii + 1

    texte_chiffre = ""

    if len(cle) == 0:
        return "/!\\ La clé ne peut pas être vide /!\\"

    for i in range(0, len(texte_clair)):
        char = texte_clair[i]
        charCle = cle[i % len(cle)]

        texte_chiffre += chr((ord(char) + ord(charCle) - 2 * min_ascii) %intervalle + min_ascii)

    return texte_chiffre

if __name__ == "__main__":
    print(chiffreVigenere("BONJOUR", "CLE"))