import random
import string

def generate_random_number(start, end):
  
    if start > end:
        start, end = end, start 
    return random.randint(start, end)

def generate_random_password(length=12):
    
    if length <= 0:
        return "Password length must be positive."
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password


