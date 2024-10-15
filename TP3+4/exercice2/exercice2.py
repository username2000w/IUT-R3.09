from hashlib import sha512

def password_generate(master_password : str, tag : str, size : int) -> str:
    sha256_password: str
    res : str
    legal_character : int
    cutting_size : int

    res = ""
    legal_character = 0
    sha256_password =  sha512(master_password.encode() + tag.encode()).hexdigest()
    cutting_size = len(sha256_password)//size

    for i in range(0, size):
        char = sha256_password[cutting_size*i:cutting_size*i+cutting_size]
        for character in char:
            legal_character += ord(character)
        legal_character = (legal_character - 33) % 95 + 33

        res += chr(legal_character)

    return res


if __name__ == "__main__":
    print(password_generate("MotDePasse", "Unilim", 10))