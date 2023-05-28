# Crie um programa que leia quanto tinheiro uma pessoa tem na sua carteira e
# mostre quantos dolares ela pode comprar.
# Considere US$1.00=R$3.27

C = float(input('quanto vc tem na carteira: '))
print('com {}R$ vc pode comprar {:.2f}US$.'.format(C, (C/3.27)))
