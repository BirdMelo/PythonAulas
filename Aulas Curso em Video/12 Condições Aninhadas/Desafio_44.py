# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:

# -À vista dinheiro/cheque: 10% de desconto;
# -À vista no cartão: 5% de desconto;
# -Em até 2x no cartão: preço normal;
# -3x ou mais no cartão: 20% de juros.

produto = float(input('Qual o valor do produto? '))
avista = str(input('Vai pagar à vista? '))
if avista == 'sim' or avista == 's' or avista == 'yes' or avista == 'y':
    tipo = str(input('dinheiro, cheque ou cartão? '))
    if tipo == 'dinheiro' or tipo == 'cheque':
        produto = produto-(produto*0.1)
        print('Okay. Ficou {}R${:.2f}{}'.format(
            '\033[1;32m', produto, '\033[m'))
    elif tipo == 'cartão':
        produto = produto-(produto*0.05)
        print('Okay. Ficou {}R${:.2f}{}'.format(
            '\033[1;32m', produto, '\033[m'))
    else:
        print('\033[1;31m'+'Digitação Incorreta'+'\033[m')
elif avista == 'não' or avista == 'n' or avista == 'no' or avista == 'ñ':
    print('Okay. Sem juros em parcelando em 2x,' +
          ' mas 3x ou mais é aplicado 20'+'%'+' de juros')
    vezes = int(input('Vai dividir em quantas vezes? '))
    if vezes == 2:
        print('Parcelamento em 2x o preço do produto. Será pago agora: {}R${}{}'.format(
            '\033[1;32m', produto/2, '\033[m'))
    else:
        print('Seu parcelamento foi de {}x irá se acrescentado 20'.format(vezes) +
              '%', 'de juros.')
        print('Pagamento fica {}R${}{} agora.'.format(
            '\033[1;32m', (produto+(produto*0.2))/vezes, '\033[m'))
else:
    print('\033[1;31m'+'Digitação Incorreta'+'\033[m')
