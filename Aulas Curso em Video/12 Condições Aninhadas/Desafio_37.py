# Escreva um programa que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de converção.

# 1 para bínario;
# 2 para octal;
# 3 para hexadecimal.

print(
    "Essa é uma conversora de números decimas para:" + " Binario, Octal e Hexadecimal."
)

num = int(input("Digite um número de decimal: "))

escolha = int(input("Escolha: 1-Bínario; 2-Octal; 3-Hexadecimal. "))
if escolha == 1:
    sb = []

    r = num % 2
    num = num // 2
    sb.append(str(r))
    while num >= 2:
        r = num % 2
        num = num // 2
        sb.append(str(r))

    sb.append(str(num))
    print("-" * 25)
    print("Valor em Binario é: {}".format("".join(list(reversed(sb)))))
    print("-" * 25)

elif escolha == 2:
    sh = []

    r = num % 8
    num = num // 8
    sh.append(str(r))
    while num > 1:
        r = num % 8
        num = num // 8
        sh.append(str(r))
    sh.append(str(num))
    print("-" * 25)
    print("Valor em Octal é: {}".format("".join(list(reversed(sh)))))
    print("-" * 25)

elif escolha == 3:
    sh = []

    r = num % 16
    num = num // 16
    if r == 10:
        sh.append("A")
    elif r == 11:
        sh.append("B")
    elif r == 12:
        sh.append("C")
    elif r == 13:
        sh.append("D")
    elif r == 14:
        sh.append("E")
    elif r == 15:
        sh.append("F")
    else:
        sh.append(str(r))

    while int(num / 16):
        r = num % 16
        num = num // 16
        if r == 10:
            sh.append("A")
        elif r == 11:
            sh.append("B")
        elif r == 12:
            sh.append("C")
        elif r == 13:
            sh.append("D")
        elif r == 14:
            sh.append("E")
        elif r == 15:
            sh.append("F")
        else:
            sh.append(str(r))

    sh.append(str(num))
    print("-" * 25)
    print("Valor em Hexadecimal é: {}".format("".join(list(reversed(sh)))))
    print("-" * 25)
