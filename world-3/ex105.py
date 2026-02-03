# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(*notas, sit=True):
    """
    -> função para analisar notas e situações de vários alunos
    :param notas: uma ou mais notas dos alunos
    :param sit: indica se deve ou não mostrar a situação
    :return: dicionário com algumas informações sobre as notas e situação da turma
    """
    dados = {}
    dados['Total'] = len(notas)
    dados['Maior nota'] = max(notas)
    dados['Menor nota'] = min(notas)
    dados['Média'] = sum(notas)/len(notas)
    if sit:
        if dados['Média'] == 10:
            dados['Situação'] = 'ÓTIMA'
        elif 10 > dados['Média'] >= 7:
            dados['Situação'] = 'BOA'
        elif 7 > dados['Média'] >= 5:
            dados['Situação'] = 'RUIM'
        else:
            dados['Situação'] = 'PÉSSIMA'
    return dados

todasNotas = []
while True:
    n = (float(input('Informe uma nota: ')))
    todasNotas.append(n)
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if r == 'N':
        break

s = str(input('Deseja ver a situação? [S/N] ')).strip().upper()
mostrar = True if s == 'S' else False

result = notas(*todasNotas, sit=mostrar)
print(result)
#help(notas)
