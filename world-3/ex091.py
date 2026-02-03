# Criar um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, colocar esse dicionário em ordem decrescente, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
ranking = []
jogadores = {'1º jogador': randint(1, 6),
             '2º jogador': randint(1, 6),
             '3º jogador': randint(1, 6),
             '4º jogador': randint(1, 6)
             }
print('VALORES SORTEADOS NO DADO:')
for k, v in jogadores.items():
    print(f"O {k} tirou {v} no dado")
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('=-' * 15)
print('RANKING DOS JOGADORES:')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
