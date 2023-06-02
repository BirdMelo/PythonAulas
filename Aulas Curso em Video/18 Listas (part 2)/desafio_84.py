# Faça um programa que leia nome e peso de várias pessoas,
#   guardando tudo em uma lista.
# No final, mostre:

# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

# Captura de dados
data = []
heavy = []
light = []
while True:
    name = str(input("Nome: "))
    Weight = float(input("Peso: "))
    data.append([name, Weight])
    while True:
        more = str(input("Quer continuar?\n").strip().lower()[0])
        if more in ["s", "n"]:
            break
        print("Digitação incorreta.")
    if more == "n":
        break

# Tratamento de dados
for i in data:
    print(f"Pessoa: {i[0]}. Pesa: {i[1]}Kg.")
    if i[1] > 75:
        heavy.append(i[0])
    else:
        light.append(i[0])
print(f"A: Foram cadastradas: {len(data)} pessoas")
print(f"B: Lista de pessoas mais pesada: {heavy}")
print(f"C: Lista de pessoas mais leve: {light}")
