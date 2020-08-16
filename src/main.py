# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')

OPCIONES = [SYMBOLS,lambda:random.randint(65,90),lambda:random.randint(0,9)]
resultados = [0,0]

def generate_password():
    contrasena = ''
    while (len(contrasena) < 16):
        choiced = random.choice(OPCIONES)
        if callable(choiced):
            character = choiced()
            if(character>64):
                contrasena += chr(character if random.choice(range(0,9))<7 else character + 32)
            else:
                contrasena += f'${character}'
            
        else:
            contrasena += random.choice(choiced)
    return contrasena


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
        #print('Secure Password')
        resultados[0] += 1
    else:
        #print('Insecure Password')
        resultados[1] += 1


if __name__ == '__main__':
    for intento in range(10000):
        run()
    print(f'secure: {resultados[0]} insecure: {resultados[1]}')