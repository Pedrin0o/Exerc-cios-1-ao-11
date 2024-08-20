m = float(input("Digite o valor de m: "))
n = float(input("Digite o valor de n: "))


produto = m * n


if produto > 0:
    print("O produto é positivo.")
elif produto < 0:
    print("O produto é negativo.")
else:
    print("O produto é zero.")