# Crie um programa onde o usuário possa digitar cinco valores númericos e
#   cadastre-os em uma lista, já na posição correta de inserção
#   (Sem usar o sort()).
# No final, mostre a lista ordenada na tela.
l: list = []
for i in range(0, 5):
    num = int(input("Digite número: "))
    if i == 0 or num >= l[-1]:
        l.append(num)
    else:
        for c in range(len(l)):
            if num <= l[c]:
                l.insert(c, num)
                break
print(l)
