distancia = float(input("Digite a distancia da viagem (em KM): "))
vm = float(input("Digite a velocidade media durante a viagem (em km/h): "))
dm = distancia*1000
vmms = vm/3.6
tempo = (dm)/vmms
tm = tempo/60
th = tm/60

print("A viagem demorou %.2f minutos, e em horas, %.2f h" %(tm, th))

# th = tm/60

# print("A viagem demorou, em horas, %.2f h" %th)
