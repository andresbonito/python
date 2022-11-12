velocidade = int(input("Digite sua velocidade: "))
if velocidade > 120:
    print("Você foi multado!")
    multa = (velocidade - 120)*5
    print("Sua multa será de R$%.2f" %multa)
else:
    print("Ta tudo beleza chefia")
