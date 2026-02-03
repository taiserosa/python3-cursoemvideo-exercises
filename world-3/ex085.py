# cadastre sete valores numéricos informados pelo usuário em uma lista única,
# mas que mantenha separado os valores pares dos ímpares
# no final, mostre a lista de números pares e ímpares em ordem crescente
numeros = [[], []]
num = 0
for n in range(1, 8):
    num = int(input(f'Informe o {n}º valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    elif num % 2 == 1:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(f'A lista de números pares é {numeros[0]}')
print(f'A lista de números ímpares é {numeros[1]}')
