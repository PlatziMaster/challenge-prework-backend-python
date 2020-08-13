# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')

def randomNum(i, j):
    return random.randint(i, j)

def swGet(passwordGn):
    selection = randomNum (1, 4)
    if selection == 1:
        passwordGn = passwordGn + chr(random.randint(48, 57))
    elif selection == 2:
        passwordGn = passwordGn + chr(random.randint(65, 90))
    elif selection == 3:
        passwordGn = passwordGn + chr(random.randint(97, 122))
    elif selection == 4:
        passwordGn = passwordGn + SYMBOLS[randomNum(0, len(SYMBOLS) - 1)]
    return passwordGn
    # ,random.randint(48, 57))

def generate_password():
    randomNumber = randomNum(8, 16)
    validation = False
    while validation == False:
        passwordGn = ''
        for i in range (0, randomNumber):
            passwordGn = swGet(passwordGn)
        if validate(passwordGn):
            validation = validate(passwordGn)
    return passwordGn

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
