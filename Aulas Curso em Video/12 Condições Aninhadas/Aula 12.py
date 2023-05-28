direção = str(input('Digite a direção do carro: '))

if direção == 'esquerda':
    print("carro virou a esquerda.")
elif direção == 'direita':
    print('carro virou a direita.')
elif direção == 'frente':
    print('carro seguiu em frente.')
elif direção == 'ré':
    print('carro voltou de ré.')
elif direção in 'janela farol pisca-alerta porta-mala porta-luva ':
    print('Executando funções do carro.')
else:
    print('comando invalido.')
