# Crie um programa que leia vários números e coloque-os em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares
#   e os valores impares digitados, respectivamente.
# No final, mostre o conteudo das 3 listas geradas.
l: list = []
par: list = []
impar: list = []

# Criando a lista primaria:
while True:
    n = int(input("Digite um número: "))
    l.append(n)
    more = " "
    while more not in "sn":
        more = str(input("Quer continuar? [ S ] [ N ] ").strip().lower()[0])
        if more not in "sn":
            print("Digitação incorreta.")
    if more == "n":
        break
# Divisão de par e impar:
for i in range(len(l)):
    if l[i] % 2 == 0:
        par.append(l[i])
    if l[i] % 2 == 1:
        impar.append(l[i])
print(f"Lista: {l}")
print(f"Pares: {par}")
print(f"Impares: {impar}")
