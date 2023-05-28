# Faça um programa que leia o nome de uma pesso a diga
# o primeiro nome;
# o ultimo nome.

nome = str(input("Digite um nome: ")).split()
stName = nome[0]
lstName = nome[len(nome)-1]
print("""Primeiro nome: {}.
Ultimo nome: {}.
""".format(stName, lstName))
