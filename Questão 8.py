nome = str(input("Digite sua lista de nomes (Separe-os com , ): ")).split(',')
print(nome)
aux = 0
for item in nome:
    itens = nome[aux].split(' ')
    n1 = itens[0]
    n2 = itens[1]
    aux += 1
    print(n2,",",n1,";")
    


