# Faça um programa que tenha uma função chamada "área()",
#   que receba os dimensões de um terreno retangular
#   (largura e comprimento) e mostre a área do terreno.


# Funções:
def area(b, h):
    print(f"A área é {b*h}m²")


def titulo(var):
    print("=" * 30)
    print(f"{var:^30}")
    print("=" * 30)


# Programa principal:
titulo("Calculo de Área")
area(b=int(input("Valor da base da área: ")), h=(int(input("Valor da altura: "))))
print("=" * 30)
