
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# * O nome com todas as letras maipusculas
# * O nome com todas minúsculas.
# * Quantas letras ao todo (sem considerar espaços)
# *Quantas letras tem o primeiro nome

nome = 'João Pedro de Melo Naves'

print(nome.upper())
print(nome.lower())
print(len(''.join(nome.lower().split())))
print(len(''.join(nome[:10].lower().split())))
