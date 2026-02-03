#ler 4 valores pelo teclado e adicioná-los a uma tupla
#mostrar quantas vezes aparece o valor 9
#em que posição foi digitado o primeiro valor 3
#quais foram os números pares digitados
valores = (int(input('Informe um número: ')),
           int(input('Informe mais um número: ')),
           int(input('Informe outro número: ')),
           int(input('Informe o último número: ')))
if 9 in valores:
    print(f'O valor 9 aparece {valores.count(9)} vezes')
else:
    print('O valor 9 não apareceu nenhuma vez!')
if 3 in valores:
    print(f'O primeiro valor três foi digitado na posição {valores.index(3) + 1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição!')
print(f'Os números pares digitados foram: ', end='')
for v in valores:
    if v % 2 == 0:
        print(v, end='')
