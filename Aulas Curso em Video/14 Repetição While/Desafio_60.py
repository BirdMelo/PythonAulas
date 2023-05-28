# Faça um programa que leia um número qualquer e mostre seu fatorial.

# Ex: 5! = 5*4*3*2*1=120

# Fazer com While e também o For

print(40*'-')
print('ESTRUTURA WHILE:')

num = int(input('Digite um número: '))
if num >= 1559:
    print('Esse número é muito grande para um Integer.')
else:
    f = 1
    print('{}! ='.format(num), end=' ')
    while num > 1:
        print('{}'.format(num), end=' * ')
        f *= num
        num -= 1
    print('1 = {}'.format(f))

print(40*'-')
print('ESTRUTURA FOR:')

num1 = int(input('Digite um número: '))
if num1 >= 1559:
    print('Esse número é muito grande para Integer.')
else:
    print('{}! ='.format(num1), end=' ')
    c = 1
    for i in range(num1, 1, -1):
        print('{}'.format(i), end=' * ')
        c *= i
    print('1 = {}'.format(c))
    print(40*'-')
if num >= 1559 and num1 >= 1559:
    print('Acho que vc é burro e não entendeu de primeira')
