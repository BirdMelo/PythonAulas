# Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
# No final, mostre qual foi o MAIOR e o MENOR valor digitado e as suas
#   respectivas posições na lista.
# Se os números MAIOR e/ou MENOR tiverem mais de uma posição
#    mostra todas as posições.
numL: list = []
for i in range(0, 5):
    n = int(input("Digite um número: "))
    if i == 0:
        bigger = smaller = n
    if bigger < n:
        bigger = n
    if smaller > n:
        smaller = n
    numL.append(n)
print(f"Maior:{bigger} Posição:", end=" ")
for i, v in enumerate(numL):
    if v == bigger:
        print(f"{i}", end=" ")
print()
print(f"Menor: {smaller} Posição:", end=" ")
for i, v in enumerate(numL):
    if v == smaller:
        print(f"{i}", end=" ")
print()
