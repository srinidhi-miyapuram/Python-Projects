import random

# Generating the password
def generate_password(length=14):
    word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789()[]*&^#$@!-_,./<>"
    password = ''.join(random.choice(word) for i in range(length))
    return password

# Checking password strength

def password_strength(password):
    characters = {
        'length': len(password) >= 8,
        'lowercase': any(char.islower() for char in password),
        'uppercase': any(char.isupper() for char in password),
        'digit': any(char.isdigit() for char in password),
        'symbols': any(char in '()[]*&^#$@!-_,./<>' for char in password),
    }
    return sum(characters.values())


if __name__ == '__main__':
    password = generate_password(12)
    strength = password_strength(password)
    print(f"\nThe password is \n {password}\n and it's strength is {strength}")