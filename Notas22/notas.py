print("""
1 - Banco de Dados
2 - Redes de Computadores
3 - Empreendedorismo
4 - Engenharia de Software
5 - Linguagens de Programação 2
6 - Arquitetura de Software
7 - Microcontroladores 
""")

materia = int(input("Digite o nº da materia que deseja calcular as notas: "))
sim = ['sim', 'Sim', 'SIm', 'SIM', 'sIM', 'siM']
nao = ['nao', 'não', 'Nao', 'Não', 'NAo', 'NÃo', 'NÃO', 'NAO', 'nAO', 'nÃO', 'nãO', 'naO']

def calculoBancoDeDados(sim, nao):
    oqtem = str(input("Essa materia possui provas?: "))
    if oqtem in sim:
        provas = int(input("Quantas provas já fez? "))
        trabalhos = int(input("Quantos trabalhos já fez? "))

        if provas == 4 and trabalhos == 2:
            print("Insira suas notas de Banco de Dados")
            p1 = float(input("Quanto tirou na P1?: "))
            p2 = float(input("Quanto tirou na P2?: "))
            p3 = float(input("Quanto tirou na P3?: "))
            p4 = float(input("Quanto tirou na P4?: "))
            t1 = float(input("Quanto tirou no T1?: "))
            t2 = float(input("Quanto tirou no T2?: "))

            mT = (t1 + t2)/2
            mP = (p1 + p2 + p3 + p4)/4
            mF = 0.7*mP + 0.3*mT

            print("Sua média final foi de %.2f" %mF)

            if mF >= 6:
                return "Passou em Banco de Dados"
            else:
                return "Não passou em Banco de Dados"

        else:
            print("Insira suas notas de Banco de Dados")
            p1 = float(input("Quanto tirou na P1?: "))
            p2 = float(input("Quanto tirou na P2?: "))
            p3 = float(input("Quanto tirou na P3?: "))
            t1 = float(input("Quanto tirou no T1?: "))

            p4 = 0
            t2 = 0

            p4 = (6*4) - (p1 + p2 + p3)
            t2 = (6*2) - t1

            return True, "Para passar de ano, será necessário: %.2f na P4 e %.2f no T2" %(p4, t2)
    elif oqtem in nao:
        return "Essa materia possui provas sim."
    else:
        return "Comando inválido."

def calculoRedes():
    oqtem = str(input("Essa materia possui provas?: "))
    if oqtem in sim:
        provas = int(input("Quantas provas já fez? "))
        trabalhos = int(input("Quantos trabalhos já fez? "))
        
        if provas == 2 and trabalhos == 4:
            print("Insira suas notas de Redes")
            p1 = float(input("Quanto tirou na P1?: "))
            p2 = float(input("Quanto tirou na P2?: "))
            t1 = float(input("Quanto tirou no T1?: "))
            t2 = float(input("Quanto tirou no T2?: "))
            t3 = float(input("Quanto tirou no T3?: "))
            t4 = float(input("Quanto tirou no T4?: "))

            mT = (t1 + t2 + t3 + t4)/4
            mP = (p1 + p2)/2
            mF = 0.6*mP + 0.4*mT

            print("Sua média final foi de %.2f" %mF)

            if mF >= 6:
                return True, "Passou em Redes"
            else:
                return "Não passou em Redes"

        else:
            print("Insira suas notas de Redes")
            p1 = float(input("Quanto tirou na P1?: "))
            t1 = float(input("Quanto tirou no T1?: "))
            t2 = float(input("Quanto tirou no T2?: "))
            t3 = float(input("Quanto tirou no T3?: "))

            p2 = 0
            t4 = 0

            p2 = (6 * 2) - p1

            t4 = (6 * 4) - (t1 + t2 + t3)

            return True, "Para passar de ano, será necessário: %.2f na P2 e %.2f no T4" %(p2, t4)
    elif oqtem in nao:
        return "Essa materia possui provas sim."
    else:
        return "Comando inválido."

