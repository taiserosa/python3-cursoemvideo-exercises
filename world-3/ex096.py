# fazer um programa que tenha uma função que receba as dimensões de um terreno (largura e compreimento)
# no final mostre a área do terreno
def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é {a}m²')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
