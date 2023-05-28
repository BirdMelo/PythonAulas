# Faça um programa que leia três números e
# mostre qual é o maior e qual é o menor.

primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
terceiro = int(input('Digite o terceiro número: '))

if primeiro < segundo and primeiro < terceiro:
    menor = primeiro
if segundo < primeiro and segundo < terceiro:
    menor = segundo
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro

if terceiro > primeiro and terceiro > segundo:
    maior = terceiro
if segundo > primeiro and segundo > terceiro:
    maior = segundo
if primeiro > segundo and primeiro > terceiro:
    maior = primeiro

print('O maior número é {} e o menor número é {}.'.format(maior, menor))
