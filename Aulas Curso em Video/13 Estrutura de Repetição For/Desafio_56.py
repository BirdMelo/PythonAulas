# Desenolva um programa que leia o nome, idade e sexo de 4 pessoas
# No final do programa, mostre:

# > A média de idade do grupo;
# > Qual é o nome do homem mais velho;
# > Quantas mulheres têm menos de 20 anos.

soma = 0
media = 0
maiorM = 0
q20 = 0
velho = ''
for i in range(0, 4):
    print('---------- {}° PESSOA ----------'.format(i+1))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [ M ] ou [ F ] : ')).upper().strip()

    soma += idade
    if sexo == 'M' and idade > maiorM:
        maiorM = idade
        velho = nome
    if sexo == 'F' and idade < 20:
        q20 += +1
media = soma/4
print(50*'-')
print('Média de idade dos participantes: {}'.format(media))
print('O homem mais velho é {} com {} anos'.format(velho, maiorM))
print('Nesse grupo temos {} mulheres com menos de 20 anos'.format(q20))
