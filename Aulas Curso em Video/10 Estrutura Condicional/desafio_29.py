# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por Hm acima da velocidade
velocidade = int(input('velocidade do carro: '))
if velocidade > 80:
    diferença = velocidade - 80
    multa = diferença*7
    print('Velocidade {}Km acima do permitido, multa prevista de R${:.2f} .'
          .format(diferença, multa))
