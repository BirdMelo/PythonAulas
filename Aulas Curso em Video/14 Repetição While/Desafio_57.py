#   Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores 'M' ou 'F'.
#   Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('''Por favor, digite seu sexo.
[ M ] Masculino  [ F ]Feminino.
''')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('''Sexo invalido. Por favor, digite seu sexo.
[ M ] Masculino  [ F ]Feminino.
''')).strip().upper()[0]
if sexo == 'M':
    print('Sexo masculino!')
elif sexo == 'F':
    print('Sexo feminino!')
