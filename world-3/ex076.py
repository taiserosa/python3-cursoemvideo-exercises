#criar uma tupla única com nomes de produtos e seus preços
#no final, mostrar a listagem dos preços e produtos em forma de tabela

lista = ('abacaxi', 2, 'banana', 4, 'abacate', 3, 'maçã', 2, 'caqui', 5)
print('-' * 40)
print(f"{"LISTAGEM DE PREÇOS":^40}")
print('-' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f"{lista[pos]:.<30}", end='')
    else:
        print(f"R${lista[pos]:>6.2f}")
print('-' * 40)
