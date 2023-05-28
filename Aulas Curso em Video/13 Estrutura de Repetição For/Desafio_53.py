# Crie um programa que leia uma frase qualquer e diga se ela é um polindromo,
# desconciderando os espaços

# Exemplos:
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA

print('Verificação de a frase é um polindromo.')
print('')
frase = str(input('Digite uma frase: ')).strip().lower()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(junto, '|', inverso)
print(40*'-')
if junto == inverso:
    print('É um políndromo.')
else:
    print('Não é um políndromo.')
