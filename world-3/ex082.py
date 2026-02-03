#criar uma lista inicial e adicionar vários valores a ela
#depois criar outra lista só para os números pares
#e outra lista só para os números ímpares
#no final, mostrar as três listas
lista = []
listaP = []
listaI = []
while True:
    num = int(input("Informe um valor: "))
    lista.append(num)
    if num % 2 == 0:
        listaP.append(num)
    elif num % 2 != 0:
        listaI.append(num)
    r = str(input("Deseja continuar? [S/N] ")).strip().upper()
    while r not in 'SN':
        r = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if r in 'N':
        break
print(f"A lista inicial é: {lista}")
print(f"A lista de números pares é: {listaP}")
print(f"A lista de números ímpares é: {listaI}")