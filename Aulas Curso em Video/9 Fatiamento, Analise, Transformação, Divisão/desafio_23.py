
# Faça um programa que leia um número de 0 a 9999 e
# mostre na tela cada um dos digitos separados.

n = str(input("Digite um número de quatro digitos: "))
print(
    """
    unidade: {}
    dezena:  {}
    centena: {}
    milhar:  {}
    """.format(n[3], n[2], n[1], n[0])
)
