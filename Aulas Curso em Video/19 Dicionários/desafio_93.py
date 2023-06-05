# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols em cada partida.
# No final, tudo isso será guardado em um dicionário,
#   incluindo o total de gols feitos durante o campeonato.
aprov = {
    "Nome": input("Nome do jogador: "),
    "Partidas": int(input("Quantidade de partidas: ")),
}
golsp: list = []
for i in range(aprov["Partidas"]):
    golsp.append(int(input(f"Gols na {i+1}° na partida: ")))
aprov["Lista de Gols"] = golsp
tot = 0
for i in range(len(golsp)):
    tot += golsp[i]
aprov["Totgols"] = tot
print("=" * 50)
print(
    f'Jogador {aprov["Nome"]} jogou {aprov["Partidas"]} partidas e deu {aprov["Totgols"]} gols.'
)
for i in range(aprov["Partidas"]):
    print(f'{aprov["Lista de Gols"][i]} na {i+1}° partida.')
