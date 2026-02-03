#Faça um programa que leia nome e peso de várias pessoas, e guarde tudo em uma lista
#No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
dados = []
pessoas = []
maior = menor = 0
while True:
    dados.append(str(input('Informe seu nome: ')))
    dados.append(int(input('Informe seu peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('=-=' * 20)
print(f'No total foram registradas {len(pessoas)} pessoas!')
print(f'O maior peso registrado foi {maior}kg, de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'<{p[0]}>', end=' ')
print()
print(f'O menor peso registrado foi {menor}kg, de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'<{p[0]}>', end=' ')
