# Resolve the problem!!
import string
import random as rd


SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
LETTERS_CAPS = string.ascii_uppercase #Generates all the ascii uppercase letters
LETTERS = string.ascii_lowercase #Generates all the ascii lowercase letters
NUMBERS = list('0123456789') 
LISTS_NAMES = [NUMBERS, LETTERS_CAPS, LETTERS, SYMBOLS]

def generate_password():
    chars_qty = rd.randint(8, 16) #gets a random number between 8 and 16. This number will be password lenght
    psswd = "" #Empty string initilized
    list_selector = 0 #changes the list from where the character will be taken to ensure that password contains elements from all lists
    for _ in range(chars_qty): #iterates the number of times chars_qty indicates
        char = rd.choice(LISTS_NAMES[list_selector]) #gets a random char from the list that the index indicates
        psswd += char #add the new char to the password
        list_selector +=1 #sum 1 to list selector so next time gets the randomchar from another list
        if list_selector == 4: #reset list_selector
            list_selector = 0 
    
    return psswd
    # Start coding here


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
