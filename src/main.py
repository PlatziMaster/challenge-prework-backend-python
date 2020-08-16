# Resolve the problem!!
import string
import random

UPLETTERS = list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')
LOWLETTERS = list('abcdefghijklmnñopqrstuvwxyz')
NUMBERS = list('1234567890')
SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    longer = random.randint(8, 16)
    password = []

    values = list(UPLETTERS + LOWLETTERS + NUMBERS + SYMBOLS)
    test_validation = False

    while test_validation == False:
        for _ in range(longer):
            password.append(random.choice(values))
        
            contraseña = ''.join(password)
        
        test_validation = validate(contraseña)

        if test_validation == False:
            password = []

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
