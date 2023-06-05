# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
#   cadastre-os (com idade) em um dicionário se por acaso a CTPS
#   for diferente de ZERO, o dicionário receberá também
#   o ano de contratação e o salario.
# Calcule e acrescente, além da idade,
#   com quantos anos a pessoa vai se aposentar.
from datetime import datetime

Dados = {"Nome": input("Nome: ")}
nasc = int(input("Ano de nascimento: "))
atual = datetime.now().year
Dados["Idade"] = atual - nasc
Dados["CTPS"] = ctps = int(input("Codigo da carteira de trabalho[0=null]: "))
if ctps > 0:
    Dados["Contr. year"] = int(input("Ano de contratação: "))
    Dados["Salario"] = int(input("Salario: "))
    Dados["Aposentadoria"] = Dados["Contr. year"] + 35
    Dados["Idade Aposen"] = Dados["Idade"] + Dados["Aposentadoria"] - atual
    print(f'De acordo com os dados: {Dados["Nome"]}', end="")
    print(f' de {Dados["Idade"]} anos, começou a trabalhar no ano de', end="")
    print(f' {Dados["Contr. year"]} e poderá se aposentar no ano de', end="")
    print(f' {Dados["Aposentadoria"]} com {Dados["Idade Aposen"]} anos.')
