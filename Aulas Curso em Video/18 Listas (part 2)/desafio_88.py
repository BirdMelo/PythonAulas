# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados
#    e vai sortear 6 números entre 1 e 60 para cada jogo,
#    cadastrando tudo em uma lista composta.
from random import randint
from time import sleep

palpites: list = []
palpite: list = []
games = int(input("Quantos jogos quer jogar?\n"))
for j in range(games):
    for i in range(6):
        while True:
            num = randint(0, 60)
            if num not in palpite:
                palpite.append(num)
                break
    palpites.append(palpite[:])
    palpite.clear()
print(f'{f" Sorteando {games} jogos ":=^40}')
for c in range(len(palpites)):
    print(f"{c+1:>5}° jogo: {palpites[c]}")
    sleep(0.6)
print(f'{" Boa Sorte ":=^40}')
