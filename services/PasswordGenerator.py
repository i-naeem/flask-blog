import string
import random


class PasswordGenerator:
    def __init__(self, password_length: int):
        self.length = password_length
        self.characters = string.ascii_letters

    def generate(self):
        passwd = ""
        for _ in range(self.length):
            passwd = passwd + random.choice(self.characters)

        return passwd
