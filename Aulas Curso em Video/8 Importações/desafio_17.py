# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângolo, calcule
# calcule e mostre o comprimento da hipotenusa

CA = float(input('Digite o valor do cateto adjacente: '))
CO = float(input('Digite o valor do cateto oposto: '))
H2 = (CA**2)+(CO**2)
H = H2**(1/2)
print('sendo o cateto adjacente {:.2f} e o cateto oposto {:.2f} a hipotenusa é {:.2f}'.format(
    CA, CO, H))
