# Crie um programa que leia varios números inteiros e só pare quando
#   for digitado 999.
# No final mostre quantos números foram digitados e qual foi a soma entre eles.
#   (desconciderando a flag)

print(5*'-'+'Somador'+5*'-')
print('Digite 999 para parar a soma')
n = s = 0.0
cont = 0
while True:
    print(20*'-')
    n = float(input('Digite um número: '))

    if n == 999:
        break

    s += n
    cont += 1
# Formatação de texto:
print(20*'-')
if cont >= 2:
    print(f'A soma desses {cont} números é de {s}')
elif cont == 1:
    print(f'Você digitou {s}')
else:
    print('Nada digitado.')
print(20*'-')
print('Encerrando atividade.')
