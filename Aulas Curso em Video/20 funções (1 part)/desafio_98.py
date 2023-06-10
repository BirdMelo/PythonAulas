# Faça um programa que tenha uma função chamada contador(),
#   que receba três parâmetros: inicio, fim, passo e realize a contagem
# Seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Um contador personalizado pelo usuário.
from time import sleep


def contador(i, f, p):
    if p == 0:
        print("Passo igual a 0 recebe 1.")
        p = 1
    print(f"{f'De {i} à {f} em {p} em {p}.':^40}")
    sleep(2.5)
    print("=" * 40)
    if i < f:
        f += 1
    elif i > f and p > 0:
        f -= 1
        p = -p
    elif i > f and p < 0:
        f -= 1
    for c in range(i, f, p):
        print(c, end=" ", flush=True)  # Usando flush para tirar o buffer.
        sleep(0.5)
    print("Fim.")
    print("=" * 40)


contador(1, 10, 1)
contador(10, 0, 2)
contador(i=int(input("Inicio: ")), f=int(input("Final: ")), p=int(input("Passo: ")))
