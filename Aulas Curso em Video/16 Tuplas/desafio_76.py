# Crie um programa que tenha um tupla única com nomes de produtos e
#   seus respectivos preços, na sequencia.
# No final, mostre uma listagem de preços,
#   organizandos os dados em forma tabular.
product = (
    "Pacote pano",
    12.00,
    "Cabo usb",
    44.00,
    "Pacote com 12 tijela",
    30.00,
    "Um par de tenis",
    60.00,
    "Um par de chinelo",
    19.00,
    "Cochão",
    200.00,
    "Redragon soundbox",
    180.00,
    "Mouse multilaser",
    50.00,
)

print(59 * "=")
print("{: ^59}".format("-WALMART-"))
print(59 * "=")
for i in range(0, len(product), 2):
    print(f"{product[i]:.<49}R$:{product[i+1]:>7.2f}")
print(59 * "=")
