# Faça um programa que calcule a soma entre todos os impares que são
# múltiplos de 3 e que se encontram entre 1 e 500
soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        cont += 1
        soma += i
print('A soma dos {} números presentes é de: {}'.format(cont, soma))
