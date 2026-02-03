# Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt, EOFError):
            print('\033[0;31mEntrada interrompida pelo usuário!\033[m')
            return 0

def leiaFloat(msg):
    while True:
        try:
            v = input(msg).replace(',', '.')
            valor = float(v)
            return valor
        except ValueError:
            print('\033[0;31mERRO! Digite um número real válido!\033[m')
            continue
        except (KeyboardInterrupt, EOFError):
            print('\033[0;31mEntrada interrompida pelo usuário!\033[m')
            return 0


n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Informe um valor real: ')

print(f'Você digitou o número inteiro {n1}!')
print(f'Você digitou o número real {n2}!')
