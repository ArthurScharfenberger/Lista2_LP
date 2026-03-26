area = float(input("Digite a área a ser pintada em metros quadrados: "))

litros = area / 3
latas = litros / 18 + 1
preco = int(latas) * 80

print(f"Quantidade de latas: {int(latas)}")
print(f"Preço total: R$ {preco:.2f}")

#Como a quantidade de latas pode dar um valor quebrado, foi adicionada 1 lata.