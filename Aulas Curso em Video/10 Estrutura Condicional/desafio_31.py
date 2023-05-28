# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km
# e R$0,45 para viagens de mais longas.

distancia = float(input('Quantos quilometros sua viagem? '))

if distancia <= 200:
    preço = distancia*0.5
else:
    preço = distancia*0.45

print('O preço da passagem é de R${:.2f} .'.format(preço))
