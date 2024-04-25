import random


class Color:
    """Just add colors for strings.
    """
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class pretty_print:
    def __init__(self, text):
        pass

    def error(text):
        print(
            Color.BOLD, Color.RED,
            text,
            Color.END, sep="", end=2*"\n"
        )


def gen_password(password_lenght):
    """Generate a password, based on ASCII code list. The function returns
        a password string in UTF-8 that was converted from ASCII code.

    Args:
        password_lenght (str): The lenght of password that the user inputs

    Returns:
        str: generated password
    """

    # The map function maps every item of (chr, range()).
    # chr return a corresponding character of a conresponding ASCII code.
    # range(33,126) is the range on ASCII Table for UTF-8 characters, it includes
    # uppercase, lowercase, numbers and special charactes.
    # https://www.ascii-code.com
    ASCII_char_list = list(map(chr, range(33, 126)))
    generated_password = ""

    for i in range(password_lenght):
        rand_char = random.choice(ASCII_char_list)
        generated_password += rand_char

    return generated_password


def main_menu():
    ...


print(gen_password(16))
