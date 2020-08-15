from interface import *
from time import sleep
from arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção cadastrar nova pessoa!
        cabeçalho('NOVO CADASTRO')
        nome = str(input('nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema.
        cabeçalho('Saindodo sistema... Até logo!')
        break
    else:
        # Digitou opção errada no menu.
        print('\033[31mERRO! Digite uma opção válida!\033[m')
sleep(2)
