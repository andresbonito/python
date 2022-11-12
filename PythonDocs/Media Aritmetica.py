n = 1
soma = 0
y = int(input("Digite quantos numeros terá: "))
while n <= y:
    x = int(input("Digite o %d° número:" %n))
    soma = soma + x
    n = n + 1
print("Média: %5.2f" % (soma/y))