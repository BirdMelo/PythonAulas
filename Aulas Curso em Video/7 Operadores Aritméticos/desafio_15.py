#    Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#    Calcule o preço a pagar, sabendo que
# o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias de carro alugado? '))*60
Km = float(input('Quantos quilometros rodados? '))*0.15
preço = dias+Km
print('Então o preço do aluguel ficou R${:.2f}.'.format(preço))
