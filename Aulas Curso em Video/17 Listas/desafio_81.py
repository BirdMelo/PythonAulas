# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:

# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
l: list = []
a = 0
while True:
    n = int(input("Digite um número: "))
    l.append(n)
    a += 1
    more = " "
    while more not in "sn":
        more = str(input("Deseja continuar? [ S ] [ N ]: ").strip().lower()[0])
        if more not in "sn":
            print("Digitação incorreta.")
    if more == "n":
        break
print(f"Lista de números: {l}")
print(f"A: Foram {a} números.")
l.sort(reverse=True)
print(f"B: {l}")
if 5 in l:
    print("C: 5 foi encontrado na lista.")
else:
    print("C: 5 não foi encontrado na lista.")
