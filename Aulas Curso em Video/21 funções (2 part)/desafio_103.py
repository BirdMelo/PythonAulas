# Faça um programa que tenha uma função chamada ficha(),
#   que receba dos parâmetros opcionais:
# O nome de um jogador e quantos gols ele marcou
# O programa deverá ser capaz de mostrar a ficha do jogador,
#   mesmo que algum dado não tenha sido informado corretamente.


def ficha(player="<desconhecido>", gols=0):
    """
    ==============================================
    --> Função que armazena 2 valores, player e
    gols, de faz uma frase com esses 2 valores.

    player: <desconhecido>
    gols: 0
    return: "Jogador <player> deu <gols> gol(s)"
    ==============================================
    """
    return f"Jogador {player} deu {gols} gol(s)"


j = input("Nome do jogador: ")
g = input("Quantidade de gols: ")

if g.isnumeric():
    g = int(g)
else:
    g = 0
if j.strip() == "":
    print(ficha(gols=g))
else:
    print(ficha(j, g))
