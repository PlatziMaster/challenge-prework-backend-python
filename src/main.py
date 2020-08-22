# Resolve the problem!!
import string
import math
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')

def int_random_number(min, max):
    value = random.randint(min, max)
    return value

def become_type_to_ascii(digit_type):
    if digit_type == 1:
        rand_symbol = int_random_number(1, 6)
        return rand_symbol + 20
    elif digit_type == 2:
        rand_number = int_random_number(1, 9)
        return rand_number + 30
    elif digit_type == 3:
        rand_upper = int_random_number(1, 9)
        return rand_upper + 40
    else:
        rand_lower = int_random_number(1, 9)
        return rand_lower + 60

def password_hex_to_ascii(hex_string):
    bytes_object = bytes.fromhex(hex_string)
    ascii_string = bytes_object.decode("ASCII")
    return ascii_string


def generate_password():
    # Start coding here
    
    while True:
        hex_password = ''
        password_length = int_random_number(8, 16)

        for x in range(password_length):
            digit_type = int_random_number(1, 4) 
            new_digit = become_type_to_ascii(digit_type)
            str_digit = str(new_digit)
            hex_password = hex_password + str_digit 

        password = password_hex_to_ascii(hex_password)

        if validate(password):
            break

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
