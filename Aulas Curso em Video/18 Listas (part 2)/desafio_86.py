# Crie uma programa que crie uma matriz de dimensão 3x3
#   e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
matriz: list = []
for j in range(3):
    stn = []
    for i in range(3):
        num = int(input(f"Digite um número para [{i+1},{j+1}]: "))
        stn.append(num)
    matriz.append(stn)
print("-" * 20)
for i in range(3):
    print(f"[{matriz[i][0]:^4}][{matriz[i][1]:^4}][{matriz[i][2]:^4}]")
print("-" * 20)
print(f'{"Fim do programa":^20}')
