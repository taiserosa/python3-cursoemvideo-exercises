#criar um programa onde são inseridos 5 números
#cada número já deve ser inserido em ordem crescente na lista sem usar o sort()
lista = []
for i in range(0, 5):
    valor = int(input("Informe um valor: "))
    if i == 0 or valor > lista[-1]:
        lista.append(valor)
        print("Valor adicionado ao final da lista!")
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f'Valor adicionado na posição {pos} da lista')
                break
            pos += 1
print(f"Os valores digitados em ordem foram: {lista} ")