# Faça um programa que mostre a tabuada de vários números, um de cada vez,
#   para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

n = 0
print(20*'-')
while True:

    n = int(input('Quer a tabuada de qual número? '))
    print(20*'-')
    if n < 0:
        print('Essa atividade apenas atende números positivos.')
        print(20*'-')
        break

    for i in range(0, 11):
        mult = n*i
        print(f'{n} x {i} = {mult}')
    print(20*'-')
