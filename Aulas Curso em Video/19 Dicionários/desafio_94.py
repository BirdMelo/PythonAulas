# Crie um programa que leia nome, sexo e idade de várias pessoas,
#   guardando os dados de cada pessoa em um dict e todos os dict em uma list.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média da idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.

# Captura de Dados:

data = []
print(f'{" Registro de pessoas ":=^50}')
while True:
    person = {"nome": input("Nome: "), "idade": int(input("Idade: "))}
    while True:
        sexo = input("Sexo: ").strip().lower()[0]
        if sexo in "mf":
            person["sexo"] = sexo
            break
        print("Digitação incorreta. [M/F]]")
    data.append(person.copy())
    person.clear()
    print("=" * 50)
    while True:
        more = str(input("Registrar mais pessoas?\n").strip().lower()[0])
        if more in ["s", "n"]:
            break
        print("Digitação incorreta. [S/N]")
    print("=" * 50)
    if more == "n":
        break

# Tratamento de dados:
soma = 0
womenL = []
for i in range(len(data)):
    soma += data[i]["idade"]
    if data[i]["sexo"] == "f":
        womenL.append(data[i]["nome"])
mediaI = soma / len(data)
Biggmedia = []
for i in range(len(data)):
    if data[i]["idade"] > mediaI:
        Biggmedia.append(data[i]["nome"])

# Mostrar em terminal:

print(f"A: Foram cadastradas {len(data)} pessoas")
print(f"B: A média da idade do grupo é {mediaI:.2f}")
print(f"C: As mulheres do grupo são: {womenL}")
print(f"D: Pessoas com idade acima da média: {Biggmedia}")
print(f'{" Fim do programa ":=^50}')
