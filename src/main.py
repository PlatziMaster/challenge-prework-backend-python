# Resolve the problem!!
import string
import math
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')

def int_random_number(min, max):
    value = random.randint(min, max)
    return value

def generate_password():
    # Start coding here
    # 1.do
    #    1.1. Generate password length  (ok)
    #    1.2. for i = 0 to password_length (ok)
    #       1.2.1 Generate digit type
    #       1.2.2 Generate random digit
    #       1.2.3 concat to password
    #    1.3. Verify if password is secure
    #   while(password === insecure) 
    # 4. Return password

    password_length = int_random_number(8, 16)
    print(password_length)
    for x in range(password_length):
        type_digit = int_random_number(1, 4) 
        print(type_digit)

    password = 'PiPe(12)'
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
