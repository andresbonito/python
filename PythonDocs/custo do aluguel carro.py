kmp = float(input("Quantos dias você está com o carro alugado? "))
kmr = float(input("Quantos KM você rodou com o carro? "))
Custor = (kmp*60)+(kmr*0.15)
Custod = Custor*5.71

print("O preço a ser pago em doláres será de $%.2f" % Custor)
print("O preço a ser pago em reais será de R$%.2f" % Custod)
