valor = float(input("Quanto custa a casa? "))
salario = float(input("Qual seu salario? "))
tempo = float(input("Quanto tempo levará para pagar? (em meses) "))
pm = valor/tempo
print("O valor da prestação mensal é R$%.2f" % pm)
if pm > salario*30/100:
    print("O emprestimo foi aprovado!")
else:
    print("O emprestimo não foi aprovado!")
