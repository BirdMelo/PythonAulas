# Utilização de F-Strings e Breaks em loots while.

n = s = 0.0
while True:
    n = float(input('Digite um número: '))

    if n == 999:
        break

    s += n
# Utilizando o Break podemos evitar de fazer gambiarras
#  para retirar o flag da conta, por exemplo.
# F-Strings é o formato novo de colocar variaveis em Strings (3.6 a frente)

print(f'A soma foi de {s:.2f}')
