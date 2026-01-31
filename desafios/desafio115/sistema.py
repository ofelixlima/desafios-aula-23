from lib.verificacao import *
from lib.interface import *
from time import sleep
from lib.leitura import *

while True:    
    lista = ["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do Sistema"]           
    m = menu(lista)
    caminho = "desafios/desafio115/lib/verificacao/lista.txt"
    back = 'desafios/desafio115/lib/backup/backup.txt'
    if m == 0:
        doBackupParaArquivo(back, caminho)
        cabecalho('PESSOAS CADASTRADAS')
        pessoas = leituraLinha(caminho)
        organizarLista(pessoas)
    elif m == 1:
        doBackupParaArquivo(back, caminho)
        cabecalho('NOVO CADASTRO')
        pessoa = cadastroNome().strip()
        idade = leiaInt('Idade: ')
        todos = f'{pessoa};{idade}'
        atualizaArquivo(caminho, todos)
        atualizaArquivo(back, todos)
        print(f"{nomePessoa(pessoa)} com a idade {idade} foi adicionado com sucesso!")
    elif m == 2:
        cabecalho('Saindo do sistema... Até logo!')
        break
    sleep(2)