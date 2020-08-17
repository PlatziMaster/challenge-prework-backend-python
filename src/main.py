# Resolve the problem!!
import string
import random
import string
import os

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    # Start coding here
    # password = ''.join(random.choice(string.ascii_uppercase + string.digits +
    #                                  "".join(SYMBOLS) + string.ascii_lowercase)
    #                                  for x in range(15))
    length = 16
    chars = string.ascii_letters + string.digits + "".join(SYMBOLS) + string.ascii_lowercase + string.ascii_uppercase
    random.seed = (os.urandom(1024))
    password = ''.join(random.choice(chars) for i in range(length))
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
