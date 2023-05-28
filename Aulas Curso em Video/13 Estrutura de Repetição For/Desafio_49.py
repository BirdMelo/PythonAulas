# Refaça o Desafio 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

num = int(input('Escolha um número: '))

for i in range(0, 11):
    print('{} * {} = {}'.format(num, i, num*i))
