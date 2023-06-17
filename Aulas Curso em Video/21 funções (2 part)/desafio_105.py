# Faça um programa que tenha uma função notas() que pode receber
#   várias notas de alunos e vai retornar um dicionario
#   com as seguintes informações:


# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação(opcional)
def notas(*nota, situ=False):
    som = 0
    for i in range(len(nota)):
        if i == 0:
            bigger = smaller = nota[i]
        elif nota[i] > bigger:
            bigger = nota[i]
        elif nota[i] < smaller:
            smaller = nota[i]
        som += nota[i]
    media = som / len(nota)
    turma = {
        "maior nota": bigger,
        "menor nota": smaller,
        "média da turma": f"{media:.2f}",
    }
    if situ:
        if media >= 7:
            turma["situação da turma"] = "BOA!"
        elif media < 5:
            turma["situação da turma"] = "ruim."
        else:
            turma["situação da turma"] = "mediana."
    return turma


turma = notas(6, 3, 10, 2, 3, 1, situ=True)
for k, v in turma.items():
    print(f"A {k} é {v}")
