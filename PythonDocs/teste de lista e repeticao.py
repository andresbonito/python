import statistics

nome = str(input("Nome do Atleta: "))
x = 0
l = []

while x < 7:
    nota = float(input("Nota: "))
    l.append(nota)
    x = x + 1

print(" ")
print("Resultado final:")
print("Nome do Atleta: ", nome)

print("Maior nota: ", max(l, key=float))
print("Menor nota: ", min(l, key=float))
print("Média: %.2f" %statistics.mean(l))