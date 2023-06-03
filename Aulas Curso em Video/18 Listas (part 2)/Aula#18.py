from random import randint

# Revisão da aula passada:
dados = []
dados2 = list()
# Para poder utilizar essa forma de lista é sempre bom lembrar que
#  a IDE sempre vai mandar um erro até ter um elemento dentro da lista
dados.append("Pedro")
dados2.append("Maria")
# Para evitar isso pode-se utilizar:
dados3: list = []
# Lista, em python, pode ter diferentes tipos de dados:
dados.append(23)
dados2.append(1)
print(dados)
# Assim podemos criar listas dentro de listas.
pessoas = list()
pessoas.append(dados)
pessoas.append(dados2)
print(pessoas)
# Ou assim:
gatos = [["Bartho", 2], ["Pimenta", 3], ["Artemis", 1]]
# acessando os dados da lista composta:
#   gatos[<índice da lista maior>][<índice da lista menor>]
print(gatos[1][0])
print(gatos[2])
# Se for adicionar uma lista a outra lista usando append():
tudo = []
tudo.append(pessoas[:])
tudo.append(gatos[:])
# Assim vc manda para a lista maior uma copia da lista menor.
# Se precisar ter uma alteração na lista menor somente dentro da lista maior
#  não mudará a lista menor original.
print(tudo)
# Lendo tudo com for:
for m in tudo:
    for s in m:
        print(f"{s[0]} tem {s[1]} anos.")

# Reestudando com Chat GPT:

# função max() procura o valor maximo em uma lista de valores.
u = [5, 2, 9, 10, 20]
print(max(u))
# função sum() soma todos os valores de uma lista, tupla..
g = [10, 10, 10, 10]
print(sum(g))
# Matriz usando for horizontal O-O:

matriz = [[randint(0, 9999) for i in range(3)] for j in range(3)]
for i in matriz:
    print(" ".join(f"[{num:^4}]" for num in i))
