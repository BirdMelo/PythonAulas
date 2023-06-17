# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indica o número a calcular e o outro chamado show,
#   que será um valor lógico (opicional) indicando se será
#   mostrado ou não na tela o processo de calculo do fatorial.
# Fazer o doc do metodo.
def fatorial(num, show=False):
    """
    ===========================================
    --> Faz o fatorial de um número.
    num: número a ser calculado.
    show = False (default): mostrar o calculo
    quando True.
    ===========================================
    """
    cont = 1
    for c in range(num, 0, -1):
        cont *= c
        if show:
            if c > 1:
                print(f"{c}", end=" x ")
            else:
                print(f"{c} = ", end="")
    return cont


print(fatorial(5, show=True))
print(fatorial.__doc__)
