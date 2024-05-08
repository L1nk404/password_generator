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
    """
    Adiciona cor as strings
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
    """ Limpa o terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')  # clear multiplataform


def boldGreenText(text):
    """ Printa o texto na cor verde """
    return f"{Color.BOLD}{Color.GREEN}{text}{Color.END}"


def boldRedText(text):
    """ Printa o texto na cor vermelha """
    return f"{Color.BOLD}{Color.RED}{text}{Color.END}"


def gen_password(password_lenght):
    """Gera o Password baseado na tabela ASCII.  A função retorna uma string com
    caracteres randomizados da lista ASCII-char_list

    Args:
        password_lenght (str): Tamanho desejado da senha

    Returns:
        str: generated password

    """

    # A função 'map' mapeia todos os item em (chr, range())
    # chr retorna o caractere correspondente da tabela ASCII dado seu código em decimal
    # range (33,126) é o intervalo em decimal da tabela ASCUU para caractereses UTF-8
    # Isso inclui Letras maiúsculas e minúsculas, números e caracteres especiais
    # https://www.ascii-code.com

    # criamos uma lista com elementos UTF-8
    ASCII_char_list = list(map(chr, range(33, 126)))

    # string vazia que será preenchida com a senha
    generated_password = ""

    for _ in range(password_lenght):
        # Aqui estamos pegando itens randomizados da lista e acrescentando na string
        # generated_password
        rand_char = random.choice(ASCII_char_list)
        generated_password += rand_char

    return generated_password  # Finalmente retornando a string


def loop_handle():
    """Essa função simplesmente controla o loop do menu, perguntando ao usuário
       se quer continuar a usar o programa, dependendo da resposta ele reinicia o programa
       ou fecha o mesmo
    """

    # Pergunta ao usuário se quer continuar a usar o programa
    loop_control = input("\n\nDeseja gerar outra senha? [y/n]: ")

    if loop_control == "n" or loop_control == "N":
        # Mensagem de despedida
        os.system(f"cowsay -f default Tchauzinho !!! | lolcat")
        exit()  # Fecha o programa
    elif loop_control == "y" or loop_control == "Y":
        cls()  # Limpa o terminal
        print(ASCII_ART)
        Execute()  # Reinicia o programa
    else:  # Caso input inválido
        print(boldRedText(
            "Entrada inválida, favor digite apenas [y] ou [n]\n"))
        loop_handle()  # Rechama a funçção


def Execute():
    """ Função principal que executa o programa
    """
    while True:

        password_lenght_input = input(
            "Insira a quantidade de caracteres desejados para a senha: ")

        if password_lenght_input.isdigit():  # Verificamos se o input é do tipo inteiro (int)
            # Executa a fiunção gen_password e formata com a função boldGreenText
            generated_password = boldGreenText(
                gen_password(int(password_lenght_input)))

            print(f"\nA senha gerada é {generated_password}\n")
            # Mensagem com dragão fofo
            os.system(f"cowsay -f dragon-and-cow Usar senhas fortes, com letras, números e símbolos, aumenta a segurança digital e protege seus dados pessoais contra ataques cibernéticos. Be safe !! | lolcat")

        else:  # Caso o input seja inválido, exibe mensagem de erro
            print(
                boldRedText(
                    "\n\nInput inválido, por favor, insira apenas números inteiros positivos.\n")
            )
            continue

        loop_handle()  # Chama o controle de loop


""" ################################################################################# """

print(ASCII_ART)

Execute()
