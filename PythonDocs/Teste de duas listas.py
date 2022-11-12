primeira = []
segunda = []
while True:
    e = int(input("Digite um valor para a primeira lista (0 para terminar): "))
    if e==0:
        break
    primeira.append(e)
while True:
    e = int(input("Digite um valor para a segunda lista (0 para terminar): "))
    if e==0:
        break
    segunda.append(e)
terceira = primeira[:] # Copia os elementos da primeira lista
terceira.extend(segunda)
x=0
while x < len(terceira):
    print("%d: %d" % (x, terceira[x]))
    x=x+1
