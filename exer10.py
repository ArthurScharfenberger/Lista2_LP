area = float(input("Digite a área a ser pintada em metros quadrados: "))

litros = area / 3
latas = litros / 18

if litros % 18 != 0:
    latas = int(latas) + 1
else:
    latas = int(latas)

preco = latas * 80

print("Quantidade de latas:", latas)
print("Preço total: R$", preco)
