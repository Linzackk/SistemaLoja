from time import sleep

from lib.arquivo import *
tipos = [
    'Pães',
    'Salgados',
    'Doces',
    'Bebidas',
    'Roupas',
    'Sapatos',

]
def leiaFloat(msg):
    """
    Possibilita a leitura do código para valores monetários utilizando "," ao invés de "."
    :param msg: Valor com casa decimal (175,85)
    :return: Valor convertido para float.
    """
    while True:
        num = str(input(msg))
        if ',' in num:
            num = num.replace(',','.')
        if num.replace('.','').isnumeric():
            break
        else:
            print(f'\033[1;31mPREÇO INVÁLIDO!\033[m')
    return float(num)

def arqexist(nome):
    """
    Verifica caso um arquivo de texto existe.
    :param nome: Nome do Arquivo
    :return: False para caso não Exista, True para caso Exista.
    """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def arqCriar(nome):
    """
    Cria um arquivo de texto
    :param nome: Nome do Arquivo a ser criado
    :return: None
    """
    a = open(nome, 'a')
    a.close()

def lerArq(nome):
    """
    Lê um arquivo e apresenta formatado em tabela no terminal
    :param nome: Nome do Arquivo
    :return: Conteúdos do Arquivo formatados
    """
    a = open(nome, 'rt', newline='\n')
    titulo(nome)
    for linha in a:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        print(f'{dado[0]:<25}{dado[1]:>25}')
    print(a.read())

def senha():
    """
    Faz uma validação da senha
    :return: True caso a senha seja aceita
    """
    titulo('LOGIN')
    while True:
        senha = input('\033[1;33m[ 0 ] \033[m- \033[1;34mSAIR\n\033[mSenha: ').strip()
        if senha == '0':
            break
        elif senha != '123':
            print('\033[1;31SENHA INVÁLIDA!\033[m')
        else:
            return True

def escArq(arq, item, preco):
    """
    Escreve no Arquivo: Nome do Produto e Preço do Produto.
    :param arq: Nome do Arquivo
    :param item: Produto
    :param preco: Preço do Produto
    :return: None
    """
    a = open(arq, 'at+')
    a.write(f'{str(item)};{str(preco)}\n')

def addItem(lista):
    """
    Adiciona um item a um arquivo caso exista a categoria indicada
    :param lista: lista com categorias da loja
    :return: None
    """
    titulo('ADICIONANDO ITEM')

    while True:
        titulo('CATEGORIAS')
        for c in tipos:
            print(f'\033[1;36m > {c}\033[m')
        cat = input('\033[1;33m[ 0 ] \033[m- \033[1;34mSAIR\n\033[mCategoria: ').strip()
        if cat == '0':
            break
        elif cat not in lista:
            print('\033[1;31mCATEGORIA NÃO ENCONTRADA.\033[m')
        else:
            linha()
            print('\033[1;33m[ 0 ] \033[m- \033[1;34mVOLTAR\033[m')
            item = str(input('Nome do Produto: ')).strip()
            if item != '0':
                p = leiaFloat('Preço: R$')
                preco = f'R${p:.2f}'
                escArq(cat, item, preco)
            else:
                sleep(0.3)
    print(f'\033[1;31mSaindo...\033[m')
    sleep(0.3)


