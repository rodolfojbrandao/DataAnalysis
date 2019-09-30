import os
import numpy as np
import pandas as pd
import math
from pandas import DataFrame

NF = 489 #number of files
NP = 16040 #number of particles
r1 = 0.003
r2 = 0.002
v1=(4/3*math.pi*r1*r1*r1)
v2=(4/3*math.pi*r2*r2*r2)
v = 0.03*0.03*0.03
rx = 5
ry = 5
rz = 10
tamanho = rx*ry*rz-1

contador1=list()
contador2=list()
contador=list()
cout1=list()
posicaoX = np.zeros((NP,NF))
posicaoY = np.zeros((NP,NF))
posicaoZ = np.zeros((NP,NF))
Tipo = np.zeros((NP,NF))
contador_tipo1 = pd.DataFrame(np.zeros((tamanho,NF)))  # type: DataFrame
contador_tipo2 = pd.DataFrame(np.zeros((tamanho,NF)))
Volume = pd.DataFrame(np.zeros((tamanho,NF)))

posicao_vetor = 1

path='/media/rodolfo/5A0819190818F5AB/DOUTORADO-SIMULACOES-COMPLETAS/CasosMisturados/06/dados'
os.chdir(path)

for j in range (0,NF):
    Dados = pd.read_csv('dados.{}.csv'.format(j))
    Tipo[:, j] = Dados.iloc[:, 1].copy()
    posicaoX[:, j] = Dados.iloc[:, 3].copy()
    posicaoY[:, j] = Dados.iloc[:, 4].copy()
    posicaoZ[:, j] = Dados.iloc[:, 5].copy()

posicaoX=pd.DataFrame(posicaoX)
posicaoY=pd.DataFrame(posicaoY)
posicaoZ=pd.DataFrame(posicaoZ)
Tipo=pd.DataFrame(Tipo)

max_x = float(posicaoX.iloc[:,[1]].max())
max_y = float(posicaoY.iloc[:,[1]].max())
max_z = float(posicaoZ.iloc[:,[1]].max())
min_x = float(posicaoX.iloc[:,[1]].min())
min_y = float(posicaoY.iloc[:,[1]].min())
min_z = float(posicaoZ.iloc[:,[1]].min())

gradeamentoX = (abs(max_x) + abs(min_x)) / rx
gradeamentoY = (abs(max_y) + abs(min_y)) / ry
gradeamentoZ = (abs(max_z) + abs(min_z)) / rz

InferiorX=float(posicaoX.iloc[:,[1]].min())
InferiorY=float(posicaoY.iloc[:,[1]].min())
InferiorZ=float(posicaoZ.iloc[:,[1]].min())

for m in range(0,NF):
    p=0
    q=0,
    concluido = m/NF*100
    print(concluido)
    for n in range(1, len(posicaoX)):
        px = math.floor((posicaoX.iloc[n,m]-min_x)/gradeamentoX)
        py = math.floor((posicaoY.iloc[n,m]-min_y)/gradeamentoY)
        pz = math.floor((posicaoZ.iloc[n,m]-min_z)/gradeamentoZ)
        posicao_vetor = -31+px+5*py+25*pz

        if Tipo.iloc[n,m]<1.5:
            contador_tipo1.iloc[posicao_vetor,m] = contador_tipo1.iloc[posicao_vetor,m]+1
        else:
            contador_tipo2.iloc[posicao_vetor, m] = contador_tipo2.iloc[posicao_vetor, m] + 1
Volume = contador_tipo1*v1/v*100+contador_tipo2*v2/v*100
#print(Area)
for n in range(0, len(Volume)):
    if Volume.iloc[n,NF-1]>5:
        cout1.append((contador_tipo1.iloc[n,:]*v1)/((contador_tipo1.iloc[n,:]*v1)+(contador_tipo2.iloc[n,:]*v2)))

cout1=pd.DataFrame(cout1)
indice=pd.DataFrame(cout1.std())
indice.to_csv('dados06.csv')