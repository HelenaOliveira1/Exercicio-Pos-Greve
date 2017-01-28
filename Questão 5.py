quantidade = int(input("Digite, em média, quantos cigarros você fuma ao dia: "))
anos = int(input("Digite há quantos anos você fuma: "))
minutos = 0

for min in range(1, quantidade+1):
    minutos += 10

vida = (anos*365)*minutos
horas = vida/60
dias = horas/24
meses = dias/30
anos = meses/12

print("Fumando assim, você perdeu %.2f anos da sua vida." %anos)
