# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores,
#   incluindo um sistema de visualização de detalhes do
#   aproveitamento de cada jogador.
print(f'{" Dados do time ":=^49}')

# Captura de dados:

time: list = []
while True:
    aprov = {
        "Nome": input("Nome do jogador: "),
        "Partidas": int(input("Quantidade de partidas: ")),
    }
    golsp: list = []
    for i in range(aprov["Partidas"]):
        golsp.append(int(input(f"Gols na {i+1}° na partida: ")))
    aprov["Lista de Gols"] = golsp
    tot = sum(golsp)
    aprov["Totgols"] = tot
    time.append(aprov.copy())
    while True:
        more = input("Continuar registrando jogadores?\n").strip().lower()[0]
        if more in "sn":
            break
    if more == "n":
        break
    else:
        print("=" * 49)

# Planilha do time:

print(f'{"Planilha do time":=^49}')
print(f'|{" Camisa ":^15}|{" Jogador ":^15}|{" Tot Gols ":^15}|')
print("-" * 49)
for i in range(len(time)):
    print(f"|{i+1:^15}|{time[i]['Nome']:^15}|{time[i]['Totgols']:^15}|")
    print("-" * 49)
print("=" * 49)

# Dados do jogador:

print("Escolha um atleta para ver seus detalhes.")
while True:
    status = int(input("Número da camisa (0 para sair): "))
    if status == 0:
        break
    elif status > len(time):
        print("Não existe esse jogador no time.")
    else:
        jogador = time[status - 1]
        print(f'\nDetalhes do jogador {jogador["Nome"]}:\n')
        for i in range(len(jogador["Lista de Gols"])):
            print(f'Gols na {i+1}° partida: {jogador["Lista de Gols"][i]}')
