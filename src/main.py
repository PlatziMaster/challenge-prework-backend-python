# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    # Esta sera la manera en que se obtendra un numero aleatorio entre 8 y 16 para poder generar la contraseña con ese numero de caracteres.
    random_number = random.choice(list(range(8, 17)))

    password = ''

    i = 0
    while i < random_number:
        # Se generara una contraseña con un total de caracteres entre 8 y 16.
        password += random.choice(string.ascii_letters)
        i += 1

    print('password length: ', len(password))

    secure_password = list(password)

    # Se agregaran symbolos cuando esta iteracion se encuentre con numeros pares.
    for i in range(0, len(password)):
       if i % 2 == 0:
            secure_password[random.choice(range(0, len(password)))] = random.choice(SYMBOLS)

    # Se agregaran algunos numeros a la contraseña.
    for char in secure_password:
        if char in SYMBOLS:
            if secure_password.index(char) % 2 != 0:
                secure_password[secure_password.index(char)] = random.choice(string.digits)
            else:
                secure_password[len(password) - 1] = random.choice(string.digits)
    
    print('final password:', ''.join(secure_password))
    return ''.join(secure_password)

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
