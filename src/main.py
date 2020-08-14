# Resolve the problem!!
import string
import random


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


def validate_chars(chars_set, word):
    for char in word:
        if char in chars_set:
            return True


def validate(password):
    if len(password) >= 8 and len(password) <= 16:

        has_lowercase = validate_chars(string.ascii_lowercase, password)
        has_uppercase = validate_chars(string.ascii_uppercase, password)
        has_numbers = validate_chars(string.digits, password)
        has_symbols = validate_chars(string.punctuation, password)

        if has_symbols and has_numbers and has_lowercase and has_uppercase:
            return password


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
