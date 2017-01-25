numero = int(input("Digite um número para o fatorial: "))
fatorial = 1

if (numero != 0):
    for i in range(1,numero+1):
        fatorial = fatorial * i

print("")     
print("O Fatorial de", numero, "é", fatorial)
