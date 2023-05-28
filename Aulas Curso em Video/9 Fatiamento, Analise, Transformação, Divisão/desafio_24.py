
# Crie um programa que leia o nome de uma cidade e
# diga se ela começa ou não com o nome "Santo".

cidade = str(input("Digite o nome de uma cidade: "))
g = cidade.split()[0].find('Santo')
if g == 0:
    print('Nome começa com Santo')
else:
    print('Nome não começa com Santo')
