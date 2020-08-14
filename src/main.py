# Resolve the problem!!
import string


def generate_password():
    # Start coding here
    pass


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
