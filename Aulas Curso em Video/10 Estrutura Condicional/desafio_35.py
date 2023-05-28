# Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.
a = int(input('Digite um número inteiro para o lado A de um triangulo: '))
b = int(input('Digite um número inteiro para o lado B de um triangulo: '))
c = int(input('Digite um número inteiro para o lado C de um triangulo: '))

if abs(b-c) < a < b+c and abs(a-c) < b < a+c and abs(a-b) < c < a+b:
    print('É UM TRIANGULO!!!')
else:
    print('Não é um triangulo')
