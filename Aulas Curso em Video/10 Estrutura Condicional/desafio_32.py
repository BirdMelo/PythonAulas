# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
ano = int(input('Escolha um ano: '))


if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano bissexto')
else:
    print('Ano não bissexto')
