# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:

# -Média abaixo de 5.0: REPROVADO!!;
# -Média entre 5,0 e 6,9: RECUPERAÇÃO!!;
# -Média 7.0 ou superior: APROVADO!!;

prova = float(input('Digite a nota da prova: '))
teste = float(input('Digite a nota do teste: '))
media = (prova+teste)/2

print('A sua média foi: {}'.format(media))

if media < 5:
    print('\033[1;31mREPROVADO!\033[m')
elif media >= 5 and media < 7:
    print('\033[1;33mRECUPERAÇÃO!\033[m')
elif media >= 7 and media <= 10:
    print('\033[1;32mAPROVADO!\033[m')
else:
    print('Digitação incorreta.')
