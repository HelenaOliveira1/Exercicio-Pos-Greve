N = int(input("Digite um número: "))
aux = 0

for soma in range(1, N+1):
    aux = aux + N
    N = N-1

print("A soma de todos os números é igual a: ", aux)
    
