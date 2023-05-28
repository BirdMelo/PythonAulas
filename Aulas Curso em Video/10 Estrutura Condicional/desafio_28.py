import random

# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir o número.

# O programa deverá escrever na tela se o usuário acertou ou errou o número.

pc = random.randint(0, 5)
eu = int(input('Qual número vc acha que é? '))
if eu == pc:
    print('ACERTOU!!!')
else:
    print('ERRROOOU!!!')
print('O número era {}'.format(pc))
