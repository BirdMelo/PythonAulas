#   Estrutura de repetição While.
#   Essa estrutura fará a repetição enquanto for verdadeira. Exemplo:

n = 1
while n != 10:
    print(n)
    n += 1

#   Dessa forma ela contará de 1 até 9,
# pois quando alcançar o valor 10 irá sair da estrutura.

#   Mas For é mais simples quando se sabe os limites da repetição.

#   While se destaca mais em situações que não se sabe
# a quantidade de repetição necessária.

# Exemplo:
letra = str(input('S/N? ')).upper()
while letra == 'S':

    print('.')
    letra = str(input('S/N? ')).upper()
print(',')
