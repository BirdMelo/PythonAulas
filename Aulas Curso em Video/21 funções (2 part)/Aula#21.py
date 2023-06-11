import time


# criando um metodo com uma documentação sobre.
def destacar(var):
    """Destaca mensagens dentro do parenteses."""
    print("=" * 60)
    print(var)
    print("=" * 60)


# Digitar help no terminal acessa os manuais das importações bases do python,
#   como "time" ou "print".
# Digitando quit sai do help
# Help foi testado aqui e não funcionou.

# Doc também funciona como o help, dando informações sobre importações.
# Doc vai mostrar informações sobre a função anterior ao ponto.


destacar(print.__doc__)
# para poder falar sobre uma importação de fato precisa
#   importar ela para o código
destacar(time.__doc__)
destacar(destacar.__doc__)


# Paremetro opcional, É definido um padrão para um parametro
# Que se não mudado ao usar o metodo fica com o padrão de uso:
def somar(a, b, c=0):
    s = a + b + c
    print(f"A soma é de {s}")


somar(1, 3)
somar(1, 2, 3)


# Escopo:
def teste():
    # Escopo local:
    # Se for escrito "global n1" o n1 local se comportará como n1 global.
    # global a
    a = 4
    print(f"a local vale {a}")


# Escopo global:
a = 8
teste()
print(f"a global vale {a}")


# Retornando valores:


# Assim o metodo tomara a forma do resultado
def mult(a, b, c=1, d=1):
    m = a * b * c * d
    return m


r1 = mult(2, 3)
r2 = mult(3, 2, 8)
r3 = mult(2, 5, 10, 2)
print(f"Resultado das mutiplicações: {r1}, {r2}, {r3}")
