# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
import math

n1 = float(input('digite qualquer número do tipo float: '))
PI = math.trunc(n1)
print('a parte inteira de {} é {}'.format(n1, PI))
