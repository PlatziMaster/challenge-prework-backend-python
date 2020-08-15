# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
LOWERCASE = list('abcdefghijklmnopqrstuvwxyz')
UPPERCASE = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
NUMBERS = list('0123456789')


def lista_random():
    global SYMBOLS, LOWERCASE, UPPERCASE, NUMBERS

    listas = [SYMBOLS, LOWERCASE, UPPERCASE, NUMBERS]
    lista = random.choice(listas)
    return lista


def generate_password():
    # Start coding here
    password = ''
    pdw_len = random.randint(8,16)

    for idx in range(pdw_len):
        if idx != pdw_len:
            lista = lista_random()
            password += random.choice(lista)
    
    print('su password es:', password)
    
    return password


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
