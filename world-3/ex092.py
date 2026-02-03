#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
dados = {}
dados['Nome'] = str(input("Informe seu nome: "))
nasc = int(input("Informe o ano de nascimento: "))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input("Informe a carteira de trabalho: (Digite 0 caso não tenha) "))
if dados['CTPS'] != 0:
    dados['Ano de contratação'] = int(input("Informe o ano de contratação: "))
    dados['Salário'] = float(input("Informe o salário: "))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Ano de contratação'] + 35) - datetime.now().year)
print('=-' * 15)
for v, k in dados.items():
    print(f"{v}: {k}")

