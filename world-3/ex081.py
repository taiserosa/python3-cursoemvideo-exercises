#adicionar certos valores a uma lista
#no final, mostrar quantos valores foram digitados,
#qual a ordem descrescente da lista,
#e se o número 5 está na lista ou não
l = []
while True:
    l.append(int(input("Informe um número inteiro: ")))
    r = str(input("Deseja continuar? [S/N] ")).strip().upper()
    while r not in 'SN':
        r = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if r in 'N':
        break
print(f"Foram digitados {len(l)} números!")
l.sort(reverse = True)
print(f"A lista ordenada em ordem reversa é: {l}")
if 5 not in l:
    print("O valor 5 não está na lista!")
else:
    print(f"O valor 5 está na posição {l.index(5)+1} da lista!")
