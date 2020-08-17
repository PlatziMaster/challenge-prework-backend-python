# Resolve the problem!!
import random
import string

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')

def generate_password(size = 16, characters=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(characters) for _ in range(size))


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
        print(generate_password())
    else:
        print('Insecure Password')
        print(generate_password())


if __name__ == '__main__':
    run()
