A = int(input("Digite o valor do inteiro A: "))
B = int(input("Digite o valor do inteiro B: "))


print("Antes da troca:")
print("A =", A)
print("B =", B)


A, B = B, A


print("Após a troca:")
print("A =", A)
print("B =", B)