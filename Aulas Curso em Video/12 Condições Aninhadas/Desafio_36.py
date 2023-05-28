# Escreva um programa para aprovar o empréstimo
# bancário para a compra de uma casa.

# O programa vai perguntar o valor da casa,
# o salário do comprador e em quantos anos ele vai pegar.

# Calcule o valor da prestação mensal, sabendo que ela não
# pode exceder 30% do salário ou então o emprestimo será negado.

vCasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual seu salário? '))
anos = float(input('Quantos anos deseja pagar a casa? '))

mensal = vCasa/(anos*12)

if mensal <= (salario*0.3):
    print('Você tem condição para pagar o lavor da prestação')
    print('R${:.2f} por mês.'.format(mensal))
else:
    print('Condição recusada, salario muito baixo ou digitação incorreta.')

print('Tenha um bom dia!')
