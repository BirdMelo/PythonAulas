# Crie um programa onde o usuário possa digitar sete valores númericos e
#    cadastre-os em uma listagem única que mantenha separado
#    os valores pares e impares.
# No final, mostre os valores pares e impares em ordem crescente.
numeros: list[list[int]] = [[], []]
for i in range(7):
    num = int(input(f"Digite o {i+1}° número: "))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(f"Pares:{numeros[0]}. Impares{numeros[1]}.")
