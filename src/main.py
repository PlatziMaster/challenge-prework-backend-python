# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    # Start coding here
    pass_symbol = ''.join((random.choice(SYMBOLS) for i in range(1)))
    pass_number = format(random.sample(range(0, 9), 1)).strip('[]')
    str_random = ''.join((random.choice(string.ascii_letters) for i in range(5)))
    str_upp = ''.join((random.choice(string.ascii_uppercase) for i in range(1)))
    pass_w = pass_symbol + pass_number + str_random + str_upp +pass_number
    return (pass_w)


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
