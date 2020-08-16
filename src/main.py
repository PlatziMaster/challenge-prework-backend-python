# Resolve the problem!!
import string
import random # Here we call the random library in order to use the randon.choice method

MAY = list('ABCDEGHIJKLMNOPQRSTUVWXYZ')
MIN = list('abcdefghijklmnopqrstuvwxyz')
NUMBERS = list('1234567890')
SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~') # Here we have the list of avaible characters for building a secure password


def generate_password():
    
    character = MAY + MIN + NUMBERS + SYMBOLS # Here we define a variable which contains the previous lists from which random.choice will be able to choose from
    keygen = [] # Here we have an open list, which we will use to feel the password

    for i in range(12): # We predefined a password with a char length of 12. This loop help us to build the secure password. 
        random_character = random.choice(character) # The random.choice sets a random character on each iteration on our keygen list.
        keygen.append(random_character) # We use the .append method to fill our keygen list with the choosen character from teh random.choice method

    keygen = "".join(keygen) # We use the .join method to turn the keygen list into a clean string
    return keygen # Here we return a clean password

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
    print(password) # Just a print statement only to see if our program runs smoothley 
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
