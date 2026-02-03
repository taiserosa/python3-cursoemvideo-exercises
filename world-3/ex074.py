#gere 5 números aleatórios e adcione-os a uma tupla
# imprima a lista dos números
# o maior, e o menor
from random import randint
#for i in range(1, 6):
#    num = (randint(0, 10))
num = (randint(1, 10), randint(1, 10), randint(1, 10),
       randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in num:
    print(f'{n}', end=' ')
print(f'\nO maior número foi: {max(num)}\nO menor número foi: {min(num)}')