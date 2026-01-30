from lib.verificacao import criarArquivo, leituraLinha, atualizaArquivo, escreveArquivo
from lib.interface import cabecalho, menu
from time import sleep

caminho = "desafios/desafio115/lib/verificacao/lista.txt"
while True:    
    lista = ["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do Sistema"]           
    m = menu(lista)
    if m == 0:
        cabecalho('PESSOAS CADASTRADAS')
        pessoas = leituraLinha(caminho)
        c = 0
        for p in pessoas:
            print(p, end="")
            c += 1
            if c == len(pessoas):
                print()
    elif m == 1:
        cabecalho('CADASTRO DE PESSOAS')
        pessoas = atualizaArquivo(caminho, str(input("Quem você quer adicionar ao arquivo?\n")).strip())
    elif m == 2:
        cabecalho('Saindo do sistema... Até logo!')
        break
    sleep(2)