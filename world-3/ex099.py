#  Faça um programa que tenha uma função chamada maior(),
#  que receba vários parâmetros com valores inteiros.
#  Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
from random import randint
def maior(*num):
    maior = 0
    cont = 0
    print('=-' * 20)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(1)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo!')
    print(f'O maior valor informado foi {maior}!')

maior(randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior(randint(0, 10), randint(0, 10), randint(0, 10))
maior(randint(0, 10), randint(0, 10))
maior(randint(0, 10))
maior()
