# Faça um programa que tenha uma função chamada "escreva()",
#   que receba um texto qualquer como parâmetro e
#   mostre uma mensagem com tamanho adaptável.
def escreva(var):
    tam = len(var) + 4
    print("=" * tam)
    print(f"  {var}")
    print("=" * tam)


escreva("Ola cidações da cidade grande")
escreva("Curso em vídeo.")
escreva("Oi")
