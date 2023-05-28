# Escreva um programa que pergunte o salário de um funcionario e
# calcule o valor do seu aumento.

# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Qual seu salario? '))

if salario > 1250:
    salario = salario+(salario*0.1)
    print(
        """Parabens! você recebeu um aumento de 10%. Seu salario atual é de R${:.2f}!"""
        .format(salario))
else:
    salario = salario+(salario*0.15)
    print(
        """Parabens! você recebeu um aumento de 15%. Seu salario atual é de R${:.2f}!"""
        .format(salario))
