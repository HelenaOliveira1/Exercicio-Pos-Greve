N = int(input("Digite um número para o fatorial: "))
fatorial = 1

if (N != 0):
    for i in range(1,N+1):
        fatorial = fatorial * i

print("")     
print("O Fatorial de", N, "é", fatorial)
