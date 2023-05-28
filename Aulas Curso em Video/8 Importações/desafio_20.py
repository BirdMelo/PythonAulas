# O mesmo professor do desafio anterior quer sortear a ordem apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

No1 = input('digite o primeiro candidato: ')
No2 = input('digite o segundo candidato: ')
No3 = input('digite o terceiro candidato: ')
No4 = input('digite o quarto candidato: ')
lista = [No1, No2, No3, No4]
random.shuffle(lista)
print('A ordem de aprensentação será:\n {}'.format(lista))
