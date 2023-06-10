# Faça um programa que tenha uma função chamada maior(),
#   que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def maior(*var):
    for c in range(len(var)):
        if c == 0:
            bigger = var[c]
        elif bigger < var[c]:
            bigger = var[c]
    print("=" * 40)
    print(f"A lista é {var}, total de {len(var)}")
    print(f"E o maior é: {bigger}")


maior(6, 2, 10, 1, 9, 12)
maior(8, 9, 9.5)
maior(0)
print("=" * 40)
