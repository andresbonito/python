a = float(input("Digite o 1° número: "))
b = float(input("Digite o 2° número: "))

print("""
1 - soma
2 - subtração
3 - multiplicação
4 - divisão
""")

operação = int(input("Digite a operação a ser feita: "))

if operação == 1:
    soma = a + b
    print(soma)
elif operação == 2:
    subtração = a - b
    print(subtração)
elif operação == 3:
    multiplicação = a*b
    print(multiplicação)
else:
    divisão = a/b
    print(divisão)
