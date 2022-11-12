valor = float(input("Digite o valor a pagar: "))
cedulas = 0
atual = 100
apagar = valor
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        if atual >= 1:
            print("%d cedula(s) de R$%d" % (cedulas, atual))
        else:
            print("%d moeda(s) de R$%5.2f" % (cedulas, atual))
        if apagar < 0.01:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 2
        elif atual == 2:
            atual = 0.5
        elif atual == 0.5:
            atual = 0.10
        elif atual == 0.1:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.01
        cedulas = 0
