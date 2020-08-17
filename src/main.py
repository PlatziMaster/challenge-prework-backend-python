# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
PASSWORD_TYPE_CHAR = ["upper_char", "number", "lower_char", "symbol"]

# LAMBDA FUNCTIONS

generate_number = lambda: random.choice(string.digits)

generate_lower_char = lambda: random.choice(string.ascii_lowercase)

generate_upper_char = lambda: random.choice(string.ascii_uppercase)

generate_symbol = lambda: random.choice(SYMBOLS)

def generate_forth_random_positions(positions):
    random_positions = set()
    while len(random_positions) < 4:
        random_positions.add(random.randrange(positions))
    return random_positions

def generate_password():
    # Start coding here

    password_length = random.randint(8, 16)
    random_positions = list(sorted(generate_forth_random_positions(password_length)))
    password_generated = [False] * password_length
    
    for i in range(len(random_positions)):
        pos = random_positions[i]
        char_type = PASSWORD_TYPE_CHAR[i]
        password_generated[pos] = char_per_string(char_type)

    for index in range(password_length):
        if password_generated[index] == False:
            password_generated[index] = char_per_string(PASSWORD_TYPE_CHAR[random.randint(0, 3)])

    string_password = ''.join(password_generated)

    return string_password

def char_per_string(value):
    if value == PASSWORD_TYPE_CHAR[0]:
        return generate_lower_char()

    if value == PASSWORD_TYPE_CHAR[1]:
        return generate_upper_char()

    if value == PASSWORD_TYPE_CHAR[2]:
        return generate_number()

    if value == PASSWORD_TYPE_CHAR[3]:
        return generate_symbol()

    return False

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
        return True
    else:
        print('Insecure Password')
        return False

if __name__ == '__main__':
    run()
