qdc = int(input("Quantos cigarros por dia você fuma? "))
qaf = float(input("Por quantos anos você fumou? "))
qafd = qaf*365 #n de anos para dias
qdcpd = qdc*10 #n de minutos perdidos
qdcpded = qdcpd/1440 #conversão de minutos para dias
perda = qafd*qdcpded #perda total de dias

print("Você perderá %.2d dias de vida" %perda)
