from lib.verificacao import encontreArquivo
from lib.interface import cabecalho, menu, submenu

while True:    
    lista = ["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do Sistema"]           
    m = menu(lista)
    if m == 0:
        cabecalho('Opção 1')
    elif m == 1:
        cabecalho('Opção 2')
    elif m == 2:
        cabecalho('Saindo do sistema... Até logo!')
        break
#encontreArquivo("desafios/desafio115/dist/verificacao/lista.txt")