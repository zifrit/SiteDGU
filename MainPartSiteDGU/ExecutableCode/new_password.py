import secrets
import string


def new_password(count: int = 10):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(count))
    return password
