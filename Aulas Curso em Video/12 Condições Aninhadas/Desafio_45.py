# Crie um programa que jogue Jokenpô com você.
import random
from time import sleep

pc = random.choice(['papel', 'pedra', 'tesoura'])

eu = str(input('escolha: pedra, papel ou tesoura: '))

if pc == 'papel' and eu == 'pedra' or pc == 'pedra' and eu == 'tesoura' or pc == 'tesoura' and eu == 'papel':
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ!!!')
    print('')
    print('{}! {}EU VENCI{}!'.format(pc.upper(), '\033[1;31m', '\033[m'))

elif eu == 'papel' and pc == 'pedra' or eu == 'pedra' and pc == 'tesoura' or eu == 'tesoura' and pc == 'papel':
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ!!!')
    print('')
    print('{}! {}VOCÊ VENCEU{}!'.format(pc.upper(), '\033[1;32m', '\033[m'))

elif eu == pc:
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ!!!')
    print('')
    print('EMPATE!')

else:
    print('\033[1;31m'+'Digitação Incorreta'+'\033[m')
