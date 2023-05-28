# Crie um programa que leia a idaded e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar
#    se o usuário quer ou não continuar.
# No final, mostre:

# A) quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

a = b = c = 0
num_cadastro = 1
print('-------- Cadastro de Pessoas --------')
while True:
    print(37*'-')
    print(f'{num_cadastro}° Cadastro:')
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'fm':
        sexo = str(input('Digite o sexo: ').strip().lower()[0])
        if sexo not in 'fm':
            print('Digitação incorreta.')
    print(37*'-')
    if idade > 18:
        a += 1
    if sexo == 'm':
        b += 1
    if sexo == 'f' and idade < 20:
        c += 1
    more = ' '
    while more not in 'ns':
        more = str(input('Quer cadastrar mais alguem?\n').strip().lower()[0])
        if more not in 'ns':
            print('Digitação incorreta.')
    if more == 's':
        num_cadastro += 1
    else:
        break
print(37*'-')
if a > 0:
    if a == 1:
        print('Apenas 1 pessoa com mais de 18 anos cadastrada.')
    elif a > 1:
        print(f'Foram cadastrados {a} pessoas com mais de 18 anos.')
if b > 0:
    if b == 1:
        print('Apenas um homem cadastrado.')
    elif b > 1:
        print(f'Foram cadastrados {b} homens.')
if c > 0:
    if c == 1:
        print('Apenas uma mulher com menos de 20 anos cadastrada.')
    elif c > 1:
        print(f'Foram cadastradas {c} mulheres com menos de 20 anos.')
print('Fim do cadastro')
