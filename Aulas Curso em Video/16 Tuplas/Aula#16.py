# Tuplas são determinadas da sequintes formas:
lanche = ('Sandwich', 'Oragen Juice', 'Water')
# Mas depois da versão 3.5 pode ser escrita assim:
lanche = 'Sandwich', 'Oragen Juice', 'Water'
print(lanche)
# Para poder mostrar um item da lisca colocamos seu espaço de memoria entre []:
print(lanche[0])
# Tuplas são imutaveis
# lanche[1]='Soda' IT'S WRONG

# Exemplo de uso:
for food in lanche:
    if food != len(lanche):
        print(food, end=', ')
    else:
        print(food, end='. ')
print('Im full!')
# Mas pode ser feito assim tb:
# Dessa forma fica mais facil de se obter o contador, já que o cont irá
#   ter o número da memoria, não o nome comida
for cont in range(0, len(lanche)):
    if cont != len(lanche):
        print(lanche[cont], end=', ')
    else:
        print(lanche[cont], end='. ')
print('Im full!')
# Colocando a Tupla em ordem alfabetica. Atensão!: não muda tupla,
#   só autera sua visualização.
print(sorted(lanche))
