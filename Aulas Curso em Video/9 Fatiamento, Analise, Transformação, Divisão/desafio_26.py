# Faça um programa que leia uma frase pelo teclado e mostre:
# * Quantas vezes a letra "A" aparece;
# * Em que posição a primeira letra "A" aparece;
# * Em que posição a ultima letra "A" aparece.

a = str(input("Digite uma frase: ")).lower()
g = a.count('a')
h = a.find('a')+1
j = a.rfind('a')+1
print("""
    * A letra "A" aparece {} vezes;
    * Aparece, primeiramente, na {}° letra;
    * Sua ultima aparição é na {}° letra.
""".format(g, h, j))
