print("Bem-vindo à Pizzaria!")

quantidade = int(input("Digite quantas pizzas deseja: "))
preco = float(input("Digite o preço da pizza que está no cardápio: "))
sem_imposto = quantidade * preco
taxa_imposto = 8.0
imposto = sem_imposto * (taxa_imposto / 100)
com_imposto = sem_imposto + imposto

print("")
print("Valor cobrado: ", com_imposto)
