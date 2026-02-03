# fazer um programa que tenha uma função que receba como parâmetro uma mensagem de texto
# e que mostre uma linha acima e abaixo da mensagem com tamanho adaptável (que acompanhe o tamanho da mensagem)
def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)
escreva(str(input('Escreva uma mensagem de texto: ')))