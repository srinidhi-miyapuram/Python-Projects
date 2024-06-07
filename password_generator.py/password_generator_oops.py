import random

class PasswordGenerator:
    def __init__(self, length = 14):
        self.length = length
        self.password = ""
        self.strength = ""
        self.__generate_password()
        self.__password_strength()
        self.display_password()
    
    def __generate_password(self):
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789()[]*&^#$@!-_,./<>"
        self.password = ''.join(random.choice(letters) for i in range(self.length))

    def __password_strength(self):
        characters = {
            'length': len(self.password) >= 8,
            'lowercase': any(char.islower() for char in self.password),
            'uppercase': any(char.isupper() for char in self.password),
            'digit': any(char.isdigit() for char in self.password),
            'symbols': any(char in '()[]*&^#$@!-_,./<>' for char in self.password),
        }
        self.strength = sum(characters.values())
    
    def display_password(self):
        print(f"\nThe password is \n {self.password}\n and the password strength is {self.strength}")

if __name__ == '__main__':
    password_class = PasswordGenerator()