divida = float(input("Valor da dívida: R$  ")) #quanto ele tem de divida
taxa = float(input("Juros mensais (%):  ")) #quanto de taxa é cobrado 
tj = taxa/100
valor = float(input("Valor mensal a pagar: R$ ")) #quanto ele pagará por mes
mes = 1
if (divida * tj > valor):
    print("O valor da dívida nunca será pago,")
    print("pois o valor a ser pago por mês será menor")
    print("que a nova divida.")
else:
    saldo = divida #armazena a dívida em uma variavel nova
    jurop = 0 #representa o quanto já pagou de juros    
    while saldo > valor:
        juros = saldo * taxa / 100 #valor de taxa para pagar
        saldo = saldo + juros - valor  #conta a ser feita
        jurop = jurop + juros # total de juros pago
        print("O saldo da dívida no mes %d é de: R$%.2f" % (mes, saldo))#acumulará os meses
        mes = mes + 1
    print ("Para pagar uma dívida de R$%.2f, a %.2f %% de juros," % (divida, taxa))
    print ("você precisará de %d meses, pagando um total de R$%.2f de juros." % (mes-1, jurop))
    print ("No último mês, você teria um saldo residual de R$%.2f a pagar." % (saldo))
