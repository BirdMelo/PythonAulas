# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade:

# -Se ele ainda vai se alistar ao servirço militar;
# -Se é a hora de se alistar;
# -Se já passou a hora de se alistar.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Qual o ano do seu nascimento? '))
anoAtual = date.today().year

idade = (anoAtual-ano)
diferença = abs(18-idade)

if idade < 18:
    print('Ainda não chegou a hora de se alistar.')
    print('falta {} anos ainda pro seu alistamento! Volte em {}'.format(
        diferença, anoAtual+diferença))
elif idade == 18:
    print('O alistamento deve ser feito ainda esse ano.')
else:
    print('O alistamento foi ou deveria ter sido feito a {} anos. Ano de {}'.
          format(diferença, anoAtual-diferença))
