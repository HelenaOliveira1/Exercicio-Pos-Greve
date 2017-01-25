base = int(input("Digite um número para base da exponenciação: "))
expoente = int(input("Digite um número para o exponte da exponenciação: "))
exponenciacao = 1

for exp in range(1, expoente+1):
    exponenciacao = exponenciacao*base

print("")
print(base, "elevado a", expoente, "é igual a: ", exponenciacao)
