L = []
while True:
    n = int(input("Digite um numero (0 sai): "))
    if n == 0:
        break
    L.append(n)
    print(L)
x = 0
while x < len(L):
    print((L[x]))
    x = x + 1