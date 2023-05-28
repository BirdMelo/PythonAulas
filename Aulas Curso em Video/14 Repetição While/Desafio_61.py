#   Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura While
num = int(input('Digite um número: '))
r = int(input('Digite a razão desse número: '))
i = 0
while i < 9:
    print('{}'.format(num), end=', ')
    num += r
    i += 1
print('{}'.format(num))
