import os
import numpy as np
import pandas as pd
import math
from pandas import DataFrame

NF = 490 #number of files
NP = 490856 #number of particles
r1 = 0.0006
r2 = 0.0015
v1=(4/3*math.pi*r1*r1*r1)
v2=(4/3*math.pi*r2*r2*r2)
rx = 5
ry = 5
rz = 10
tamanho = rx*ry*rz-1

#velocidade_resultante = pd.DataFrame(np.zeros((NP,NF)))
contador1=list()
contador2=list()
contador=list()
cout1=list()
posicaoX = np.zeros((NP,NF))
posicaoY = np.zeros((NP,NF))
posicaoZ = np.zeros((NP,NF))
Tipo = np.zeros((NP,NF))
#Raio = np.zeros((NP,NF))
#vx = np.zeros((NP,NF))
#vy = np.zeros((NP,NF))
#vz = np.zeros((NP,NF))
contador_tipo1 = pd.DataFrame(np.zeros((tamanho,NF)))  # type: DataFrame
contador_tipo2 = pd.DataFrame(np.zeros((tamanho,NF)))
#velocidade_tipo1 = pd.DataFrame(np.zeros((tamanho,NF)))
#velocidade_tipo2 = pd.DataFrame(np.zeros((tamanho,NF)))
posicao_vetor = 1

path='/media/rodolfo/5A0819190818F5AB/DOUTORADO-SIMULACOES-COMPLETAS/PCC-efeito-combinado-tamanho-densidade/17/dados'
os.chdir(path)

# leitura e separaçao de dados
for j in range (0,NF):
    Dados = pd.read_csv('dados.{}.csv'.format(j))
    Tipo[:, j] = Dados.iloc[:, 1].copy()
#    vx[:,j] = Dados.iloc[:, 2].copy()
#    vy[:,j] = Dados.iloc[:, 3].copy()
#    vz[:,j] = Dados.iloc[:, 4].copy()
#    Raio[:, j] = Dados.iloc[:, 5].copy()
    posicaoX[:, j] = Dados.iloc[:, 6].copy()
    posicaoY[:, j] = Dados.iloc[:, 7].copy()
    posicaoZ[:, j] = Dados.iloc[:, 8].copy()

posicaoX=pd.DataFrame(posicaoX)
posicaoY=pd.DataFrame(posicaoY)
posicaoZ=pd.DataFrame(posicaoZ)
Tipo=pd.DataFrame(Tipo)
#Raio=pd.DataFrame(Raio)
#vx=pd.DataFrame(vx)
#vy=pd.DataFrame(vy)
#vz=pd.DataFrame(vz)

# rever gradeamento
max_x = float(posicaoX.iloc[:,[1]].max())
max_y = float(posicaoY.iloc[:,[1]].max())
max_z = float(posicaoZ.iloc[:,[1]].max())

min_x = float(posicaoX.iloc[:,[1]].min())
min_y = float(posicaoY.iloc[:,[1]].min())
min_z = float(posicaoZ.iloc[:,[1]].min())

gradeamentoX = (abs(max_x) + abs(min_x)) / rx
gradeamentoY = (abs(max_y) + abs(min_y)) / ry
gradeamentoZ = (abs(max_z) + abs(min_z)) / rz

#for i in range(0,NF):
#    velocidade_resultante.iloc[:,[i]] = vx.iloc[:,[i]]*vx.iloc[:,[i]]+vy.iloc[:,[i]]*vy.iloc[:,[i]]+vz.iloc[:,[i]]*vz.iloc[:,[i]]

#velocidade_resultante=velocidade_resultante.pow(1./2)
#V_medio = velocidade_resultante.mean(axis=0)

InferiorX=float(posicaoX.iloc[:,[1]].min())
InferiorY=float(posicaoY.iloc[:,[1]].min())
InferiorZ=float(posicaoZ.iloc[:,[1]].min())

for m in range(0,NF):
    p=0
    q=0,
    concluido = m/NF*100
    print(concluido)
    for n in range(1, len(vx)):
        px = math.floor((posicaoX.iloc[n,m]-min_x)/gradeamentoX)
        py = math.floor((posicaoY.iloc[n,m]-min_y)/gradeamentoY)
        pz = math.floor((posicaoZ.iloc[n,m]-min_z)/gradeamentoZ)
        posicao_vetor = -31+px+5*py+25*pz

        if Tipo.iloc[n,m]<1.5:
            contador_tipo1.iloc[posicao_vetor,m] = contador_tipo1.iloc[posicao_vetor,m]+1
        else:
            contador_tipo2.iloc[posicao_vetor, m] = contador_tipo2.iloc[posicao_vetor, m] + 1

for n in range(0, len(contador_tipo1)):
    if contador_tipo1.iloc[n,NF-1]>50:
        cout1.append((contador_tipo1.iloc[n,:]*v1)/((contador_tipo1.iloc[n,:]*v1)+(contador_tipo2.iloc[n,:]*v2)))

cout1=pd.DataFrame(cout1)
indice=pd.DataFrame(cout1.std())
indice.to_csv('dados17.csv')