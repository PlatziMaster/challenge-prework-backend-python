# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    pwd_length = random.randint(8, 16)
    password = ''
    for i in range(pwd_length):
      password += randomChar(i)

    return password
      

def randomChar(cont):
    symbols = ''.join(SYMBOLS[0:len(SYMBOLS)])
    if(cont > 3):
      x = random.randint(0,3)
    else:
      x = cont
    if(x==0):
      return random.choice(string.ascii_lowercase)
    elif(x==1):
      return random.choice(string.ascii_uppercase)
    elif(x==2):
      return random.choice(string.digits)
    elif(x==3):
      return random.choice(symbols)


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