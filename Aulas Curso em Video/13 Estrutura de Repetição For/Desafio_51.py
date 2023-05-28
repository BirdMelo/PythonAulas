# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
num = int(input('Primeiro termo: '))
r = int(input('Razão: '))
dec = num+(10-1)*r

for n in range(num, dec+num, r):
    print('{}'.format(n), end=', ')
