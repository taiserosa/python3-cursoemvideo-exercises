#pedir para informar 5 números e adicioná-los a uma lista
#no final, mostrar a lista, qual o maior, qual o menor e suas posições
lista = []
menor = maior = 0
for i in range(0, 5):
    lista.append(int(input(f"Informe o {i}º valor: ")))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
print('=-=' * 30)
print(f'Você digitou os valores {lista}')
print(f"O maior valor digitado foi: {maior} e está nas posições ", end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f"O menor valor digitado foi {menor} e está nas posições ", end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}... ", end='')
print()
