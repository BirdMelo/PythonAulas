# Faça um programa que leia o nome e a média de um aluno,
#   Guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
# (Situação: Aprovado/Reprovado)
a = {"Aluno": input("Aluno: "), "Média": input("Média: ")}
if float(a["Média"]) >= 5.0:
    a["Situação"] = "Aprovado"
else:
    a["Situação"] = "Reprovado"
print(a)
