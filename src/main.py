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
    print('hex to ascii')
    # hex_string = "616263"[0:]
    # hex_string = hex_string[0:]
    # print(hex_string)
    bytes_object = bytes.fromhex(hex_string)
    # print(bytes_object)
    ascii_string = bytes_object.decode("ASCII")
    # print(ascii_string)
    # print(type(ascii_string))
    # str_password = str(ascii_string, 'utf-8')
    # print(type(str_password))
    return ascii_string


def generate_password():
    # Start coding here
    # 1.do
    #    1.1. Generate password length  (ok)
    #    1.2. for i = 0 to password_length (ok)
    #       1.2.1 Generate digit type (ok)
    #       1.2.2 Generate random digit (ok)
    #       1.2.3 Generate hex password  (ok)       
    #       1.2.4 concat to password (ok)
    #       1.2.5 hex to ascii
    #    1.3. Verify if password is secure
    #   while(password === insecure) 
    # 4. Return password

    hex_password = ''
    password_length = int_random_number(8, 16)
    print(password_length)

    for x in range(password_length):
        digit_type = int_random_number(1, 4) 
        new_digit = become_type_to_ascii(digit_type)
        str_digit = str(new_digit)
        hex_password = hex_password + str_digit 

    password = password_hex_to_ascii(hex_password)
    print(password)
    print(type(hex_password))
    
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
    print(password)
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
