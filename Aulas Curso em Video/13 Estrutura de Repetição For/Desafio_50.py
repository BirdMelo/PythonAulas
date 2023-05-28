# Desenvolva um programa que leia 6 números inteiros e
# mostre a soma apenas daqueles que forem pares. Se for impar, desconsidere-o
for i in range(0, 6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        num += num
print(num)
