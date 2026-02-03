# pedir para o usuário informar o nome e a média de um aluno,
# calcular a situação baseada na média e guardar tudo em um dicionário
# no final, mostrar o nome, a média e a situação (aprovado, em recuperação ou reprovado)
alunos = {}
while True:
    alunos['Nome'] = str(input('Informe o nome: '))
    alunos['Média'] = float(input(f'Informe a média de {alunos["Nome"]}: '))
    if alunos['Média'] >= 7:
        alunos['Situação'] = 'Aprovado'
    elif 5 <= alunos['Média'] < 7:
        alunos['situação'] = 'Em recuperação'
    elif alunos['Média'] < 5:
        alunos['Situação'] = 'Reprovado'
    print('=-' * 20)
    for v, k in alunos.items():
        print(f"{v} é igual a {k}")
    print('=-' * 20)
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] '))
    if r in 'N':
        break
