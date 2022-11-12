x = float(input("Digite sua 1ª nota: "))
y = float(input("Digite sua 2ª nota: "))
z = float(input("Digite sua 3ª nota: "))
w = float(input("Digite sua 4ª nota: "))
notas = [x, y, z, w]
soma = 0
x = 0
while x < 4:
    soma = soma + notas[x]
    x = x + 1
print("Média: %.2f" % (soma/x))
