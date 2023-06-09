# Aula sobre Funções como declarar e usar def's
# Pode se definir uma função nova com parametro ou sem parametro
# Como pode ser observado a baixo criamos uma variavel
#   para poder ser usada na função.
# Dando o valor a variavel nos paremetros de sua invocação.


def titulo(var):
    print("=" * 60)
    print(f"{var:^60}")
    print("=" * 60)


titulo("Central Aluno")


# Esse aqui é um método para colocar varios números em uma variavel,
#   transformando-a em uma tupla.
def contador(*num):
    print(num)
    print(f"São ao todo {len(num)}")


contador(1, 2, 3, 4, 8, 0, 2)


# Def com listas:
def dobra(lst):
    for i in range(len(lst)):
        lst[i] *= 2


lista = [4, 2, 1, 10, 5, 7, 3, 9]
print(lista)
dobra(lista)
print(lista)
