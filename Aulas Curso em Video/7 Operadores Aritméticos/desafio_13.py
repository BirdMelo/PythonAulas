# faça um algoritmo que leia o salário de um funcionario e mostre
# seu novo salário, com 15% de aumento.

s = float(input('salário do funcionario: '))
print(
    'Com o aumento o salário do funcionario ficara R${:.2f}'.format(s+(s*0.15))
)
