# rie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular
# e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=True):
    """
    -> calcula o fatorial de um número
    :param num: o número a ser calculado
    :param show: mostrar ou não a conta
    :return: o cálculo do fatorial de um número n
    """
    conta = 1
    print(f'O fatorial de {num} é: ', end='')
    for i in range(num, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        conta *= i
    return conta


n = int(input('Deseja ver o fatorial de qual número? '))
fat = str(input('Deseja ver a conta? [S/N] ')).strip().upper()
mostrar = True if fat == 'S' else False
print(fatorial(n, mostrar))
#help(fatorial)