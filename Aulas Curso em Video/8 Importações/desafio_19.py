# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido.
import random

No1 = input('digite o primeiro candidato: ')
No2 = input('digite o segundo candidato: ')
No3 = input('digite o terceiro candidato: ')
No4 = input('digite o quarto candidato: ')
Q = random.choice([No1, No2, No3, No4])
print('quem irá apagar o quadro é {}'.format(Q))
