# crie um algoritmo que leia  um número e mostre o seu dobro, seu triplo e raiz quadrada.
F = int(input('Digite qualquer número: '))
print('O dobro de {} é {}, o triplo é {} e sua raiz é {:.3f}'.format(
    F, (F*2), (F*3), (F**(1/2))))
