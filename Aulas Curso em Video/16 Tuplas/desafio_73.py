# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
#   Campionato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) os últimos 4 colocados na tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time Chapecoense.

Ranking = (
    "Flamengo",
    "Palmeiras",
    "Athletico Paranaense",
    "Atlético Mineiro",
    "São Paulo",
    "Fluminense",
    "Fortaleza",
    "Corithians",
    "Santos",
    "Internacional",
    "Grêmio",
    "América Mineiro",
    "Atlético Goianiense",
    "Ceará",
    "Bahia",
    "Botafogo",
    "Red Bull Bragantino",
    "Cruzeiro",
    "Goiás",
    "Cuiabá",
)
print("Os 5 primeiros colocados são:")
for c in range(0, 5):
    if c < 4:
        print(Ranking[c], end=", ")
    else:
        print(Ranking[c] + ".")
print("Os 4 ultimos colocados são:")
for u in range(-1, -5, -1):
    if u > -4:
        print(Ranking[u], end=", ")
    else:
        print(Ranking[u] + ".")
print("Ordem alfabética dos times:")
print(sorted(Ranking))
cont = 1
time = "Chapecoense"
while Ranking[cont - 1] != time:
    cont += 1
    if cont > 20:
        break
if cont <= 20:
    print(f"Time {time} está classificado no {cont}° lugar.")
else:
    print(f"Time {time} está abaixo do 20° lugar.")
