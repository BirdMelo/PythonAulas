# A Confederação Nacional de Natação precisa de um programa que leia o ano de
# nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# -Até 9 anos:  MIRIM
# -Até 14 anos: INFANTIL
# -Até 19 anos: JUNIOR
# -Até 20 anos: SÊNIOR
# -Acima:       MASTER
from datetime import date

nascimento = int(input('Ano de nascimento do atleta: '))
idade = (date.today().year)-nascimento

if idade <= 9:
    atleta = 'MIRIM'
elif idade <= 14:
    atleta = 'INFANTIL'
elif idade <= 19:
    atleta = 'JUNIOR'
elif idade <= 20:
    atleta = 'SÊNIOR'
else:
    atleta = 'MASTER'

print('Atleta de {}{}{} anos e categoria {}{}{}'.format(
    '\033[1;34m', idade, '\033[m', '\033[1;34m', atleta, '\033[m'))
