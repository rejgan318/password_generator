import string
import secrets
from constants import DEFAULT_LENGTH


def generate_random_password(length: int = DEFAULT_LENGTH, az: bool = True, az_upper: bool = True, num: bool = True,
                             symbol: bool = True) -> str:
    """
    :param length: length of password
    :param az: use lowercase letters - not used, always True
    :param az_upper: use uppercase letters
    :param num: use numbers
    :param symbol: use symbols
    :return: random password
    """
    alphabet = string.ascii_lowercase + \
               (string.ascii_uppercase if az_upper else "") + \
               (string.digits if num else "") + \
               (string.punctuation if symbol else "")

    return ''.join(secrets.choice(alphabet) for i in range(length))
