import json
import calendar
from datetime import date
import os

arq = 'alunos-Luana.json'

def carregaralunos():
    """
    Carrega os dados dos alunos de um arquivo JSON.
    
    Args:
        arq (str): Caminho do arquivo JSON.
        
    Returns:
        dict: Dicionário com os alunos carregados ou {} se o arquivo não existir ou for inválido.
    """
    try:
        if os.path.exists(arq):
            with open(arq, 'r', encoding='utf-8') as file:
                return json.load(file)
        return {} # Retorna dict vazio se o arquivo não existir
    except json.JSONDecodeError:
        print(f'\033[0;31mERRO: O arquivo "{arq}" está corrompido ou mal formatado.\033[m')
        return {}
    except PermissionError:
        print(f'\033[0;31mERRO: Sem permissão para ler o arquivo "{arq}".\033[m')
        return {}
    except Exception as e:
        print(f'\033[0;31mERRO inesperado ao carregar "{arq}": {str(e)}\033[m')
        return {}


def linha():
    print('-' * 50)


def titulo(msg):
    linha()
    print(f'{msg:^50}')
    linha()


def salvaralunos(alunos):
    """
    Salva os dados dos alunos em um arquivo JSON sem retornar valores.
    Exibe mensagens de erro apenas se a operação falhar.
    """
    try:
        with open(arq, 'w', encoding='utf-8') as file:
            json.dump(alunos, file, indent=4, ensure_ascii=False)
    except PermissionError:
        print(f'\033[0;31mERRO: Sem permissão para escrever no arquivo "{arq}".\033[m')
    except IsADirectoryError:
        print(f'\033[0;31mERRO: O caminho "{arq}" é um diretório, não um arquivo.\033[m')
    except Exception as e:
        print(f'\033[0;31mERRO inesperado ao salvar em "{arq}": {str(e)}\033[m')


def cadastraraluno(alunos):
    """
    Cadastra um novo aluno no sistema, com dias de treino e valor por aula.
    - Valida se o aluno já existe.
    - Permite cadastrar múltiplos dias de treino.
    - Garante que os inputs são válidos.
    """
    titulo('NOVO CADASTRO')
    while True:
        nome = str(input(f'Nome do(a) aluno(a): ')).strip().title()
        if not nome:
            print(f'\033[0;31mERRO: Nome não pode estar vazio!\033[m')
            continue
        if nome in alunos:
            print(f'O aluno {nome} já tem cadastro!')
            return
        break
    linha()
    print(f'\033[32mCadastrando os dados do(a) aluno(a) {nome}\033[m')
    linha()
    diassemana = ['seg', 'ter', 'qua', 'qui', 'sex']
    treino = []
    for dia in diassemana:
        while True:
            res = input(f'{nome} treina {dia}? [S/N]: ').strip().upper()
            if res == 'S':
                treino.append(dia)
                break
            elif res == 'N':
                break
            else:
                print(f'\033[0;31mERRO: Digite apenas [S/N]\033[m')
    while True:
        try:
            valorhora = float(input(f'\nValor da hora/aula para {nome}: R$ '))
            if valorhora <= 0:
                print(f'\033[0;31mERRO: O valor deve ser positivo!\033[m')
                continue
            break
        except ValueError:
            print(f'\033[0;31mERRO: Digite um valor numérico válido!\033[m')
    alunos[nome] = {'dias': treino, 
                    'hora/aula': valorhora,
                    'historico': {} # guarda o historico do mês/ano
                          }
    salvaralunos(alunos)
    linha()
    print(f'\033[32mAluno {nome} cadastrado com sucesso!\033[m')


def contdiasmes(mes, ano):
    """
    Conta quantas vezes cada dia útil (segunda a sexta) aparece em um mês/ano específico.

    Args:
        mes (int): Número do mês (1 a 12)
        ano (int): Ano (ex: 2024)

    Returns:
        dict: Dicionário com a contagem de dias por dia da semana
        Exemplo: {'seg': 4, 'ter': 4, 'qua': 5, 'qui': 4, 'sex': 4}"""
    cont = {'seg': 0, 'ter': 0, 'qua': 0, 'qui': 0, 'sex': 0}
    for dia in range(1, calendar.monthrange(ano, mes)[1] + 1):
        diasem = calendar.weekday(ano, mes, dia)
        if diasem == 0: cont['seg'] += 1
        elif diasem == 1: cont['ter'] += 1
        elif diasem == 2: cont['qua'] += 1
        elif diasem == 3: cont['qui'] += 1
        elif diasem == 4: cont['sex'] += 1
    return cont


def atualizarhistorico(aluno, mes_ano, contador):
    """
    Atualiza o histórico de aulas do aluno para o mês/ano especificado.
    Apenas atualiza os dias que o aluno normalmente treina.

    Args:
        aluno (dict): Dicionário do aluno a ser atualizado
        mes_ano (str): String no formato 'MM/AAAA' (ex: '05/2024')
        contador (dict): Dicionário com contagem de aulas por dia (ex: {'seg': 4, 'ter': 3})
        """
    if 'historico' not in aluno:
        aluno['historico'] = {}
    if mes_ano not in aluno:
        aluno['historico'][mes_ano] = {}
    for dia in aluno['dias']:
        aluno['historico'][mes_ano][dia] = contador.get(dia, 0)


def recibo(nome, mes_ano, aulas, valorhora):
    totaulas = sum(aulas.values())
    total = totaulas * valorhora
    emissao = date.today().strftime('%d/%m/%Y')
    arquivo = f'recibo-{nome}-{mes_ano}.txt'
    with open(arquivo, 'w', encoding='utf-8') as file:
        file.write(f'Recibo Personal Trainer Luana Kovalski\n')
        file.write(f'Aluno {nome}\n')
        file.write(f'Mês/Ano: {mes_ano[:4]}/{mes_ano[5:]}\n')
        file.write(f'Aulas por dia da semana:\n')
        for dia, qnt in aulas.items():
            file.write(f'  {dia}: {qnt}\n')
        file.write(f'Total de aulas: {totaulas}\n')
        file.write(f'Valor da hora/aula: R${valorhora:.2f}\n')
        file.write(f'Valor total: R${total:.2f}\n')
        file.write(f'Data da emissão: {emissao}\n')
    print(f'\033[32mRecibo gerado com sucesso!\033[m {arquivo}')
    linha()


def todosrecibos(alunos, mes, ano):
    mes_ano = f'{ano}-{mes:02d}'
    contmes = contdiasmes(mes, ano)
    for nome, dados in alunos.items():
        atualizarhistorico(dados, mes_ano, contmes)
        aulas = dados['historico'][mes_ano]
        recibo(nome, mes_ano, aulas, dados['hora/aula'])
    salvaralunos(alunos)
    print(f'\033[32mTodos os recibos gerados com sucesso!\033[m')


def menu(lista):
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m[{c}]\033[m - \033[34m{item}\033[m')
        c += 1
    linha()
    opc = leiaInt('\033[35mOpção selecionada => \033[m')
    return opc


def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
                print(f'\033[0;31mERRO! Digite um número inteiro válido.\033[m')
                continue
        except KeyboardInterrupt:
            print(f'\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n