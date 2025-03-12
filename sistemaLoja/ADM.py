from sistemaLoja.lib.interface import *
from sistemaLoja.lib.arquivo import *

# Sistema Administrativo para Manutenção de Itens na Loja

adm = senha()
if adm:
    menus = [
        'Adicionar Item',
        'Remover Item',
    ]
    while True:
        titulo('ADMINISTRAÇÃO')
        menu(menus)
        e = escolha(len(menus) - 1)
        if e == 0:
            addItem(tipos)
        if e == 1:
            print('REMOVER ITEM')
        if e == (len(menus) - 1):
            break


