# Crie um programa que simule o funcionomento de um caixa eletrônico.
# No inicio, pergunte ao usuário qual será o valor a ser sacado
#   (número inteiro) e o programa vai informar quantas cédulas de cada valor
#   serão entregues.

# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('----Caixa Eletronico----')
allced = 0
ced = 50
withdraw = int(input('Quanto deseja retirar do caixa?\n'))
print(50*'-')
print(f'Foi requerido R${withdraw:.2f}. Será entregue em:')

# Divisão de cedúlas:
while True:
    if withdraw >= ced:
        withdraw -= ced
        allced += 1
    else:
        if allced > 0:
            if allced == 1:
                print(f'1 cédula de R${ced:.2f}.')
            else:
                print(f'{allced} cédulas de R${ced:.2f}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        allced = 0
        if withdraw == 0:
            break
print('Faça bom profeito.')
print(50*'-')
