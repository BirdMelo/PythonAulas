# Crie um programa que vai gerar cinco números aleatórios e coloca em um tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor
#   e o maior valor que estão na tupla.
from random import randint

t = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print(f"Tupla: {t}")
print(f"Maior: {max(t)}")
print(f"Menor: {min(t)}")
