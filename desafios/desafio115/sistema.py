from lib.verificacao import criarArquivo
from lib.interface import cabecalho, menu
from time import sleep

"""while True:    
    lista = ["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do Sistema"]           
    m = menu(lista)
    if m == 0:
        cabecalho('Opção 1')
    elif m == 1:
        cabecalho('Opção 2')
    elif m == 2:
        cabecalho('Saindo do sistema... Até logo!')
        break
    sleep(2)
"""

file = criarArquivo("desafios/desafio115/lib/verificacao/lista.txt")
print(file)