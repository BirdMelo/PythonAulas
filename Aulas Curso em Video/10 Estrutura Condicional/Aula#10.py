# Estrutura condicional
n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
media = (n1+n2)/2
if media >= 6:
    print("Parabéns pela sua nota de {:.1f}!".format(media))
else:
    print('Sua média foi {:.1f} precisa estudar mais :/'.format(media))
