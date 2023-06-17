# Reescreva a função leiaInt() que fizemos no desafio 104,
#   incluindo agora a possibilidade de digitação de um número de tipo invalido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(msg):
    while True:
        n = input(msg)
        try:
            return int(n)
        except ValueError:
            print("Digite um número inteiro")


def leiaFloat(msg):
    while True:
        n = input(msg)
        try:
            return float(n)
        except ValueError:
            print("Digite um valor Real.")


print(leiaInt("Número inteiro: "))
print(leiaFloat("Número Real: "))
