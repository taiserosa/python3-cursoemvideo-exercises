# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
aproveit = {}
partidas = []
aproveit['Nome'] = str(input("Qual o nome do jogador? "))
tot = int(input(f"Quantas partidas {aproveit["Nome"]} jogou? "))
for p in range(0, tot):
   partidas.append(int(input(f"Quantos gols fez na partida {p+1}? ")))
aproveit['Gols'] = partidas[:]
aproveit['Total'] = sum(partidas)
print('=-' * 20)
print(aproveit)
print('=-' * 20)
for k, v in aproveit.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 20)
print(f'O jogador {aproveit["Nome"]} jogou {len(aproveit["Gols"])} partidas!')
for i, v in enumerate(aproveit["Gols"]):
    print(f'=> Na partida {i+1} fez {v} gols')
print(f'Total de gols: {aproveit["Total"]}')

