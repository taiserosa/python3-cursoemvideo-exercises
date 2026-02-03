# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
lista = []
lista2 = []
jogos = int(input("Quantos jogos serão sorteados? "))
tot = 1
while tot <= jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    lista2.append(lista[:])
    lista.clear()
    tot += 1
print('=-=' * 2, f' SORTEANDO {jogos} JOGOS! ', '=-=' * 2)
for i, l in enumerate(lista2):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('=-=-=' * 2, ' BOA SORTE! ', '=-=-=' * 2)
