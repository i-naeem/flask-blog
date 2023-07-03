import string
import random

MIN_CHARACTERS = 6
MAX_CHARACTERS = 64


class PasswordGenerator:
    def __init__(self, password_length: int):

        self.characters = string.ascii_letters

        if password_length <= MIN_CHARACTERS:
            password_length = MIN_CHARACTERS
        elif password_length >= MAX_CHARACTERS:
            password_length = MAX_CHARACTERS
        else:
            password_length = password_length

        self.length = password_length

    def generate(self):
        passwd = ""
        for _ in range(self.length):
            passwd = passwd + random.choice(self.characters)

        return passwd
