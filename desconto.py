valor = float(input("Digite o valor da compra: R$ "))

if valor >= 200:
    desconto = 0.20
elif valor >= 100:
    desconto = 0.10
else:
    desconto = 0

valor_final = valor - (valor * desconto)
print(f"Desconto aplicado: {desconto * 100:.0f}%")
print(f"Valor final: R$ {valor_final:.2f}")
