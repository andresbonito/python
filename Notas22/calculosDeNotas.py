from funcsSecunds import *
from strings import *
from listas import *

def calculoBancoDeDados():
    oqtem = str(input("\nEssa materia possui provas?: "))
    if oqtem in sim:
        provas = int(input("\nQuantas provas já fez? "))
        trabalhos = int(input("\nQuantos trabalhos já fez? "))

        if provas == 4 and trabalhos == 2:
            print("\nInsira suas notas de Banco de Dados")
            p1 = menorMaior("\nP1", 0, 10)
            p2 = menorMaior("\nP2", 0, 10)
            p3 = menorMaior("\nP3", 0, 10)
            p4 = menorMaior("\nP4", 0, 10)
            t1 = menorMaior("\nT1", 0, 10)
            t2 = menorMaior("\nT2", 0, 10)

            mT = (t1 + t2)/2
            mP = (p1 + p2 + p3 + p4)/4
            mF = 0.7*mP + 0.3*mT

            print("\nSua média final foi de %.2f" %mF)

            if mF >= 6:
                return passou
            else:
                return naopassou

        else:
            print("\nInsira suas notas de Banco de Dados")
            p1 = menorMaior("\nP1", 0, 10)
            p2 = menorMaior("\nP2", 0, 10)
            p3 = menorMaior("\nP3", 0, 10)
            t1 = menorMaior("\nT1", 0, 10)

            p4 = 0
            t2 = 0

            p4 = (6*4) - (p1 + p2 + p3)
            t2 = (6*2) - t1

            return "\nPara passar de ano, será necessário: %.2f na P4 e %.2f no T2" %(p4, t2)
    elif oqtem in nao:
        return temProva
    else:
        return invalidCommand

def calculoRedes():
    oqtem = str(input("\nEssa materia possui provas?: "))
    if oqtem in sim:
        provas = int(input("\nQuantas provas já fez? "))
        trabalhos = int(input("\nQuantos trabalhos já fez? "))
        
        if provas == 2 and trabalhos == 4:
            print("\nInsira suas notas de Redes de Computadores")
            p1 = menorMaior("\nP1", 0, 10)
            p2 = menorMaior("\nP2", 0, 10)
            t1 = menorMaior("\nT1", 0, 10)
            t2 = menorMaior("\nT2", 0, 10)
            t3 = menorMaior("\nT3", 0, 10)
            t4 = menorMaior("\nT4", 0, 10)

            mT = (t1 + t2 + t3 + t4)/4
            mP = (p1 + p2)/2
            mF = 0.6*mP + 0.4*mT

            print("\nSua média final foi de %.2f" %mF)

            if mF >= 6:
                return passou
            else:
                return naopassou

        else:
            print("\nInsira suas notas de Redes de Computadores")
            p1 = menorMaior("\nP1", 0, 10)
            t1 = menorMaior("\nT1", 0, 10)
            t2 = menorMaior("\nT2", 0, 10)
            t3 = menorMaior("\nT3", 0, 10)

            p2 = 0
            t4 = 0

            p2 = (6 * 2) - p1

            t4 = (6 * 4) - (t1 + t2 + t3)

            return "\nPara passar de ano, será necessário: %.2f na P2 e %.2f no T4" %(p2, t4)
    elif oqtem in nao:
        return temProva
    else:
        return invalidCommand

def calculoEmpreendedorismo():
    oqtem = str(input("\nEssa materia possui provas?: "))
    if oqtem in sim:
        return naoTemProva
    elif oqtem in nao:
        provas = int(input("\nQuantas provas já fez? "))
        trabalhos = int(input("\nQuantos trabalhos já fez? "))
        
        if provas != 0:
            return "\nEssa materia não possui provas"
        else:
            if provas == 0 and trabalhos == 4:
                print("\nInsira suas notas de Empreendedorismo")
                t1 = menorMaior("\nT1", 0, 10)
                t2 = menorMaior("\nT2", 0, 10)
                t3 = menorMaior("\nT3", 0, 10)
                t4 = menorMaior("\nT4", 0, 10)

                mF = round(((t1 * 2) + (t2 * 2) + (t3 * 3) + (t4 * 3)) / 10, 2)

                if mF >= 6:
                    return passou
                else:
                    return naopassou
            else:
                t1 = menorMaior("\nT1", 0, 10)
                t2 = menorMaior("\nT2", 0, 10)
                t3 = menorMaior("\nT3", 0, 10)

                t4 = round(((6*10) - (t1 * 2) - (t2 * 2) - (t3 * 3) / 3), 2)

                return "\nVocê precisará de %.2f no T4 de Empreendedorismo para passar." %t4
    else:
        return invalidCommand
        

