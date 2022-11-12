print("""
    1 p/ Residencia
    2 p/ Comercial
    3 p/ Industria
    """)

instalação = int(input("Qual a instalação?"))

if instalação == 1:
    faixa = float(input("Quanto? "))
    if faixa <= 500:
        preço = faixa*0.4
        print("Pagará R$%.2f" % preço)
    else:
        preço = faixa*0.65
        print("Pagará R$%.2f" % preço)
elif instalação == 2:
    faixa = float(input("Quanto? "))
    if faixa <= 1000:
        preço = faixa*0.55
        print("Pagará R$%.2f" % preço)
    else:
        preço = faixa*0.6
        print("Pagará R$%.2f" % preço)
elif instalação == 3:
    faixa = float(input("Quanto? "))
    if faixa <= 5000:
        preço = faixa*0.55
        print("Pagará R$%.2f" % preço)
    else:
        preço = faixa*0.6
        print("Pagará R$%.2f" % preço)