def calculoEmpreendedorismo():
    oqtem = str(input("Essa materia possui provas?: "))
    if oqtem in sim:
        return "Não possui provas."
    elif oqtem in nao:
        provas = int(input("Quantas provas já fez? "))
        trabalhos = int(input("Quantos trabalhos já fez? "))
        
        if provas != 0:
            return "Essa materia não possui provas"
        else:
            if provas == 0 and trabalhos == 4:
                print("Insira suas notas de Empreendedorismo")
                t1 = float(input("Quanto tirou no T1?: "))
                t2 = float(input("Quanto tirou no T2?: "))
                t3 = float(input("Quanto tirou no T3?: "))
                t4 = float(input("Quanto tirou no T4?: "))

                mF = round(((t1 * 2) + (t2 * 2) + (t3 * 3) + (t4 * 3)) / 10, 2)

                if mF >= 6:
                    return "Passou em Empreendedorismo"
                else:
                    return "Não passou em Empreendedorismo"
            else:
                t1 = float(input("Quanto tirou no T1?: "))
                t2 = float(input("Quanto tirou no T2?: "))
                t3 = float(input("Quanto tirou no T3?: "))

                t4 = round(((6*10) - (t1 * 2) - (t2 * 2) - (t3 * 3) / 3), 2)

                return "Você precisará de %.2f no T4 de Empreendedorismo para passar." %t4
    else:
        return "Comando inválido."
        

def calculoEngSoft():
    oqtem = str(input("Essa materia possui provas?: "))
    if oqtem in sim:
        provas = int(input("Quantas provas já fez? "))
        trabalhos = int(input("Quantos trabalhos já fez? "))
        
        if provas == 2 and trabalhos == 4:
            print("Insira suas notas de Engenharia de Software:")
            p1 = float(input("Quanto tirou no P1?: "))
            p2 = float(input("Quanto tirou no P2?: "))
            t1 = float(input("Quanto tirou no T1?: "))
            t2 = float(input("Quanto tirou no T2?: "))
            t3 = float(input("Quanto tirou no T3?: "))
            t4 = float(input("Quanto tirou no T4?: "))
            t5 = float(input("Quanto tirou no T5?: "))
            t6 = float(input("Quanto tirou no T6?: "))
            t7 = float(input("Quanto tirou no T7?: "))
            t8 = float(input("Quanto tirou no T8?: "))

            T1 = (t1 + t2) / 2
            T2 = (t3 + t4) / 2
            T3 = (t5 + t6) / 2
            T4 = (t7 + t8) / 2

            mP = round(((p1 + p2) / 2), 2)
            mT = round(((T1 + T2 + T3 + T4) / 4), 2)
            mF = (0.6 * mP) + (0.4 * mT)

            if mF >= 6:
                return "Passou em Engenharia de Software"
            else:
                return "Não passou em Engenharia de Software"

        else:
            p1 = float(input("Quanto tirou no P1?: "))
            t1 = float(input("Quanto tirou no T1?: "))
            t2 = float(input("Quanto tirou no T2?: "))
            t3 = float(input("Quanto tirou no T3?: "))
            t4 = float(input("Quanto tirou no T4?: "))
            t5 = float(input("Quanto tirou no T5?: "))
            t6 = float(input("Quanto tirou no T6?: "))
            
            T1 = (t1 + t2) / 2
            T2 = (t3 + t4) / 2
            T3 = (t5 + t6) / 2
            
            p2 = (6 * 2) - p1
            T4 = (6 * 4) - (T1 + T2 + T3)

            return "Você precisará de %.2f na P2 e %.2f de média no T4" %(p2, T4)
    elif oqtem in nao:
        return "Essa materia possui provas."
    else:
        return "Comando inválido."

