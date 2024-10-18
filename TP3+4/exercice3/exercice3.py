from hashlib import sha512
import os

def password_generate(tag : str, size : int) -> str:
    sha512_password: str
    res : str
    legal_character : int
    cutting_size : int

    res = ""
    legal_character = 0

    file = os.path.join(os.path.dirname(__file__), "mpwd.txt")
    try:
        with open(file, "r") as f:
            master_password = f.read()
            f.close()
    except FileNotFoundError:
        with open(file, "w") as f:
            f.write("MotDePasse")
            f.close()
        with open(file, "r") as f:
            master_password = f.read()
            f.close()

    sha512_password =  sha512(master_password.encode() + tag.encode()).hexdigest()
    cutting_size = len(sha512_password)//size

    for i in range(0, size):
        char = sha512_password[cutting_size*i:cutting_size*i+cutting_size]
        for character in char:
            legal_character += ord(character)
        legal_character = (legal_character - 33) % 95 + 33

        res += chr(legal_character)

    return res


if __name__ == "__main__":
    print(password_generate("Unilim", 8))