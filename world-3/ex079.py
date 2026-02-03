#criar um programa onde o usuário digita vários valores
#adicionar esses valores na lista somente se não se repetirem
#no final mostrar a lista com os valores em ordem crescente
numeros = []
while True:
    num = int(input("Informe um valor inteiro: "))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado a lista com sucesso! ')
    else:
        print('Valor duplicado! Esse valor não será adcionado a lista!')
    r = str(input("Deseja continuar? [S/N]: ")).strip().upper()
    while r not in 'SN':
        r = str(input("Deseja continuar? [S/N]: ")).strip().upper()
    if r in 'Nn':
        break
numeros.sort()
print(f"Os valores digitados foram: {numeros}")