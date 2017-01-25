quantidade = int(input("Digite, em média, quantos cigarros você fuma ao dia: "))
anos = int(input("Digite há quantos anos você fuma: "))
minutos = 0

for min in range(1, quantidade+1):
    minutos += 10

vida = (anos*365)*minutos

print("Fumando assim, você perdeu,", vida, "minutos da sua vida.")
