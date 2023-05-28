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
if numL.count(bigger) == 1:
    print(f"Maior: {bigger}; Posição: {numL.index(bigger)+1}")
    print(20 * "-")
else:
    print(f"Maior: {bigger}; Posição:", end=" ")
    for num in range(0, len(numL)):
        if numL[num] == bigger:
            print(f"{num+1}", end=" ")
    print("\n" + 20 * "-")
if numL.count(smaller) == 1:
    print(f"Menor: {smaller}")
    print(20 * "-")
else:
    print(f"Menor: {smaller}; Posição:", end=" ")
    for num in range(0, len(numL)):
        if numL[num] == smaller:
            print(f"{num+1}", end=" ")
    print("\n" + 20 * "-")
