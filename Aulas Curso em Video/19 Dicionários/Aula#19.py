# Dicionarios são estruturas assim como tuplas e listas,
#    mas agora com Dicionários podemos usar indices literais.
tuplas: tuple = ()
listas: list = []
dicionário: dict = {}
# Criando dicionário:
dicionário = {"nome": "Pedro", "idade": 17}
print(f"Criando dicionário: {dicionário}")
# Adicionando elementos ao dicionário.
# Se o index já existir dentro do dict ele irá substituir o elemento:
dicionário["sexo"] = "M"
print(f"Adicionando elementos: {dicionário}")
# Deletando elementos no dicionário:
del dicionário["sexo"]
print(f"Deletando elementos: {dicionário}")

print("=" * 50)

# Trabalhando com dicionário:
filme = {"Titulo": "Star Wars", "Ano": 1977, "Diretor": "George Lucas"}
# Mostrando os valores:
print(filme.values())
# Mostrando os indices ou chaves:
print(filme.keys())
# Mostrando os indices e os elementos, ou seja, os itens:
print(filme.items())
# For com dicionários:
for k, v in filme.items():
    print(f"O {k} é {v}")
# Dicionário com Lista:
locadora = [
    filme,
    {"Titulo": "Avengers", "Ano": 2012, "Diretor": "Joss Whedon"},
    {"Titulo": "Matrix", "Ano": 1999, "Diretor": "Wachowski"},
]
print(locadora[0]["Ano"])
print(locadora[2]["Titulo"])
# como o comando enumerate serve para se obter o index e elemento da
#   lista/tuplas, aqui não poderar ser usado, já que o index é em texto.

# Como fazer uma copia com dict:
estado = {}
brasil = []
for c in range(3):
    estado["UF"] = str(input("Unidade Federativa: "))
    estado["sigla"] = str(input("Sigla: "))
    brasil.append(estado.copy())
print(brasil)
