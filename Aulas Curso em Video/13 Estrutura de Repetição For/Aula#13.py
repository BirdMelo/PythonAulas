# Estrutura simples de For que conta de 0 a 6.
# Sempre é ignorado o ultimo número,
# por isso colocar o zero para repitir o codigo 7x
for c in range(0, 7):
    print('Oi')
print('fim')
print(5*'-')
# Função: range(<inicio>,<fim>,<condição final/iteração>)
for i in range(0, 6, 2):
    print(i)

print(5*'-')

# For está contando números do maior pro menor usando essa função:
for i in range(6, 0, -1):
    print(i)