def calculoLP2():
    oqtem = str(input("Essa materia possui provas?: "))
    if oqtem in sim:
        provas = int(input("Quantas provas já fez? "))
        trabalhos = int(input("Quantos trabalhos já fez? "))
        
        if provas == 4 and trabalhos == 2:
            print("Insira suas notas de Linguagens de Programação 2:")
            p1 = float(input("Quanto tirou na P1?: "))
            p2 = float(input("Quanto tirou na P2?: "))
            p3 = float(input("Quanto tirou na P3?: "))
            p4 = float(input("Quanto tirou na P4?: "))
            t1 = float(input("Quanto tirou no T1?: "))
            t2 = float(input("Quanto tirou no T2?: "))

            mP = round((((2 * ((p1 + p2) / 2)) + (3 * ((p3 + p4) / 2))) / 5), 2)
            mT = (t1 + t2) / 2

            mF = (0.5 * mP) + (0.5 * mT)

            if mF >= 6:
                print("Passou em Linguagens de Programação 2")
            else:
                print("Não passou em Linguagens de Programação 2")
        else:
            p1 = float(input("Quanto tirou na P1?: "))
            p2 = float(input("Quanto tirou na P2?: "))
            p3 = float(input("Quanto tirou na P3?: "))
            t1 = float(input("Quanto tirou no T1?: "))
            
            p4 = (6 * 5) - (2 * ((p1 + p2) / 2)) - (3 * (p3 / 2))
            t2 = (6 * 2) - t1

            return "Você precisará de %.2f na P4 e %.2f no T2" %(p4, t2)
    elif oqtem in nao:
        return "Essa materia possui provas."
    else:
        return "Comando inválido."


def calculoArqSoft():
    oqtem = str(input("Essa materia possui provas?: "))
    if oqtem in sim:
        provas = int(input("Quantas provas já fez? "))
        trabalhos = int(input("Quantos trabalhos já fez? "))

        if provas == 2 and trabalhos == 2:
            print("Insira suas notas de Arquitetura de Software:")
            p1 = float(input("Quanto tirou na P1?: "))
            p2 = float(input("Quanto tirou na P2?: "))
            t1 = float(input("Quanto tirou na T1?: "))
            t2 = float(input("Quanto tirou no T2?: "))

            mP = ((p1 * 2) + (p2 * 3)) / 5
            mT = (t1 + t2) / 2

            mF = (mP * 0.5) + (mT * 0.5)

            if mF >= 6:
                print("Passou em Arquitetura de Software")
            else:
                print("Não passou em Arquitetura de Software")

        else:
            p1 = float(input("Quanto tirou na P1?: "))
            t1 = float(input("Quanto tirou na T1?: "))

            p2 = round((((6 * 5) - (p1 * 2)) / 3), 2)
            t2 = round(((6 * 2) - t1), 2)

            return "Você precisará de %.2f na P2 e %.2f no T2" %(p2, t2)
    elif oqtem in nao:
        return "Essa materia possui provas."
    else:
        return "Comando inválido."


def calculoMicrocontroladores():
    oqtem = str(input("Essa materia possui provas?: "))
    if oqtem in nao:
        trabalhos = int(input("Quantos trabalhos já fez? "))

        if trabalhos == 3:
            print("Insira suas notas de Microcontroladores: ")
            t1 = float(input("Quanto tirou no T1?: "))
            t2 = float(input("Quanto tirou no T2?: "))
            t3 = float(input("Quanto tirou no T3?: "))

            mF = ((4 * t1) + (3 * t2) + (3 * t3)) / 10

            if mF >= 6:
                print("Passou em Microcontroladores")
            else:
                print("Não passou em Microcontroladores")
        else:
            nTrabs = int(input("Quantos trabalhos já fez?: "))
            if nTrabs == 1:
                t1 = float(input("Quanto tirou no T1?: "))

                T2 = ((6 * 10) - (t1 * 4)) / 3

                return "Você precisará de %.2f em média, no T2 e T3 para passar" %T2
    elif oqtem in sim:
        return "Essa materia não possui provas."
    else:
        return "Comando inválido."


if materia == 1:
    print(calculoBancoDeDados(sim, nao))
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
    print("Matéria invalida")