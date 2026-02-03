#Preencher uma tupla com os vinte primeiros times colocados no campeonato brasileiro de futebol
#mostrar quais são os primeiros 5 colocados
#mostrar quais são os 4 últimos colocados
#mostrar os times me ordem alfabética
#mostrar onde está o time corinthians
times = ('Flamengo', 'Cruzeiro', 'Bragantino', 'Palmeiras', 'Bahia', 'Fluminense', 'Atlético - MG', 'Botafogo', 'Mirassol', 'Corinthians', 'Grêmio', 'Ceará', 'Vasco', 'São Paulo', 'Santos', 'Vitória', 'Internacional', 'Fortaleza', 'Juventude', 'Sport')
print('=-=' * 30)
print(f"A lista de times do Brasileirão é:")
for t in times:
    print(t)
print('=-=' * 30)
print('Os cinco primeiros colocados são:')
for t in (times[0:5]):
    print(t)
print('=-=' * 30)
print("Os 4 últimos colocados são:")
for t in (times[-4:]):
    print(t)
print('=-=' * 30)
print("Os times em ordem alfabética são:")
for t in sorted(times):
    print(t)
print('=-=' * 30)
print(f"O time Corinthians está na {times.index('Corinthians') + 1}ª posição")
print('=-=' * 30)
'''
print('=-=' * 30)
print(f"A lista de times do Brasileirão é: {times}")
print('=-=' * 30)
print(f'Os cinco primeiros colocados são: {times[0:5]}')
print('=-=' * 30)
print(f"Os 4 últimos colocados são: {times[-4:]}")
print('=-=' * 30)
print(f"Os times em ordem alfabética são: {sorted(times)}")
print('=-=' * 30)
print(f"O time Corinthians está na {times.index('Corinthians') + 1}ª posição")
print('=-=' * 30)
'''