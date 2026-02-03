#criar um programa onde o usuário digite uma expressão que use parênteses
#o programa deverá analisar a expressão e verificar se todos os parênteses abertos foram fechados
exp = str(input("Digite uma expressão: "))
lista = []
for simbolo in exp:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está inválida!")