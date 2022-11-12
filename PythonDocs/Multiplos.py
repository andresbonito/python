fim = int(input("Digite o último valor a imprimir: "))
x = int(input("Digite em qual valor começar a contagem: "))
divisor = (int(input("Qual será o dividendo?: ")))

while x <= fim:
    if x % divisor == 0:
        print(x)
    x = x + 1
