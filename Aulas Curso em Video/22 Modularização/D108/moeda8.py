def aumentar(var, p100):
    """
    ==============================================
    --> Aumenta, em porcentagem, o valor.
    var: valor a ser aumentado.
    p100: valor em porcetagem a ser acrescentado.
    ==============================================
    """
    return var + (var * (p100 / 100))


def diminuir(var, p100):
    """
    ============================================
    --> Diminui, em porcentagem, o valor.
    var: valor a ser diminuido.
    p100: valor em porcentagem a ser subtraido.
    ============================================
    """
    return var - (var * (p100 / 100))


def dobrar(var):
    """
    ===============
    return var*2
    ==============
    """
    return var * 2


def metade(var):
    """
    =============
    return var/2
    =============
    """
    return var / 2


def moeda(var, m="R$"):
    """
    ============================================
    Retorna uma formatação em número monetário.
    return f'{var:.2f}'
    ============================================
    """
    return f"{m}{var:.2f}".replace(".", ",")
