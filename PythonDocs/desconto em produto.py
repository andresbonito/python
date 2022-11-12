mercadoria = float(input("Digite o valor da mercadoria: "))
pdd = int(input("Digite o percentual de desconto: "))
frete = float(input("Digite o valor do frete: "))
desconto = (mercadoria*pdd/100)
total = (mercadoria - desconto) + frete

print("O desconto foi de %.2f reais, portanto deverá pagar R$%.2f" %(desconto, total))
