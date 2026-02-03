#Criar uma tupla com números (de 0 até 20) escritos por extenso
#ler um número digitado pelo usuário
#mostrar o número digitado escrito por extenso
#perguntar se o usuário deseja informar outro número

numbers = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input("Informe um número inteiro entre 0 e 20: "))
    if 0 <= n <= 20:
        print(f"Você digitou o número {numbers[n]}!")
    else:
        print('Número digitado inválido! Tente novamente!')
        continue
    r = ' '
    while r not in "SN":
        r = str(input("Deseja informar outro número? ")).strip().upper()
    if r == 'N':
        print('Programa encerrado!')
        break
