# Crie um programa que leia nome e preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final mostre:

# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.
buy = lowPrice = 0.0
product = thousand = 0
while True:
    product += 1
    print(50*'-')
    print(f'{product}° produto:')
    name = str(input('Qual o nome do produto: '))
    price = float(input('Preço do produto: R$'))
    if lowPrice == 0.0:
        cucaracha = name
        lowPrice = price
    elif lowPrice > price:
        cucaracha = name
        lowPrice = price
    if price > 1000:
        thousand += 1
    buy += price
    print(50*'-')
    more = str(input('Quer mais produtos?\n').strip().lower()[0])
    if more == 'n':
        break
print(50*'-')
print(f'O item mais barato é {cucaracha} por R${lowPrice:.2f}.')
if thousand == 1:
    print('Apenas um item custa mais de R$1000.00.')
else:
    print(f'{thousand} itens custam mais de R$1000.00.')
print(f'E o total da compra ficou R${buy:.2f}.')
