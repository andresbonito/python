def menorMaior(nome,menor,maior):
    if menor < maior :
        digitado = input('Digite a nota da %s: '%nome)
        Verificação = True
        while Verificação == True:
            if type(digitado) == str:
                try:
                    digitado = float(digitado)
                except ValueError:
                    print('Digite um número!')
                    digitado = input('Digite a nota da %s: '%nome)
            else:
                Verificação = False
                while (digitado < menor) or (digitado > maior):
                    print('Digite um valor de %i a %i.'%(menor,maior))
                    digitado = input('Digite a nota da %s: '%nome)
                    if type(digitado) == str:
                        Verificação = True
                        break
                    else:
                        digitado = float(digitado)
        return digitado
    else:
        return 'Erro'
