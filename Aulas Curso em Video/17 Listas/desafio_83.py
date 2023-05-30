# Crie um programa onde o usuário digite uma expressão qualquer que
#   usa parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses
#   abertos e fechados na ordem correta.
express = str(input("Digite uma expressão:\n"))
lp: list = []
for i in express:
    if i == "(":
        lp.append("(")
    elif i == ")":
        if len(lp) > 0:
            lp.pop()
        else:
            lp.append(")")
if len(lp) == 0:
    print("Expressão correta.")
else:
    print("Expressão incorreta.")
