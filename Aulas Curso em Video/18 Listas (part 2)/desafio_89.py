# Crie um programa que leia nome e duas notas de vários alunos
#   e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média cada um e
#   permita que o usuário possa mostrar as notas de cada aluno individualmente
clas: list = []
student: list = []
while True:
    student.append(str(input("Nome do Aluno: ")))
    student.append(float(input("Nota do teste: ")))
    student.append(float(input("Nota da prova: ")))
    clas.append(student[:])
    student.clear()
    while True:
        more = str(input("Quer continuar?[S/N]\n").lower())
        if more in ["s", "n"]:
            break
        print('Digite apenas "S" ou "N".')
    if more == "n":
        break
print(f'{" Boletim ":=^51}')
for c in clas:
    print(f"Aluno: {c[0]}")
    print(f"Nota: {(c[1]+c[2])/2}")
    print("-" * 51)
while True:
    indiv = str(input("Quer ver as notas de um aluno?\n").lower())
    if indiv == "n":
        break
    elif indiv not in ["s", "n"]:
        print("-" * 25)
        print('Digite "S" ou "N"')
    else:
        while True:
            while True:
                person = str(input("Digite o nome do aluno:"))
                for i in range(len(clas)):
                    for j in range(len(clas[i])):
                        if clas[i][j] == person:
                            print("-" * 23)
                            print("{: ^23}".format(clas[i][0]))
                            print(f"Teste: {clas[i][1]} Prova: {clas[i][2]}")
                            print()
                            break
                    if clas[i][j] == person:
                        break
                if clas[i][j] == person:
                    break
                else:
                    print("Esse aluno não está registrado.")
            print("-" * 23)
            while True:
                more = str(input("Quer ver mais um aluno?[S/N]\n").lower())
                if more in ["s", "n"]:
                    break
                print("Digitação incorreta. Responda com [S/N]")
            if more == "n":
                break
        if more == "n":
            break
print("Volte sempre!")
