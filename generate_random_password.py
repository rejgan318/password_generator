import string
import secrets
from random import shuffle


def generate_random_password(length: int = 6, az: bool = True, az_upper: bool = True, num: bool = True,
                             symbol: bool = True, force: bool = True, masked: bool = False) -> str:
    """
    :param length: length of password
    :param az: use lowercase letters - not used, always True
    :param az_upper: use uppercase letters
    :param num: use numbers
    :param symbol: use symbols
    :param force: At least one character from the parameter sets is guaranteed
    :param masked: use all chars,  also special masked chars - ' " \
    :return: random password
    """

    MASKED_CHARS = "\"\'\\"     # Не знаю зачем это и почему именно такие символы :)
    # remove masked chars if needed
    punctuation = string.punctuation.translate({ord(c): None for c in MASKED_CHARS}) if masked else string.punctuation[:]

    alphabet = string.ascii_lowercase + \
               (string.ascii_uppercase if az_upper else "") + \
               (string.digits if num else "") + \
               (punctuation if symbol else "")
    result = []
    get_one_char = lambda source: secrets.choice(source)

    if force:
        if az:
            result.append(get_one_char(string.ascii_lowercase))
        if az_upper:
            result.append(get_one_char(string.ascii_uppercase))
        if num:
            result.append(get_one_char(string.digits))
        if symbol:
            result.append(get_one_char(punctuation))

    result.extend([secrets.choice(alphabet) for i in range(length - len(result))])
    shuffle(result)

    return ''.join(result)
