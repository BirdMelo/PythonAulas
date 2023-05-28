# Crie um programa que leia dois valores e mostre um menu na tela:

# [ 1 ] SOMAR
# [ 2 ] MULTIPLICAR
# [ 3 ] QUAL O MAIOR
# [ 4 ] SUBSTITUIR NÚMEROS
# [ 5 ] SAIR DO PROGRAMA

# Seu programa deverá realizar a operação solicitada em cada caso.
operador = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um segundo número: '))
while operador != 5:
    print(20*'-')
    print('Qual operação deseja fazer?')
    print('[ 1 ] SOMAR')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] QUAL O MAIOR')
    print('[ 4 ] SUBSTITUIR NÚMEROS')
    print('[ 5 ] SAIR DO PROGRAMA')
    print(20*'-')
    operador = int(input(': '))
    print(20*'-')
    if operador == 1:
        print('SOMAR: {} + {} = {}'.format(n1, n2, n1+n2))
        operador2 = str(input('Quer voltar ao menu [ S ] ou [ N ]: ')).upper()
        if operador2 == 'N':
            operador = 5
    elif operador == 2:
        print('MULTIPLICAR: {} * {} = {}'.format(n1, n2, n1*n2))
        operador2 = str(input('Quer voltar ao menu [ S ] ou [ N ]: ')).upper()
        if operador2 == 'N':
            operador = 5
    elif operador == 3:
        if n1 > n2:
            print('{} é maior que {}.'.format(n1, n2))
        elif n2 > n1:
            print('{} é maior que {}.'.format(n2, n1))
        else:
            print('São o mesmo número.')
        operador2 = str(input('Quer voltar ao menu [ S ] ou [ N ]: ')).upper()
        if operador2 == 'N':
            operador = 5
        if operador2 not in 'SN':
            print('Digitação incorreta, voltando ao menu.')
            operador2 = 'S'
    elif operador == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite um segundo número: '))
print('Fechando programa.')
