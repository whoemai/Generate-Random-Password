import random
import string


def generate_password(length=20):
    characters = "-" + string.ascii_letters + "-" + "@" + string.digits + "-"
    password = ''.join(random.choice(characters) for i in range(length))
    return password


print(f"Your password gereta: {generate_password()}")
