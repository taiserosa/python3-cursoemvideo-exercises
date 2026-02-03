# pedir para o usuário preencher uma matriz 3x3
# no final, mostrar a matriz formatada,
# a soma dos números pares digitados,
# a soma dos valores da terceira coluna,
# e qual o maior valor da segunda linha
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaTerceira = cont = soma = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f"Informe um número para a posição {i, j} da matriz: "))
        cont += 0
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]
    print()
for i in range(0, 3):
    somaTerceira += matriz[i][2]
for j in range(0, 3):
    if j == 0:
        maior = matriz[1][j]
    elif matriz[1][j] > maior:
            maior = matriz[1][j]
print(f'A soma dos números pares digitados foi: {soma}')
print(f'A soma dos números da terceira coluna foi: {somaTerceira}')
print(f'O maior valor digitado na segunda linha foi: {maior}')
