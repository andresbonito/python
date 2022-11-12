distancia = float(input("Quantos KM você percorrerá? "))
if distancia <= 200:
    preço = distancia*0.5
    print("O preço da sua passagem será de R$%.2f" % preço)
else:
    preço = distancia*0.45
    print("O preço da sua passagem será de R$%.2f" % preço)
