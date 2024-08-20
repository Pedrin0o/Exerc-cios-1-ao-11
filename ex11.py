# Calcula o valor total a ser pago pelas fotocópias com base nas tarifas fornecidas
fotocopias = int(input("Digite a quantidade de fotocópias realizadas: "))

if fotocopias <= 10:
    custo = fotocopias * 0.25
elif fotocopias <= 30:
    custo = 10 * 0.25 + (fotocopias - 10) * 0.20
else:
    custo = 10 * 0.25 + 20 * 0.20 + (fotocopias - 30) * 0.10

print(f"O valor a ser pago é: R$ {custo:.2f}")
