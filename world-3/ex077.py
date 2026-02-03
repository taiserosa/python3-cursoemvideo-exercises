#criar uma tupla com várias palavras (sem acentos)
#depois mostrar quais são as vogais de cada palavra

t = ('cama', 'quadro', 'parede', 'ar', 'paz', 'guerra', 'sad')
for palavra in t:
    print(f'\nNa palavra {palavra.upper()} temos as vogais', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
