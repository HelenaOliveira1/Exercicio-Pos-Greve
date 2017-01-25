
def valorpagamento(prestacao, d_atraso, multa, m_dia):
    if(d_atraso == 0):
        print("Valor Cobrado: ", prestacao)
        print("")
    else:
        v_multa = prestacao*multa
        v_dia = d_atraso*m_dia
        prestacao = prestacao+v_multa+v_dia
        print("Valor Cobrado: ", prestacao)
        print("")

prestacao = 1
aux = 0
prestacao_dia = 0

while (prestacao != 0):
    prestacao = float(input("Digite o valor da prestação: "))
    d_atraso = float(input("Digite o número de dias de atraso: "))
    multa = 3.0/100.0
    m_dia = 0.1/100.0
    valorpagamento(prestacao, d_atraso, multa, m_dia)
    aux += 1
    prestacao_dia += prestacao
        
print("")
print("Programa Encerrado")
print("")
print("Relatório do dia: ")
print("Quantidade de prestações pagas: ", aux-1)
print("Valor total das prestações pagas: ", prestacao_dia)
        
