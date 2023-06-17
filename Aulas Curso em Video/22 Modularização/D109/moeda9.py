def aumentar(var, p100, mot=False):
    """
    ==============================================
    --> Aumenta, em porcentagem, o valor.
    var: valor a ser aumentado.
    p100: valor em porcetagem a ser acrescentado.
    mot=False (default) apresentar o número em
        sua forma monetária
    ==============================================
    """
    if mot:
        return moeda(var + (var * (p100 / 100)))
    return var + (var * (p100 / 100))


def diminuir(var, p100, mot=False):
    """
    ============================================
    --> Diminui, em porcentagem, o valor.
    var: valor a ser diminuido.
    p100: valor em porcentagem a ser subtraido.
    mot=False (default) apresentar o número em
        sua forma monetária
    ============================================
    """
    if mot:
        return moeda(var - (var * (p100 / 100)))
    return var - (var * (p100 / 100))


def dobrar(var, mot=False):
    """
    ===============
    return var*2
    mot=False (default) apresentar o número em
        sua forma monetária
    ==============
    """
    if mot:
        return moeda(var * 2)
    return var * 2


def metade(var, mot=False):
    """
    =============
    return var/2
    mot=False (default) apresentar o número em
        sua forma monetária
    =============
    """
    if mot:
        return moeda(var / 2)
    return var / 2


def moeda(var, m="R$"):
    """
    ============================================
    Retorna uma formatação em número monetário.
    return f'{var:.2f}'
    ============================================
    """
    return f"{m}{var:.2f}".replace(".", ",")