def calculoEngSoft():
    oqtem = str(input("\nEssa materia possui provas?: "))
    if oqtem in sim:
        provas = int(input("\nQuantas provas já fez? "))
        trabalhos = int(input("\nQuantos trabalhos já fez? "))
        
        if provas == 2 and trabalhos == 4:
            print("\nInsira suas notas de Engenharia de Software:")
            p1 = menorMaior("\nP1", 0, 10)
            p2 = menorMaior("\nP2", 0, 10)
            t1 = menorMaior("\nT1", 0, 10)
            t2 = menorMaior("\nT2", 0, 10)
            t3 = menorMaior("\nT3", 0, 10)
            t4 = menorMaior("\nT4", 0, 10)
            t5 = menorMaior("\nT5", 0, 10)
            t6 = menorMaior("\nT6", 0, 10)
            t7 = menorMaior("\nT7", 0, 10)
            t8 = menorMaior("\nT8", 0, 10)

            T1 = (t1 + t2) / 2
            T2 = (t3 + t4) / 2
            T3 = (t5 + t6) / 2
            T4 = (t7 + t8) / 2

            mP = round(((p1 + p2) / 2), 2)
            mT = round(((T1 + T2 + T3 + T4) / 4), 2)
            mF = (0.6 * mP) + (0.4 * mT)

            if mF >= 6:
                return passou
            else:
                return naopassou

        else:
            p1 = menorMaior("\nP1", 0, 10)
            t1 = menorMaior("\nT1", 0, 10)
            t2 = menorMaior("\nT2", 0, 10)
            t3 = menorMaior("\nT3", 0, 10)
            t4 = menorMaior("\nT4", 0, 10)
            t5 = menorMaior("\nT5", 0, 10)
            t6 = menorMaior("\nT6", 0, 10)
            
            T1 = (t1 + t2) / 2
            T2 = (t3 + t4) / 2
            T3 = (t5 + t6) / 2
            
            p2 = (6 * 2) - p1
            T4 = (6 * 4) - (T1 + T2 + T3)

            return "\nVocê precisará de %.2f na P2 e %.2f de média no T4" %(p2, T4)
    elif oqtem in nao:
        return temProva
    else:
        return invalidCommand

def calculoLP2():
    oqtem = str(input("\nEssa materia possui provas?: "))
    if oqtem in sim:
        provas = int(input("\nQuantas provas já fez? "))
        trabalhos = int(input("\nQuantos trabalhos já fez? "))
        
        if provas == 4 and trabalhos == 2:
            print("\nInsira suas notas de Linguagens de Programação 2:")
            p1 = menorMaior("\nP1", 0, 10)
            p2 = menorMaior("\nP2", 0, 10)
            p3 = menorMaior("\nP3", 0, 10)
            p4 = menorMaior("\nP4", 0, 10)
            t1 = menorMaior("\nT1", 0, 10)
            t2 = menorMaior("\nT2", 0, 10)

            mP = round((((2 * ((p1 + p2) / 2)) + (3 * ((p3 + p4) / 2))) / 5), 2)
            mT = (t1 + t2) / 2

            mF = (0.5 * mP) + (0.5 * mT)

            if mF >= 6:
                return passou
            else:
                return naopassou
        else:
            p1 = menorMaior("\nP1", 0, 10)
            p2 = menorMaior("\nP2", 0, 10)
            p3 = menorMaior("\nP3", 0, 10)
            t1 = menorMaior("\nT1", 0, 10)
            
            p4 = (6 * 5) - (2 * ((p1 + p2) / 2)) - (3 * (p3 / 2))
            t2 = (6 * 2) - t1

            return "\nVocê precisará de %.2f na P4 e %.2f no T2" %(p4, t2)
    elif oqtem in nao:
        return temProva
    else:
        return invalidCommand


def calculoArqSoft():
    oqtem = str(input("\nEssa materia possui provas?: "))
    if oqtem in sim:
        provas = int(input("\nQuantas provas já fez? "))
        trabalhos = int(input("\nQuantos trabalhos já fez? "))

        if provas == 2 and trabalhos == 2:
            print("\nInsira suas notas de Arquitetura de Software:")
            p1 = menorMaior("\nP1", 0, 10)
            p2 = menorMaior("\nP2", 0, 10)
            t1 = menorMaior("\nT1", 0, 10)
            t2 = menorMaior("\nT2", 0, 10)

            mP = ((p1 * 2) + (p2 * 3)) / 5
            mT = (t1 + t2) / 2

            mF = (mP * 0.5) + (mT * 0.5)

            if mF >= 6:
                return passou
            else:
                return naopassou

        else:
            p1 = menorMaior("\nP1", 0, 10)
            t1 = menorMaior("\nT1", 0, 10)

            p2 = round((((6 * 5) - (p1 * 2)) / 3), 2)
            t2 = round(((6 * 2) - t1), 2)

            return "\nVocê precisará de %.2f na P2 e %.2f no T2" %(p2, t2)
    elif oqtem in nao:
        return temProva
    else:
        return invalidCommand


def calculoMicrocontroladores():
    oqtem = str(input("\nEssa materia possui provas?: "))
    if oqtem in nao:
        trabalhos = int(input("\nQuantos trabalhos já fez? "))

        if trabalhos == 3:
            print("\nInsira suas notas de Microcontroladores: ")
            t1 = menorMaior("\nT1", 0, 10)
            t2 = menorMaior("\nT2", 0, 10)
            t3 = menorMaior("\nT3", 0, 10)

            mF = ((4 * t1) + (3 * t2) + (3 * t3)) / 10

            if mF >= 6:
                return passou
            else:
                return naopassou
        else:
            nTrabs = int(input("\nQuantos trabalhos já fez?: "))
            if nTrabs == 1:
                t1 = menorMaior("\nT1", 0, 10)

                T2 = ((6 * 10) - (t1 * 4)) / 3

                return "\nVocê precisará de %.2f em média, no T2 e T3 para passar" %T2
    elif oqtem in sim:
        return naoTemProva
    else:
        return invalidCommand