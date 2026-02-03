# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador
aproveit = {}
partidas = []
time = []
while True:
    aproveit.clear()
    aproveit['Nome'] = str(input("Qual o nome do jogador? "))
    tot = int(input(f"Quantas partidas {aproveit["Nome"]} jogou? "))
    partidas.clear()
    for p in range(0, tot):
        partidas.append(int(input(f"Quantos gols fez na partida {p+1}? ")))
    aproveit['Gols'] = partidas[:]
    aproveit['Total'] = sum(partidas)
    time.append(aproveit.copy())
    while True:
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
        print('ERRO! Responda apenas S ou N!')
    if r in 'Nn':
        break
print('=-' * 20)
print('Cod', end=' ')
for i in aproveit.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input("Mostrar dados de qual jogador? (Digite 999 para parar) "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"ERRO! Não existe jogador com o código {busca}!")
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'   No jogo {i+1} ele fez {g} gols')
    print('-' * 40)
print('<< PROGRAMA ENCERRADO, VOLTE SEMPRE! >>')    