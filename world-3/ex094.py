# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
pessoa = {}
lista = []
soma = cont = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input("Informe seu nome: "))
    while True:
        pessoa['Sexo'] = str(input("Informe seu sexo [F/M]: ")).strip().upper()[0]
        if pessoa['Sexo'] in 'FM':
            break
        print('ERRO! Por favor, digite apenas M ou F!')
    pessoa['Idade'] = int(input("Informe sua idade: "))
    soma += pessoa['Idade']
    lista.append(pessoa.copy())
    while True:
        r = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
        if r in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou F!')
    if r == 'N':
        break
print('=-' * 26)
print(f'A) No total foram cadastradas {len(lista)} pessoas!')
media = soma / len(lista)
print(f'B) A média de idade das pessoas cadastradas é {media:5.2f}!')
print('C) A lista das mulheres cadastradas é: ', end=' ')
for p in lista:
    if p['Sexo'] in 'F':
        print(f'{p["Nome"]}', end='')
print()
print('D) Lista de pessoas que estão acima da média de idade: ')
for p in lista:
    if p['Idade'] > media:
        print('  ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print()
print('<< PROGRAMA ENCERRADO! >>')