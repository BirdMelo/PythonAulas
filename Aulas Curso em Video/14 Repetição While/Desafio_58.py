#   Melhore o jogo do DESAFIO 028 ondeo computador vai "pensar" em um número
# entre 0 até 10.

#   Só que agora o jogador vai tentar adivinhar até acertar, mostrando no
# final quantos palpites foram necessários para vencer.
from random import randint

pc = randint(0, 10)
print('Adivinhe um número que estou pensando.')
eu = 11
times = 1
while eu != pc:
    eu = int(input(': '))
    if eu != pc:
        print(20*'-')
        print('Errou! Tente de novo.')
        times += 1
print('Acertou! Eu pensei no número {}.'.format(pc) +
      ' Parabéns acertou na {}° tentativa.'.format(times))
