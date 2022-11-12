salario = int(input("Informe seu salario: "))
if salario > 1250:
    aumento = salario*10/100
    ns = salario + aumento
    print("Seu salario era de R$%.2f, houve um aumento de R$%.2f e ficou R$%.2f" % (salario, aumento, ns))
if salario <= 1250:
    aumento = salario*15/100
    ns = salario + aumento
    print("Seu salario era de R$%.2f, houve um aumento de R$%.2f e ficou R$%.2f" % (salario, aumento, ns))
