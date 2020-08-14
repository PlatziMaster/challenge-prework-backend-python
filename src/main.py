# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def random_chars(elemnts, len_min, len_max):
    return random.choices(elemnts, k=random.randint(len_min, len_max))


def generate_password():
    pass_len_min = 8 // 4  # It is divided by the number of different possibilities
    pass_len_max = 16 // 4  # [ upper, lower, digits, symbols ] = 4

    upper = random_chars(string.ascii_uppercase, pass_len_min, pass_len_max)
    lower = random_chars(string.ascii_lowercase, pass_len_min, pass_len_max)
    digits = random_chars(string.digits, pass_len_min, pass_len_max)
    symbols = random_chars(string.punctuation, pass_len_min, pass_len_max)

    password_chars = upper + lower + digits + symbols

    # shuffle characters so as not to always have the same grouping
    # 1st upper's chars, 2nd lower's chars, 3st digits, 4st symbols.
    password = random.sample(password_chars, len(password_chars))
    return ''.join(password)


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
