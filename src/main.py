# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')

OPCIONES = [SYMBOLS,list(range(65,90)),list(range(0,10))]
resultados = [0,0]

def generate_password():
    contrasena = ''
    size = random.randint(8,16)
    batch = int(size/4)
    for opcion in OPCIONES:
        sample = random.sample(opcion,batch)
        for  element in sample:
            try:
                if element >= 65:
                    contrasena += chr(element if random.randint(0,1) else element + 32)
                else:
                    contrasena += f"{element}"
            except:
                contrasena += element
    if(len(contrasena)<size):
        sample = random.sample(OPCIONES[1],size-len(contrasena))
        for element in sample:
            contrasena += chr(element + 32)
    print(contrasena)
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