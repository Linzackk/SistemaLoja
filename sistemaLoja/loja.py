from sistemaLoja.lib.interface import *
from sistemaLoja.lib.arquivo import *

# Interface da Loja


# Tipos está sendo importado de interface\__init__.py
for items in tipos:
    # Verificando caso os arquivos das categorias não existam.
    if not arqexist(items):
        # Cria os Arquivos caso eles não existam.
        arqCriar(items)

while True:
    # Cria o Título Formatado
    titulo('Padaria do seu Zé')

    # Formata o Menu com os Tipos
    menu(tipos)

    # Cria uma Linha de separação
    linha()

    # Recebe a interação do Usuário apenas aceitando os valores possíveis.
    e = (escolha(len(tipos ) - 1))

    # Mostra na Tela o Conteúdo dependendo da interação do Usuário.
    if e == 4:
        break
    if e == 0:
        lerArq(tipos[0])
    if e == 1:
        lerArq(tipos[1])
    if e == 2:
        lerArq(tipos[2])
    if e == 3:
        lerArq(tipos[3])

print('\033[1;31mFIM\033[m')