# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    # Obtener un número entre el 8 y 16
    characters_in_password = random.randint(8, 16);
    # Crear una lista de caracteres bajo los siguientes criterios
    
    # 2 números entre 0 y 30 (lista de símbolos) => 2 caracteres de la lista
    array_index_simbols = [random.randint(0, 27), random.randint(0, 27)]
    # 2 números entre 48 y 57 (ascii números) => 2 caracteres ascii
    array_index_ascii_numbers = [random.randint(48, 57), random.randint(48, 57)]
    # 2 números entre 65 y 90 (ascii letras mayúsculas) => 2 caracteres ascii
    array_index_ascii_upper_characters = [random.randint(65, 90), random.randint(65, 90)]
    # 2 números entre 97 y 122 (ascii letras minúsculas) => 2 caracteres ascii
    array_index_ascii_lower_characters = [random.randint(97, 122), random.randint(97, 122)]    
        
    # Obtener string    
    simbols_string = SYMBOLS[array_index_simbols[0]] + SYMBOLS[array_index_simbols[1]]
    numbers_string = chr(array_index_ascii_numbers[0]) + chr(array_index_ascii_numbers[1])
    upper_characters_string = chr(array_index_ascii_upper_characters[0]) + chr(array_index_ascii_upper_characters[1])
    lower_characters_string = chr(array_index_ascii_lower_characters[0]) + chr(array_index_ascii_lower_characters[1])

    # Verificar si no faltaron caracteres extra
    extra_simbols_string = ""   
    if characters_in_password > 8:
        # Si faltaron, añadir la cantidad restante de los símbolos
        length = characters_in_password - 8
        for x in range(length):
            symbol_index = random.randint(0,27)
            extra_simbols_string += SYMBOLS[symbol_index]
    
    # Crear un string aleatorio con los caracteres obtenidos
    password = simbols_string + numbers_string + upper_characters_string + lower_characters_string + extra_simbols_string
    shuffle_password = "".join(random.sample(password, len(password)))    
    
    print(shuffle_password)
    return shuffle_password


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
