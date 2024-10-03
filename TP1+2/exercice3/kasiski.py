from math import gcd
import os

def kasiski(nom_fichier : str) -> int:
    texte : str
    sous_chaines : dict[str, list[int]]
    sous_chaine : str
    longueur_sous_chaine_debut : int
    positions : list[int]
    distances : list[int]
    pgcd : int
    liste_pgcd : list[int]

    longueur_sous_chaine_debut = 3
    liste_pgcd = []

    fichier = open(os.path.join(os.path.dirname(__file__), nom_fichier), "r")
    texte = fichier.read()

    while True:
        if len(liste_pgcd) > 2:
            if liste_pgcd[-1] == liste_pgcd[-2] and liste_pgcd[-1] != 1:
                break

        sous_chaines = {}
        
        for i in range(len(texte) - longueur_sous_chaine_debut):
            sous_chaine = texte[i:i+longueur_sous_chaine_debut]
            if sous_chaine in sous_chaines:
                sous_chaines[sous_chaine].append(i)
            else:
                sous_chaines[sous_chaine] = [i]

        distances = []
        for sous_chaine in sous_chaines:
            positions = sous_chaines[sous_chaine]
            if len(positions) > 1:
                positions = sous_chaines[sous_chaine]
                for i in range(len(positions) - 1):
                    for j in range(i + 1, len(positions)):
                        distances.append(abs(positions[i] - positions[j]))

        distances = list(dict.fromkeys(distances))
        pgcd = gcd(*distances)
        liste_pgcd.append(pgcd)

        longueur_sous_chaine_debut += 1

    fichier.close()
    return liste_pgcd[-1]
    
if __name__ == "__main__":
    res = kasiski("kasiski.txt")
    print("La clé est de taille " + str(res))