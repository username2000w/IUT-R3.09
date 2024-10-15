from hashlib import sha256

def password_generate(master_password : str, tag : str) -> str:
    sha256_password: str
    res : str
    legal_character : int

    res = ""
    legal_character = 0

    sha256_password =  sha256(master_password.encode() + tag.encode()).hexdigest()

    for i in range(0, 8):
        char = sha256_password[8*i:8*i+8]
        for character in char:
            legal_character += ord(character)
        legal_character = (legal_character - 33) % 95 + 33

        res += chr(legal_character)

    return res


if __name__ == "__main__":
    print(password_generate("MotDePasse", "Unilim"))