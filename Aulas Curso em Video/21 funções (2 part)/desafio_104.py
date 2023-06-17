# Crie um programa que tenha a função leiaInt(), que vai funcionar
#   de forma semelhante a função input() do Python, só que fazendo a validação
#   para aceitar apenas um valor númerico.
# Ex: n=leiaInt('Digite um número')
def leiaInt(msg):
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            break
        print("Digitação incorreta")
    return valor


n = leiaInt("Digite um número: ")
print(n)
