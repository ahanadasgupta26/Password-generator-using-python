import random
import string

def genarate(minlen,num=True,splch=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation
    
    char=letters
    if num:
        char+=digits
    if splch:
        char+=special
    pwd=""
    crieria=False
    has_nums=False
    has_spl=False

    while not crieria or len(pwd)<minlen:
        new_char=random.choice(char)
        pwd+=new_char
        if new_char in digits:
           has_nums=True
        elif new_char in special:
           has_spl=True

        crieria=True
        if num:
            crieria=has_nums
        if splch:
            crieria=crieria and has_spl
    return pwd
   
def check_strength(pwd):
    length = len(pwd)
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(c in string.punctuation for c in pwd)
    
    if length >= 12 and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif length >= 8 and ((has_upper and has_lower) or (has_digit and has_special)):
        return "Moderate"
    else:
        return "Weak"


minlen=int(input("Enter the minimum length of your password: "))
has_nums=input("Do you want numbers in your password (y/n)? ").lower() == "y"
has_spl=input("Do you want special characters in your password (y/n)? ").lower() == "y"

while True:
    pwd=genarate(minlen, has_nums, has_spl)
    strength=check_strength(pwd)
    print("The generated password is:",pwd)
    print("Password strength:",strength)
    response = input("Do you want to regenerate the password (y/n)? ").lower()
    if response != "y":
        break