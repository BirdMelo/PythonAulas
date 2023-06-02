# Aprimore o desafio anterior, mostrando no final:

# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior número da segunda linha.

# Criando matriz:
matriz: list = []
for i in range(3):
    stng = []
    for j in range(3):
        stng.append(int(input(f"Digite um número para [{i+1},{j+1}]: ")))
    matriz.append(stng)
print("-" * 20)
for i in range(3):
    print(" ".join(f"[{matriz[i][j]:^4}]" for j in range(3)))
print("-" * 20)

# Respondendo questões:
a = b = c = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] % 2 == 0:
            a += matriz[i][j]
        if j == 2:
            b += matriz[i][j]
        if i == 1:
            if j == 0:
                c == matriz[i][j]
            elif matriz[i][j] > c:
                c = matriz[i][j]
print(f"A: A soma de todos os valor pares é: {a}")
print(f"B: A soma de todos os valor da terceira coluna é: {b}")
print(f"C: O maior valor da segunda linha é: {c}")
