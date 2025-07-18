#SISTEMA PRINCIPAL
from modulos import *
from time import sleep

alunos = carregaralunos()
if __name__ == '__main__':
    while True:
        resposta = menu(['CADASTRAR NOVO ALUNO', 'GERAR RECIBOS DO MÊS', 'SAIR DO SISTEMA'])
        if resposta == 1:
            cadastraraluno(alunos)
        elif resposta == 2:
            mes = int(input('Digite o mês [1-12]: '))
            ano = int(input('Digite o ano [ex: 2025]: '))
            linha()
            todosrecibos(alunos, mes, ano)
        elif resposta == 3:
            titulo('ENCERRANDO SISTEMA...Até logo!')
            sleep(1)
            break
        else:
            print(f'\033[0;31mERRO! Digite uma opção válida!\033[m')
        sleep(1.5)