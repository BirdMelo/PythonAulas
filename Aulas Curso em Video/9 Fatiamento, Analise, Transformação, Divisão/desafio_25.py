
# Crie um programa que leia o nome de uma
# pessoa e verifique se tem "Silva" nome

nome = str(input("Digite o nome de uma cidade: "))
g = nome.find('Silva')
if g >= 0:
    print('Nome contem Silva')
else:
    print('Nome não contem Silva')
