# Desenvolva uma logica que leia o peso e altura de uma pessoa, calcule seu IMC
# e mostre seu status, de acordo com a tabela abaixo:

# Abaixo de 18.5: Abaixo do Peso;
# Entre 18.5 e 25: Peso ideial;
# 25 até 30: Sobrepeso;
# 30 até 40: Obesidade;
# Acima de 40: Obesidade mórbita.

h = float(input('Sua altura: '))
kg = float(input('Seu peso: '))
imc = kg/(h**2)

if imc < 18.5:
    status = '\033[1;37m'+'Abaixo do Peso'+'\033[m'
elif imc < 25:
    status = '\033[1;32m'+'Peso ideal'+'\033[m'
elif imc < 30:
    status = '\033[1;33m'+'Sobrepeso'+'\033[m'
elif imc <= 40:
    status = '\033[1;31m'+'Obesidade'+'\033[m'
elif imc > 40:
    status = '\033[1;35m'+'Obesidade Mórbita'+'\033[m'

print('Seu status na tabela IMC é: {}.'.format(status))
