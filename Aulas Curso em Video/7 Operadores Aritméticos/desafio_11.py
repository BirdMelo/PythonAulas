# Calcule a area de uma parede, com o programa lendo a altura e largura.
# Calcule quantos litros essa parede vai consumir sabendo que gasta 0.5L/m^2

H = int(input('qual é a altura da parede? '))
W = int(input('qual é a largura da parede? '))
A = H*W
L = A*0.5
print('sendo que a área é de {}m^2 para pintar essa parede usará {}L de tinta.'.format(A, L))
