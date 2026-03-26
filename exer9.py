anos = int(input("Digite sua idade em anos: "))
meses = int(input("Digite sua idade em meses: "))
dias = int(input("Digite sua idade em dias: "))

idade_dias = (anos * 365) + (meses * 30) + dias

print(f"Sua idade em dias é {idade_dias}")