import re
import random
def check_symbols (value):
    symbols_pattern = r"[<>, *&^%$#@! -=+'0-9]"
    symbols_found = re.findall (symbols_pattern, value)
    if len (symbols_found) > 2:
        return True 
    else:
        return False
def generate_password (value) :
    letters = '+-/*!&$#?=@<>abcdefghiiklnopgrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    value = ''
    for i in range (10):
        value += random. choice (letters)
    return value
def validate_password(value):
    password_length = len(value)
    if password_length > 8 and check_symbols(value):
        print("Your password is quite good! You can use it.")
    else:
        good_pass = generate_password (value)
        print(f"Your password is not good enough... May be try this one: {good_pass}")
value = input( 'Enter a password to check: ')
validate_password(value)
