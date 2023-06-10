# Faça um program que tenha uma lista chamada números e duas funções
#   chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e
#   a segunda função vai mostrar a soma entre todos os valores PARES sorteados
#   pela função anterior
from random import randint


def sorteia():
    lst = []
    for i in range(5):
        lst.append(randint(0, 9))
    print(f"Lista: {lst}")
    return lst


def somarPar(var):
    soma = 0
    for i in range(len(var)):
        if var[i] % 2 == 0:
            soma += var[i]
    print(f"Soma dos pares: {soma}")


somarPar(sorteia())
