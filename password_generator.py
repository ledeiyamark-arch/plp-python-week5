import random
import string


def make_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password