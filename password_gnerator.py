import random
import string

def generate_password(length=12):
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$&*()_"

    all_characters = lower_case + upper_case + digits + special_chars

    password = [
        random.choice(lower_case),
        random.choice(upper_case),
        random.choice(digits),
        random.choice(special_chars)
    ]

    password += random.choices(all_characters, k=length-4)

    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    print("Generated password is")
    print(generate_password(length=10))
