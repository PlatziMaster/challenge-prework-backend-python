# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
abcLower = list('abcdefghijklmnopqrstwxyz')
abcUpper = list('ABCDEFGHIJKLMNOPQRSTWXYZ1234567890')
NUMBERS = list('1234567890')


def generate_password():
    contraseña = ""
    for i in range(4):
        contraseña += random.choice(abcLower)
    
    for i in range(4):
        contraseña += random.choice(abcUpper)

    for i in range(4):
        contraseña += random.choice(SYMBOLS)

    for i in range(4):
        contraseña += random.choice(NUMBERS)
    
    return contraseña

def validate(password):
    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
