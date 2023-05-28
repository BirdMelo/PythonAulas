# Crie um programa que leia um número inteiro e
# mostre na tela se ele é par ou impar

numero = int(input('número inteiro: '))
verificar = numero % 2

if verificar == 0:
    print('número par')
else:
    print('número impar')
