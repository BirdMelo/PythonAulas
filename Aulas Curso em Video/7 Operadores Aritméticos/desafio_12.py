# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

P = float(input('qual o preço do produto? '))
print('Seu produto de R${:.2f} na liguidação fica R${:.2f}'.format(
    P, (P-(P*0.05))))
