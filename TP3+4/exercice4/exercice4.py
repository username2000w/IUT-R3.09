from hashlib import sha512
import itertools

def password_generate(master_password : str, tag : str, size : int) -> str:
    sha512_password: str
    res : str
    legal_character : int
    cutting_size : int

    res = ""
    legal_character = 0
    sha512_password =  sha512(master_password.encode() + tag.encode()).hexdigest()
    cutting_size = len(sha512_password)//size

    for i in range(0, size):
        char = sha512_password[cutting_size*i:cutting_size*i+cutting_size]
        for character in char:
            legal_character += ord(character)
        legal_character = (legal_character - 33) % 95 + 33

        res += chr(legal_character)

    return res



# --------------------------------------------------------------------------------------------- #

def brute_force(size : int) -> str:
    password_to_find_unilim = password_generate("MotDePasse", "Unilim", size)
    password_to_find_netflix = password_generate("MotDePasse", "Netflix", size)
    password_to_find_amazon = password_generate("MotDePasse", "Amazon", size)

    compteur = 0

    for i in range(33, 126):
        for j in range(33, 126):
            for k in range(33, 126):
                for l in range(33, 126):
                    for m in range(33, 126):
                        for n in range(33, 126):
                            for o in range(33, 126):
                                for p in range(33, 126):
                                    for q in range(33, 126):
                                        for r in range(33, 126):
                                            compteur += 1
                                            a = chr(i) + chr(j) + chr(k) + chr(l) + chr(m) + chr(n) + chr(o) + chr(p) + chr(q) + chr(r)
                                            brute_unilim = password_generate(a, "Unilim", size)
                                            brute_netflix = password_generate(a, "Netflix", size)
                                            brute_amazon = password_generate(a, "Amazon", size)

                                            if compteur % 1000000 == 0:
                                                print(str(compteur))
                                            if password_to_find_unilim == brute_unilim and password_to_find_netflix == brute_netflix and password_to_find_amazon == brute_amazon:
                                                print(password_to_find_unilim + "\t" + password_to_find_netflix + "\t" + password_to_find_amazon)
                                                return "Collisions trouvées : " + a + "en " + str(compteur) + " tentatives"
    return "Pas de colisions trouvées"

def brute_force_mieux(size: int) -> str:
    password_to_find_unilim = password_generate("MotDePasse", "Unilim", size)
    password_to_find_netflix = password_generate("MotDePasse", "Netflix", size)
    password_to_find_amazon = password_generate("MotDePasse", "Amazon", size)

    compteur = 0
    char_range = [chr(i) for i in range(33, 126)]  # Pré-génération des caractères possibles

    # Utilisation d'itertools.product pour générer toutes les combinaisons de taille 10
    for comb in itertools.product(char_range, repeat=10):
        compteur += 1
        a = ''.join(comb)
        
        brute_unilim = password_generate(a, "Unilim", size)
        brute_netflix = password_generate(a, "Netflix", size)
        brute_amazon = password_generate(a, "Amazon", size)

        if compteur % 1000000 == 0:
            print(str(compteur))
        
        # Vérification des collisions
        if (password_to_find_unilim == brute_unilim and 
            password_to_find_netflix == brute_netflix and 
            password_to_find_amazon == brute_amazon):
            print(f"{password_to_find_unilim}\t{password_to_find_netflix}\t{password_to_find_amazon}")
            print(f"Collisions trouvées : {a} en {compteur} tentatives")
            return f"Collisions trouvées : {a} en {compteur} tentatives"
    print("Pas de collisions trouvées")
    return "Pas de collisions trouvées"



if __name__ == "__main__":
    brute_force_mieux(2)