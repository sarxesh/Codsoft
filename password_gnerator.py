import random
import string

def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    all_chars = lowercase + uppercase + digits + symbols
    
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    
    random.shuffle(password)
    
    return ''.join(password)

while True:
    try:
        length = int(input("Enter the desired password length (minimum 8 characters): "))
        if length < 8:
            print("Password length should be at least 8 characters for security.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

password = generate_password(length)
print("\nGenerated Password:", password)
