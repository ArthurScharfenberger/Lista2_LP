valorConsumo = float(input("Qual o valor total de consumo? "))
qntPessoas = int(input("Insira a quantidade de pessoas na mesa: "))

taxa = valorConsumo * 0.10
valorTotal = valorConsumo + taxa
valorPessoa = valorTotal / qntPessoas

print(f"O valor total da conta é R$ {valorTotal}")
print(f"O valor por pessoa vai dar R$ {valorPessoa}")