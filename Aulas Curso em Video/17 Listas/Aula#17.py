# Essa aula é dedicada a 1° parte das aulas lista em pithon.
# Assim que se faz uma lista:
lista = ["Comida", "Bola", "Cançaso", "Planeta do Tesouro"]
print(lista)
# Para adicionar um valor:
# Observe que a lista oculpa de 0-3 espaços.
# usa-se o '.append()' para adicionar no final da lista:
lista.append("Viagem")  # assim a lista fica com 0-4 espaços.
print(lista)
# usa-se o '.insert(<posição>,'<novo elemento>') para
#  adicionar elementos nas lista na posição desejada, impurrando pra frente
#  os demais elementos.
lista.insert(1, "Gato")
print(lista)
# Metodos de Eliminação de dados:
del lista[2]  # Elimina o dado referente ao índice.
lista.pop(3)  # Um metodo que elimina elemento referente ao índice.
#   .pop() sem parametro elimina o ultimo elemento.
lista.remove("Viagem")  # Um método que elimina o dado expecifico do parametro.
# Todos os 3 vão eliminar o índice e reposicionar os índices restantes.

# Desse jeito expresso abaixo a variavel B não irá receber os valores de A.
#   Mas sim linkar as duas listas.
a = [1, 2, 3, 4]
b = a
b[2] = 2
print(f"Lista A: {a}")
print(f"Lista B: {b}")
# O jeito certo dos valores serem passados de uma lista a outra é:
c = [12, 13, 14, 15, 16]
v = c[:]  # usando metodo de fatiamento.
v[2] = 0
print(f"Lista c: {c}")
print(f"Lista v: {v}")
