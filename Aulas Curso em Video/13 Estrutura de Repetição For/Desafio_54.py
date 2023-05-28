# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e
# quantas já são de maiores
from datetime import date

anoAtual = date.today().year
menor = []
maior = []

for i in range(0, 7):
    nome = str(input('Digite um nome: '))
    nas = int(input('Digite o ano de nascimento dessa pessoa: '))
    idade = anoAtual - nas
    print(idade)

    if idade < 18:
        menor.append(nome)
    else:
        maior.append(nome)
print(40*'-')
print('Lista das pessoas maiores de idade: {}'.format(maior))
print(40*'-')
print('Lista das pessoas menores de idade: {}'.format(menor))
print(40*'-')
