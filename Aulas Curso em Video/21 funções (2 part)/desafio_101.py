# Crie um programa que tenha uma função chamada voto()
#   que vai receber como parâmetro o ano de nascimento de uma pessoa,
#   retornando um valor literal indicando se uma pessoa tem voto
#   NEGADO, OPICIONAL ou OBRIGATORIO nas eleições.
from datetime import datetime


def voto(nasc):
    """
    =====================================================
    --> A função recebe o ano de nascimento de uma pessoa
    e verifica sua condição para voto baseado na idade.
    =====================================================
    """
    atual = datetime.now().year
    idade = atual - nasc
    if idade >= 18 and idade <= 70:
        return "\033[32mOBRIGATORIO\033[m"
    elif idade < 16:
        return "\033[31mNEGADO\033[m"
    else:
        return "\033[33mFACULTATIVO\033[m"


n = int(input("Digite o ano de seu nascimento: "))
print(f"Seu voto é: {voto(n)}")
print(voto.__doc__)
