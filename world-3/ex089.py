# ler o nome e duas notas de vários alunos e guardar tudo em uma lista composta
# no final mostre um boletim fomatado contendo o nome e a média de cada aluno
# depois perguntar ao usuário se deseja ver as notas isoladas de um determinado aluno
lista = []
while True:
    nome = str(input('Informe seu nome: '))
    nota1 = float(input('Informe a primeira nota: '))
    nota2 = float(input('Informe a segunda nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    r = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    while r not in 'SN':
        r = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    if r == 'N':
        break
print('=-' * 20)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 24)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 24)
    opc = int(input('Deseja ver as notas de qual aluno? (Digite 999 para parar): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    elif opc <= len(lista) - 1:
        print(f'As notas de {lista[opc][0]} são {lista[opc][1]}')
print('<<< VOLTE SEMPRE! >>>')