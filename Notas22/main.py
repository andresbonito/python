from calculosDeNotas import *
from listas import *
from strings import tchau

print("""
1 - Banco de Dados
2 - Redes de Computadores
3 - Empreendedorismo
4 - Engenharia de Software
5 - Linguagens de Programação 2
6 - Arquitetura de Software
7 - Microcontroladores 
""")

começar = str(input("Quer calcular alguma nota? "))

def mainProgram():
    if começar in sim:
        materia = int(input("Digite o nº da materia que deseja calcular as notas: "))

        if materia == 1:
            print(calculoBancoDeDados())
        elif materia == 2:
            print(calculoRedes())
        elif materia == 3:
            print(calculoEmpreendedorismo())
        elif materia == 4:
            print(calculoEngSoft())
        elif materia == 5:
            print(calculoLP2())
        elif materia == 6:
            print(calculoArqSoft())
        elif materia == 7:
            print(calculoMicrocontroladores())
        else:
            return invalidSubject
        
print(mainProgram())

continuar = str(input("Deseja continuar calculando notas?: "))

while continuar in sim:
    print(mainProgram())
    if continuar is nao:
        print(tchau)
        break