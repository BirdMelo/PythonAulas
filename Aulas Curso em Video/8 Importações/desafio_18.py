# faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

An = float(input('digite o valor do ângulo: '))

print('O ângulo {}° tem seu seno de valor {:.2f}, cosseno de valor {:.2f} e tangente de valor {:.2f}'.format(
    An, (math.sin(math.radians(An))), (math.cos(
        (math.radians(An)))), (math.tan((math.radians(An))))
))
