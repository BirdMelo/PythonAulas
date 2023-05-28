# Faça um programa que leia o peso de cinco pessoas. No final,
# mostre qual foi o maior e o menor peso lidos.
lpeso = []
for i in range(0, 5):
    peso = float(input('Digite o peso da {}° pessoa: '.format(i+1)))
    lpeso.append(peso)
lpeso.sort()
print(50*'-')
print('''Pessoa com menor peso tem: {}Kg.
Pessoa com maior peso tem: {}Kg.'''.format(lpeso[0], lpeso[4]))
print('')
