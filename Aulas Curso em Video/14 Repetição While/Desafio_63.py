#   Escreva um programa que leia um número n inteiro qualquer e
# mostre na tela os n primeiros elementos de uma sequencia de Fibonacci
print(40*'-')
print('Sequencia de Fibonacci:')
num = int(input('Digite um número: '))
q = int(input('Quantos termos devo mostrar? '))
print(40*'-')
ant = 0
print('{}'.format(num), end=', ')
for i in range(0, q-2, 1):
    c = num+ant
    ant = num
    num = c
    print(num, end=', ')
print(num+ant)
print(40*'-')
