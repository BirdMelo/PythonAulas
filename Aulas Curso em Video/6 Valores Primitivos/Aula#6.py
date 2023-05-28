# Aula 6: https://www.youtube.com/watch?v=hdDHg1p3YVc
# na aula passada aprendemos a usar o input para o usúario poder digitar uma mensagem e ela se guardada em uma váriavel.
# nessa aula aprenderemos a guarda números nessas váriaveis.

n1 = int(input('primeiro número: '))
n2 = int(input('segundo número: '))
s = n1+n2
print('{} + {} = {}'.format(n1, n2, s))

# Esses são alguns tipos de valores primitivos.

e1 = str('1')  # String
print(type(e1), e1)
e2 = int(1)  # Inteiro
print(type(e2), e2)
e3 = float(1)  # Real
print(type(e3), e3)
e4 = bool(True)  # Boleano
print(type(e4), e4)
