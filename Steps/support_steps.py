import random
import string


def generate_random_string(length):
    random_string = ""
    for i in range(length):
        random_string += random.choice(string.ascii_letters[random.randint(0, 5)])
    return random_string
