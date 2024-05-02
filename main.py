import random
import os

ASCII_ART = """\033[92m
                    ........
             .^7YPGBB######BBGPY7^.
           ^JGB####################BGJ^
        :YB############################BY:
       ^P##################################P^
     .P######################################P.
    !########BG5J???J5GB#######################!
   ?######G?^.         .^?G#####################?
  !#####G~                 ~G####################!
 .B####J         ...         Y###################B.
 ?####Y       !PB###BP!       JGGGGGGGGGGGGG######?
 G###B.      5#########5                    .J####G
 G###G      :#BBBBBB#BB#:                     B###G
 G###B.      5BBBBBBBB#5                    .J####G
 ?####Y       !5B##BBP!       JGGG!..     :BB#####?
 .B####J         ...         Y#####B#5    !######B.
  !#####G~                 ~G#########P??5B######!
   ?######G?^.         .^?G#####################?
    !########BG5J???Y5GB#######################!
     .P######################################P.
       ^P##################################P^
         :YB############################BY:
            ^JGB####################BGJ^
              .^7YPGBB######BBGPY7^.
                     ........


\033[0m"""


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


def cls():
    """ Clear the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')  # clear multiplataform


def boldGreenText(text):
    return f"{Color.BOLD}{Color.GREEN}{text}{Color.END}"


def boldRedText(text):
    return f"{Color.BOLD}{Color.RED}{text}{Color.END}"


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
        # Here we take random elements from ASCII_char_list
        rand_char = random.choice(ASCII_char_list)
        generated_password += rand_char

    return generated_password


def loop_handle():
    loop_control = input("Deseja gerar outra senha? [y/n]: ")

    if loop_control == "n" or loop_control == "N":
        print("\n Até mais !!")
        exit()
    elif loop_control == "y" or loop_control == "Y":
        cls()
        print(ASCII_ART)
        Execute()
    else:
        print(boldRedText(
            "Entrada inválida, favor digite apenas [y] ou [n]\n"))
        loop_handle()


def Execute():
    """Simply execute the program and return the generated password
    """
    while True:

        password_lenght_input = input(
            "Insira a quantidade de caracteres desejados para a senha: ")

        if password_lenght_input.isdigit():  # Here we are verifying if the user input is int type

            # Execute the gen_password function, and format it with PrettyPrint class
            generated_password = boldGreenText(
                gen_password(int(password_lenght_input)))

            print(f"\nA senha gerada é {generated_password}\n")

        else:
            print(
                boldRedText(
                    "Input inválido, por favor, insira apenas números inteiros positivos.\n")
            )
            continue

        loop_handle()


""" ################################################################################# """

print(ASCII_ART)

Execute()
