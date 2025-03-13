def linha():
    """
    Linha para separar e deixar o Terminal mais organizado e legivel
    :return: 50 caracteres de -
    """
    print('\033[1;35m-\033[m' * 50)

def titulo(msg):
    """
    Cria um Título organizado e formatado
    :param msg: Mensagem que Aparecerá no Título
    :return: Título inteiro formatado
    """
    linha()
    print(msg.center(50))
    linha()

def menu(lista=[]):
    """
    Cria um menu formatado com as informações contidas numa lista. Caso necessário ele cria uma opção "sair" em ultimo na lista
    :param lista: Lista com Elementos presentes no Menu
    :return: Menu formatado e parametro "sair"
    """
    try:
        lista.index('Sair')
    except ValueError:
        lista.append('Sair')

    for c in range(0, len(lista)):
        print(f'\033[1;33m[ {c} ]\033[m - \033[1;34m{lista[c]}\033[m')


def escolha(n=0):
    """
    Cria um Input de escolhas onde o valor mínimo é 0 e o máximo é N
    :param n: Valor Máximo da escolha
    :return: N caso atenda os parâmetros
    """
    while True:
        e = input()
        if e.isnumeric():
            if int(e) > n - 1 or int(e) < 0:
                print(f'\033[1;31m{e} NÃO É VÁLIDO!\033[m')
            else:
                break
        else:
            print(f'\033[1;31m{e} NÃO É VÁLIDO!\033[m')
    return int(e)


#def listagem(msg):
