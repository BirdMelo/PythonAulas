# Crie um programa que tem uma tupla de zero a vinte,
#   todos escritos por extenso.
# Seu programa deverá ler um número pelo teclado e mostra-lo por extenso.


números = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "quatoze",
    "quinze",
    "dezesseis",
    "dezesete",
    "dezoito",
    "dezenove",
    "vinte",
)
while True:
    while True:
        n = int(input("Digite um número de 0 à 20: "))
        if 0 <= n <= 20:
            break
        print("Tente novamente", end=". ")
    print(f"Por extenso é {números[n]}.")
    more = str(input("Quer continuar? [ S ] [ N ]: ").strip().lower()[0])
    if more == "n":
        break
print("Fim do programa")
