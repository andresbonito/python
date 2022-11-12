salario = int(input("Quanto você recebe de salario? "))
if salario < 1000:
        print("Não paga imposto!")
elif salario < 3000:
        print("Você pagará 20% de imposto!")
        imposto = (salario*20/100)
        total = salario - imposto
        print("Seu imposto será de R$%.2f" %imposto)
        print("Você receberá R$%.2f" %total)
else:
        print("Você pagará 35% de imposto!")
        imposto = (salario*35/100)
        total = salario - imposto
        print("Seu imposto será de R$%.2f" %imposto)
        print("Você receberá R$%.2f" %total)
