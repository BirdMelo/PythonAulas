# Refaça o Desafio 035 dos triângulos, acrecentando o recurso de mostrar
# que tipo de triângulo será formado:
# -EQUILÁTERO: Todos os lados iguais;
# -ISÓSCELES: Dois lados iguais;
# -ESCALENO: Todos os lados diferentes.

a = int(input('Determine o primeiro lado de um triângulo: '))
b = int(input('Determine o segundo lado ded um triângulo: '))
c = int(input('Determine o terceiro lado de um triângulo: '))

if abs(b-c) < a < b+c and abs(a-c) < b < a+c and abs(a-b) < c < a+b:
    if a == b == c:
        triangulo = 'EQUILÁTERO'
    elif a == b != c or a == c != b or c == b != a:
        triangulo = 'ISÓSCELES'
    elif a != b != c != a:
        triangulo = 'ESCALENO'
    print('É um triangulo {}{}{}'.format('\033[1;34m', triangulo, '\033[m'))
else:
    print('\033[1;31m'+'Não é um triangulo.'+'\033[m')
