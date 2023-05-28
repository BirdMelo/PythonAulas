#   Crieum programa que leia vários números inteiros pelo teclado.

#   No final da execução, mostre a média entre todos os valores e qual foi o
# maior e o menor valores lidos.

#   O programa deve perguntar ao usuário se ele quer ou não continuar a
# digitar valores.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = soma = menor = maior = 0
operador = 'S'
cont = 2

while operador != 'N':

    if cont == 2:
        if n1 > n2:
            maior = n1
            menor = n2
        elif n2 > n1:
            maior = n2
            menor = n1
        else:
            maior = menor = n1
        soma = n1+n2
    if cont > 2:
        if n3 > maior:
            maior = n3
        if n3 < menor:
            menor = n3
        soma += n3

    operador = str(input('Quer mais números? [ S ] [ N ]: ')).upper()
    if operador == 'S':
        n3 = int(input('Digite mais um número:'))
        cont += 1
    elif operador != 'N' and operador != 'S':
        print('Digitação incorreta.')
        operador = 'N'
print('Media: {}\nMaior: {}\nMenor: {}'.format(soma/cont, maior, menor))
