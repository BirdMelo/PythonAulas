#   Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais
# alguns termos.

#   O programa encerra quando ele disser que quer mostrar 0 termos.
num = int(input('Escolha um número: '))
r = int(input('Escolha a razão: '))

g = 9
while g != 0:
    i = 0
    while i < g:
        print('{}'.format(num), end=', ')
        num += r
        i += 1
    print('{}.'.format(num))
    condição = str(
        input('Quer mais termos? [ S ] ou [ N ]. ')).upper()
    if condição == 'S':
        g = int(input('Mais quantos termos? '))
    elif condição == 'N':
        g = 0
    else:
        print('Digitação incorreta.')
        g = 0
print('Fim do programa.')
