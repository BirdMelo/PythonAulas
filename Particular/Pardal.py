temp = float(input('tempo percorrido do ponto A pro B: '))
mps = 1/temp
mkph = mps*3.6
print('Carro em {:.1f}Km/h'.format(mkph))
if 25 < mkph <= 50.0:
    print(27*'-')
    print('Carro passou com segurança.')
    print(27*'-')
elif mkph > 50.9:
    dif = mkph-50
    multa = 20+dif*10
    print(65*'-')
    print(
        'Carro acima da velocidade. Multa calculada de R${:.2f}.'.format(
            multa))
    print(65*'-')
else:
    dif = 25.9-mkph
    multa = 20+dif*5
    print(65*'-')
    print(
        'Carro abaixo da velocidade minima.' +
        ' Multa calculada de R${:.2f}.'.format(multa))
    print(65*'-')
