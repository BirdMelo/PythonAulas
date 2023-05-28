n = float(input('Número de espiras: '))
a = float(input('Área Transversal: '))
mi = (input('Permeabilidade do núcleo: '))
c = float(input('Comprimento: '))

if mi == "A":
    i = ((n**2)*(4*3.14*10-7)*a)/c
else:
    print("em desenvolvimento")
