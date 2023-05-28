# Faça um programa que leia um número inteiro e diga
# se ele é ou não um número primo.

num = int(input('Digite um número: '))
lista = []
for i in range(1, num+1):
    if num % i == 0:
        lista.append(i)
if len(lista) == 2:
    print('O número {} é primo, por ser divisível'.format(num) +
          ' por apenas 1 e ele mesmo')
elif len(lista) == 1:
    print('O número 1 é divisivel penas por ele mesmo. números primos tem' +
          ' que ser excencialmente divisiveis por 2 números.')
else:
    print('O número {} não é primo, por ser divisivel por: {}.'.format(
        num, lista))
