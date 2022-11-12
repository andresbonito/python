def CalculoBhaskara():
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))
    c = int(input("Digite o valor de c: "))
    
    delta = (b**2) - (4 * a * c)

    x1 = (((-1) * b) + (delta**0.5)) / (2 * a)
    x2 = (((-1) * b) - (delta**0.5)) / (2 * a)

    if delta <= 0:
        return "Não há raizes, pois o Delta é negativo"
    elif delta == 0:
        return "Há apenas uma raiz pois o Delta vale 0"
    elif delta > 0:
        return "A primeira raiz vale " + str(x1) +  "A segunda raiz vale " + str(x2)

print(CalculoBhaskara())