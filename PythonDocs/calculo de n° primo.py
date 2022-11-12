n = int(input("Digite um numero: "))
if n < 0:
    print("Caso invalido. Digite numeros positivos.")
if n == 0 or n == 1:
    print("Caso especial. Digite outro valor.")
else:
    if n == 2:
        print("2 é um numero primo.")
    elif n % 2 == 0:
        print("Não é um numero primo, pois 2 é o unico numero par primo.")
    else:
        x = 3
        while(n > x):
            if n % x == 0:
                break
            x = x + 2
        if x == n:
            print("%d é um numero primo" % n)
        else:
            print("%d não é primo, pois é divisivel por %d" % (n, x))
