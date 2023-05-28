# Crie um programa onde o usuário possa digitar cinco valores númericos e
#   cadastre-os em uma lista, já na posição correta de inserção
#   (Sem usar o sort()).
# No final, mostre a lista ordenada na tela.
l: list = []
for n in range(0, 5):
    num = int(input("Digite um número: "))
    if n == 0 or num >= l[-1]:
        l.append(num)
    elif num <= l[0]:
        l.insert(0, num)
    else:
        i = 0
        while True:
            if l[i] >= num <= l[i + 1]:
                print(f"l[i+1]: {l[i+1]}")
                l.insert(l[i], num)
                break
            else:
                i += 1
    print(l)
