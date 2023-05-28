#   Crie um programa que leia vários números inteiros pelo teclado. O programa
# só vai parar quando o usuário digitar o valor de 999,
# que é a condição de parada.

#   No final, mostre quantos números foram digitados e a soma entre eles
# (Desconciderando o flag (999)).

q = soma = num = 0
while num != 999:
    num = int(input('Digite o {}° número [ 999 pra parar ]\n: '.format(q+1)))
    if num != 999:
        q += 1
        soma += num
print('Soma: {}\nQuantidade de Numeros: {}'.format(soma, q))
