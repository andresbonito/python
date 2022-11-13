# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 23:55:38 2018

@author: Michael Pedroza Mattioli leite
"""
from os import system

#------------------------------------------------------------------------------------------

#Funções para calculo de médias bimestrais, anuais e ponderada(n=7)

def Médiaparcial1FG():
    Calculo = (( NotaP1)*2 +  (NotaT1))/3
    return Calculo

def Médiaparcial1C():
    Calculo = (( NotaP1*0.7) +  (NotaT1*0.3))
    return Calculo

def Médiaparcial1Ga():
    Calculo = (( NotaP1*0.7) +  (NotaT1*0.3))
    return Calculo


def Médiaparcial2FG():
    Calculo = (( NotaP1 + NotaP2) +  (NotaT1 + NotaT2)/2)/3
    return Calculo

def Médiaparcial2C():
    Calculo = (( NotaP1*0.7 + NotaP2*0.7) + (NotaT1*0.3 + NotaT2*0.3))/2
    return Calculo

def Médiaparcial2Ga():
    Calculo = (( NotaP1 + NotaP2)*0.7/2 +  (2*NotaT1 + 3*NotaT2)*0.3/5)
    return Calculo

         
def Médiaparcial3FG():
    Calculo = (( 2*(NotaP1 + NotaP2) + 3*NotaP3 )*2/7 + (NotaT1 + NotaT2 + NotaT3)/3)/3
    return Calculo

def Médiaparcial3C():
    Calculo = ( ( 2*(NotaP1 + NotaP2) + 3*NotaP3)*0.7 + (( 2*(NotaT1 + NotaT2) + 3*NotaT3)*0.3))/7
    return Calculo

def Médiaparcial3Ga():
    Calculo = ((2*(NotaP1 + NotaP2) + 3*NotaP3)*0.7)/7 + (( 2*NotaT1 + 3*NotaT2 + 3*NotaT3)*0.3)/8
    return Calculo

        
def Médiaparcial4FG():
    Calculo = ( ( 2*(NotaP1 + NotaP2) + 3*(NotaP3 + NotaP4))*2/10 + ((NotaT1 + NotaT2 +NotaT3 + NotaT4))*1/4 )/3
    return Calculo

def Médiaparcial4C():
    Calculo =  ((2*(NotaP1 + NotaP2) + 3*(NotaP3 + NotaP4))*0.7 +  (2*(NotaT1 + NotaT2) + 3*(NotaT3 + NotaT4))*0.3)/10
    return Calculo

def Médiaparcial4Ga():
    Calculo = ((2*(NotaP1 + NotaP2) + 3*(NotaP3 + NotaP4))*0.7 + ( 2*NotaT1 + 3*NotaT2 + 3*NotaT3 + 2*NotaT4)*0.3)/10
    return Calculo

def MédiaDesenho_Computação():
    Calculo = (NotaT1 + NotaT2 + NotaT3 + NotaT4 + NotaT5 + NotaT6 + NotaT7)
    return Calculo
#-----------------------------------------------------------------------------------------------

#Funções que calculam quanto precisa tirar com a nota de corte de 60%, alem de avisar ao usuario quanto ele precisa, ou se ele passou, ou se já pegou dp.

#Função que calcula a nota para tirar nos demais bimestres
def Aviso_e_Calculo (periodo):
    if periodo == 1:
        Notaparatirar = (60 - 2*Médiaparcial1)/8
        print ('Você precisa tirar no 2º, 3º e 4º Bimestre, média: %.2f' % Notaparatirar)
        
    if periodo == 2:
        Notaparatirar = (60 - 4*Médiaparcial2)/6
        print ('Você precisa tirar no 3º e 4º Bimestre, média: %.2f' % Notaparatirar)
        
    if periodo == 3:
        Notaparatirar = (60 - 7*Médiaparcial3)/3
        if Notaparatirar <= 0:
            print('Você passou de ano! Parabéns!')
            print('Sua média é maior do que 60%!')
        if Notaparatirar > 10:
            print('Você pegou dp.')
        elif Notaparatirar >0 :
            print ('Você precisa tirar no 4 Bimestre: %.2f' % Notaparatirar)
            
    if periodo == 4 :
        Notaparatirar = (60 - 10*Média)
        
        if Notaparatirar <= 0:
            print('Você passou de ano! Parabéns!')
            print('Sua Média é: %0.2f' %Média)
        else:
            print('Você pegou dp.')
            print('Sua Média é: %0.2f' %Média)

#Função que calcula a nota que precisa tirar atravez de uma média ponderada de trabalhos           
def MédiaDe_Co(periodo):
    if periodo == 1:
        MédiaD1 = (42 - MédiaD_C)/6
        print('Você precisa tirar %.2f nos demais trabalhos.'%MédiaD1)
    if periodo == 2:
        MédiaD1 = (42 - MédiaD_C)/5
        print('Você precisa tirar %.2f nos demais trabalhos.'%MédiaD1)
    if periodo == 3:
        MédiaD1 = (42 - MédiaD_C)/4
        if MédiaD1 > 10:
            print('Você pegou DP.')
        else: 
            print('Você precisa tirar %.2f nos demais trabalhos.'%MédiaD1)
    if periodo == 4:
        MédiaD1 = (42 - MédiaD_C)/3
        if MédiaD1 > 10:
            print('Você pegou DP.')
        else: 
            print('Você precisa tirar %.2f nos demais trabalhos.'%MédiaD1)
    if periodo == 5:
        MédiaD1 = (42 - MédiaD_C)/2
        if MédiaD1 <= 0:
            print('Você passou de ano, parabens! Sua média é: %0.2f'%MédiaD_C/5)
        if MédiaD1 > 10:
            print('Você pegou DP.')
        else: 
            print('Você precisa tirar %.2f nos demais trabalhos.'%MédiaD1)
    if periodo == 6:
        MédiaD1 = (42 - MédiaD_C)
        if MédiaD1 <= 0:
            print('Você passou de ano, parabens! Sua média é: %0.2f'%MédiaD_C/6)
        if MédiaD1 > 10:
            print('Você pegou DP.')
        else: 
            print('Você precisa tirar %.2f nos demais trabalhos.'%MédiaD1)
    if periodo == 7:
        MédiaD1 = (MédiaD_C)/7
        if MédiaD1 > 6:
            print('Você passou de ano, parabens! Sua média é: %0.2f'%MédiaD1)
        else:
            print ('Sua Média é abaixo de 6 %.2f'%MédiaD1)
            print('Você pegou DP.')

#-----------------------------------------------------------------------------------------------
    
#Funções que evitam o usuario digitar uma string 

#Função que verfica se o digitado é um número entre um intervalo (menor,maior)                  
def é_número_entre_menor_e_maior (nome,menor,maior):
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

#Função que verifica se irá usar um calculo bimestral, semestral ou de trabalho.
def periodo_de_avaliação (periodo, genero, menor, maior):
    if menor < maior :
        Periodo = input('Digite quant%ss %s você já fez: '%(genero, periodo)) #Usuário introduz quantidade de provas
        Verificação = True
        while Verificação == True: #Verifica se o digitado é numero inteiro entre 1 e 4
            if type(Periodo) == str or type(Periodo) == float:
                try:
                    Periodo = int(Periodo)
                except ValueError:
                    print('Digite um número inteiro!')
                    Periodo = input('Digite quant%ss %s você já fez: '%(genero, periodo))
            else:
                Verificação = False
                while (Periodo < menor) or (Periodo > maior):
                    print('Digite um valor de %i a %i.'%(menor,maior))
                    Periodo = input('Digite quant%ss %s você já fez: '%(genero, periodo))
                    if type(Periodo) == str or type(Periodo) == float:
                        Verificação = True
                        break
                    else:
                        Periodo = int(Periodo)
                        Verificação = False
        return Periodo
    else:
        return 'Erro'

#---------------------------------------------------------------------------------------------------


while True:

#Variaveis para reset
    NotaP1 = 0
    NotaP2 = 0
    NotaP3 = 0
    NotaP4 = 0
    
    NotaT1 = 0
    NotaT2 = 0
    NotaT3 = 0
    NotaT4 = 0
    NotaT5 = 0
    NotaT6 = 0
    NotaT7 = 0
    
    Médiaparcial1 = 0
    Médiaparcial2 = 0
    Médiaparcial3 = 0
    Média = 0
    
    MédiaD_C = 0
    
    Bimestre = 0
    Semestre = 0
    Trabalhos = 0
    
    Matéria = ''

#----------------------------------------------------------------------------------------------------
    
    Matérias = ['calculo', 'física', 'ga','química','introdução a engenharia', 'desenho', 'computação'] #Lista de Matérias
    Matérias_provasbimestrais = ['calculo', 'física', 'ga','química']
    Matérias_trabalhos = ['desenho', 'computação']
    
    print ('Escolha a matéria destre estas disponiveis:') #Tabela de Matérias Disponiveis
    
    i=0
    for aula in Matérias:
        if i==7:
            break
        print ('- ' + Matérias[i])
        i+=1
        
    print()
    
    Matéria = str(input('Digite a matéria: ')) #Usuário introduz uma matéria
    Matéria = Matéria.lower()
    while Matéria not in  Matérias: #Verifica se o usuario digitou uma matéria valida
        print('Digite uma Matéria valida.')
        Matéria = str(input('Digite a matéria: '))
        Matéria = Matéria.lower()
        
    if Matéria in Matérias_provasbimestrais:
        Bimestre = periodo_de_avaliação ('provas bimestrais', 'a', 1, 4)
        if Bimestre == 1:
        
            NotaP1 = é_número_entre_menor_e_maior ('P1',0,10)
            NotaT1 = é_número_entre_menor_e_maior ('T1',0,10)
            
            if Matéria == 'física' or Matéria == 'química' :
                Médiaparcial1 = Médiaparcial1FG()
                print()
                Aviso_e_Calculo (Bimestre)
                        
            if Matéria == 'calculo':
                Médiaparcial1 = Médiaparcial1C()
                print()
                Aviso_e_Calculo (Bimestre)
            
            if Matéria == 'ga':
                Médiaparcial1 = Médiaparcial1Ga()
                print()
                Aviso_e_Calculo (Bimestre)
            
        if Bimestre == 2:
        
            NotaP1 = é_número_entre_menor_e_maior ('P1',0,10)
            NotaP2 = é_número_entre_menor_e_maior ('P2',0,10)
            
            NotaT1 = é_número_entre_menor_e_maior ('T1',0,10)
            NotaT2 = é_número_entre_menor_e_maior ('T2',0,10)
            
            if Matéria == 'física' or Matéria == 'química' :
                Médiaparcial2 = Médiaparcial2FG()
                print()
                Aviso_e_Calculo (Bimestre)
                
            if Matéria == 'calculo':
                Médiaparcial2 = Médiaparcial2C()
                print()
                Aviso_e_Calculo (Bimestre)
                
            if Matéria == 'ga':
                Médiaparcial2 = Médiaparcial2Ga()
                print()
                Aviso_e_Calculo (Bimestre)
            
        if Bimestre == 3:
        
            NotaP1 = é_número_entre_menor_e_maior ('P1',0,10)
            NotaP2 = é_número_entre_menor_e_maior ('P2',0,10)
            NotaP3 = é_número_entre_menor_e_maior ('P3',0,10)
            
            NotaT1 = é_número_entre_menor_e_maior ('T1',0,10)
            NotaT2 = é_número_entre_menor_e_maior ('T2',0,10)
            NotaT3 = é_número_entre_menor_e_maior ('T3',0,10)
                
            if Matéria == 'física' or Matéria == 'química' :
                Médiaparcial3 =  Médiaparcial3FG()
                print()
                Aviso_e_Calculo (Bimestre)
                
            if Matéria == 'calculo':
                Médiaparcial3 = Médiaparcial3C()
                print()
                Aviso_e_Calculo (Bimestre)
                
            if Matéria == 'ga':
                Médiaparcial3 = Médiaparcial3Ga()
                print()
                Aviso_e_Calculo (Bimestre)
            
        if Bimestre == 4:
            
            NotaP1 = é_número_entre_menor_e_maior ('P1',0,10)
            NotaP2 = é_número_entre_menor_e_maior ('P2',0,10)
            NotaP3 = é_número_entre_menor_e_maior ('P3',0,10)
            NotaP4 = é_número_entre_menor_e_maior ('P4',0,10)
            
            NotaT1 = é_número_entre_menor_e_maior ('T1',0,10)
            NotaT2 = é_número_entre_menor_e_maior ('T2',0,10)
            NotaT3 = é_número_entre_menor_e_maior ('T3',0,10)
            NotaT4 = é_número_entre_menor_e_maior ('T4',0,10)
                
            if Matéria == 'física' or Matéria == 'química' :
                Média = Médiaparcial4FG()
                print()
                Aviso_e_Calculo (Bimestre)
                
            if Matéria == 'calculo':
                Média = Médiaparcial4C()
                print()
                Aviso_e_Calculo (Bimestre)
                
            if Matéria == 'ga':
                Média = Médiaparcial4Ga()
                print()
                Aviso_e_Calculo (Bimestre)
                        
    if Matéria in Matérias_trabalhos:
        Trabalhos = periodo_de_avaliação ('trabalhos', 'o', 1, 7)
        if Trabalhos == 1:
            NotaT1 = é_número_entre_menor_e_maior ('T1',0,10)
            MédiaD_C = MédiaDesenho_Computação()
            print()
            MédiaDe_Co(Trabalhos)
            
        if Trabalhos == 2:
            NotaT1 = é_número_entre_menor_e_maior ('T1',0,10)
            NotaT2 = é_número_entre_menor_e_maior ('T2',0,10)
            MédiaD_C = MédiaDesenho_Computação()
            print()
            MédiaDe_Co(Trabalhos)
        
            
        if Trabalhos == 3:
            NotaT1 = é_número_entre_menor_e_maior ('T1',0,10)
            NotaT2 = é_número_entre_menor_e_maior ('T2',0,10)
            NotaT3 = é_número_entre_menor_e_maior ('T3',0,10)
            MédiaD_C = MédiaDesenho_Computação()
            print()
            MédiaDe_Co(Trabalhos)
            
        if Trabalhos == 4:
            NotaT1 = é_número_entre_menor_e_maior ('T1',0,10)
            NotaT2 = é_número_entre_menor_e_maior ('T2',0,10)
            NotaT3 = é_número_entre_menor_e_maior ('T3',0,10)
            NotaT4 = é_número_entre_menor_e_maior ('T4',0,10)
            MédiaD_C = MédiaDesenho_Computação()
            print()
            MédiaDe_Co(Trabalhos)
        
        if Trabalhos == 5:
            NotaT1 = é_número_entre_menor_e_maior ('T1',0,10)
            NotaT2 = é_número_entre_menor_e_maior ('T2',0,10)
            NotaT3 = é_número_entre_menor_e_maior ('T3',0,10)
            NotaT4 = é_número_entre_menor_e_maior ('T4',0,10)
            NotaT5 = é_número_entre_menor_e_maior ('T5',0,10)
            MédiaD_C = MédiaDesenho_Computação()
            print()
            MédiaDe_Co(Trabalhos)
        
        if Trabalhos == 6:
            
            NotaT1 = é_número_entre_menor_e_maior ('T1',0,10)
            NotaT2 = é_número_entre_menor_e_maior ('T2',0,10)
            NotaT3 = é_número_entre_menor_e_maior ('T3',0,10)
            NotaT4 = é_número_entre_menor_e_maior ('T4',0,10)
            NotaT5 = é_número_entre_menor_e_maior ('T5',0,10)
            NotaT6 = é_número_entre_menor_e_maior ('T6',0,10)
            MédiaD_C = MédiaDesenho_Computação()
            print()
            MédiaDe_Co(Trabalhos)
        
            
        if Trabalhos == 7:
            
            NotaT1 = é_número_entre_menor_e_maior ('T1',0,10)
            NotaT2 = é_número_entre_menor_e_maior ('T2',0,10)
            NotaT3 = é_número_entre_menor_e_maior ('T3',0,10)
            NotaT4 = é_número_entre_menor_e_maior ('T4',0,10)
            NotaT5 = é_número_entre_menor_e_maior ('T5',0,10)
            NotaT6 = é_número_entre_menor_e_maior ('T6',0,10)
            NotaT7 = é_número_entre_menor_e_maior ('T7',0,10)
            MédiaD_C = MédiaDesenho_Computação()
            print()
            MédiaDe_Co(Trabalhos)
        
    if Matéria == 'introdução a engenharia':
        print('Ainda em desenvolvimento')
        # Semestre = periodo_de_avaliação ('provas semestrais', 'a', 1, 2)
    
    print()
    print()
    
    sim_não = ['s', 'sim', 'n', 'nao', 'não', 'ñ']
    Pergunta = str(input('Deseja calcular outra nota? (S/N): '))
    Pergunta = Pergunta.lower()
    while Pergunta not in sim_não:
        print('Escolha sim ou não')
        Pergunta = str(input('Deseja calcular outra nota? (S/N): '))
        Pergunta = Pergunta.lower()
    if Pergunta == 'sim' or Pergunta == 's':
        system('cls')
    else:
        break