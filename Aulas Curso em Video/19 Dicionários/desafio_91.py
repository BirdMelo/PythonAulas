# Crie um programa onde 4 jogadores joguem um dado e
#   tenham resultados aleatórios.
# Guarde-os um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que
#   o vencedor tirou o maior número no dado
from operator import itemgetter
from random import randint
from time import sleep

# Colocando em um dict:
jogos: dict = {}
for i in range(4):
    j = randint(0, 6)
    jogos[f"{i+1}° jogador"] = j
# Lendo dict:
for k, v in jogos.items():
    print(f"{k} acertou {v} no dado.")
    sleep(0.5)
print(f'{f" Raking ":=^30}')
# Organizando dict:
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
# Lendo dict:
for i in range(len(ranking)):
    print(f"{i+1}° lugar: {ranking[i][0]}, acertou {ranking[i][1]} no dado.")
