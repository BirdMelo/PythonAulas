# Desenvolva um programa que leia quatro valores pelo teclado e
#   guarde-os em uma tupla.
# No final, mostre:
# A) Quantas vezes aparece o número 9
# B) Em que posição foi digitado o número 3 pela primeira vez.
# C) Quais foram os números pares.
l: list = []
for i in range(0, 4):
    n = int(input(f"Digite o {i+1} número: "))
    l.append(n)
t = tuple(l)
if t.count(9) == 1:
    print("O núemro 9 apareceu somente 1 vez")
else:
    print(f"O número 9 aparece {t.count(9)} vezes.")
i = 0
if 3 in t:
    print(f" O número 3 aparece na {t.index(3)+1}° posição")
else:
    print("número 3 não foi digitado em nem uma posição.")
print("Os números pares são: ", end="-")
for i in range(0, len(t)):
    if t[i] % 2 == 0:
        print(t[i], end="-")
