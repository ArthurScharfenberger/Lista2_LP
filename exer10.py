area = float(input("Digite a área a ser pintada em metros quadrados: "))

litros = area / 3
latas = litros / 18 + 1
preco = int(latas) * 80

if litros % 18 == 0:
    latas = litros / 18
    preco = int(latas) * 80

print(f"Quantidade de latas: {int(latas)}")
print(f"Preço total: R$ {preco:.2f}")
