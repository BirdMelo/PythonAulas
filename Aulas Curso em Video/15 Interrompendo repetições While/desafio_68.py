# Faça um programa que jogue "Par ou Impar" com o computador.
# O jogo só será interrompido quando o jogador PERDER,
#   mostrando o total de vitórias consecutivas que ele conquistou no final.

from random import randint

import emoji

cont = 0
while True:
    pc = randint(1, 10)
    escolha = str(input('Par ou Impar? ').lower())
    if escolha == 'par':
        print('Impar!')
        n = int(input('Digite um número: '))
        if (pc+n) % 2 == 0:
            print(emoji.emojize(f'{pc}! Você venceu :enraged_face:'))
            cont += 1
        elif (pc+n) % 2 == 1:
            print(emoji.emojize(
                f'{pc}! Eu venci :face_with_hand_over_mouth:' +
                f' E você venceu {cont} vezes.'))
            break
    elif escolha == 'impar':
        print('Par!')
        n = int(input('Digite um número: '))
        if (pc+n) % 2 == 1:
            print(emoji.emojize(f'{pc}! Você venceu :enraged_face:'))
        elif (pc+n) % 2 == 0:
            print(emoji.emojize(
                f'{pc}! Eu venci :face_with_hand_over_mouth:' +
                f' E você venceu {cont} vezes.'))
            break
    else:
        print(emoji.emojize('Digita direito!:face_with_steam_from_nose:'))
