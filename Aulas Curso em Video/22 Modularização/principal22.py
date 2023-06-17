from D107 import moeda7
from D108 import moeda8
from D109 import moeda9
from D110 import moeda10
from D111 import dados, moeda11

price = dados.justnum("Digite um número: ")
print(f"Desafio 107: R${moeda7.metade(price)}")
print(f"Desafio 108: {moeda8.moeda(moeda8.metade(price))}")
print(f"Desafio 109: {moeda9.metade(price,True)}")
print("\nDesafio 110:")
print(moeda10.resumo(price, 40, 20))
print("\nDesafio 111-112:")
print(moeda11.resumo(price, 40, 30))
