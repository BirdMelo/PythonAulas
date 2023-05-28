# Crie um programa que tenha um tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ("Arroz", "nariz", "cabelo", "ruivo", "bebado", "crime")
for word in tupla:
    print(f"\n Vogais de {word}: ", end="")
    for letter in word:
        if letter.lower() in "aeiou":
            print(f"{letter}", end=" ")
