import os
import numpy as np
import pandas as pd
import math
from pandas import DataFrame

NF = 494 #number of files
NP = 147465 #number of particles

r1 = 0.0009
r2 = 0.0021

v1=(4/3*math.pi*r1*r1*r1)
v2=(4/3*math.pi*r2*r2*r2)

rz = 10
tamanho = rz

cout1=list()
posicaoZ = np.zeros((NP,NF))
Tipo = np.zeros((NP,NF))
contador_tipo1 = pd.DataFrame(np.zeros((tamanho,NF)))  # type: DataFrame
contador_tipo2 = pd.DataFrame(np.zeros((tamanho,NF)))

path='/media/rodolfo/5A0819190818F5AB/Doutorado/numerico/PCC-efeito-combinado-tamanho-densidade/07/dados'
os.chdir(path)

for j in range (0,NF):
    Dados = pd.read_csv('dados.{}.csv'.format(j))
    Tipo[:, j] = Dados.iloc[:, 1].copy()
    posicaoZ[:, j] = Dados.iloc[:, 8].copy()

posicaoZ=pd.DataFrame(posicaoZ)
Tipo=pd.DataFrame(Tipo)

InferiorZ=float(posicaoZ.iloc[:,[1]].min())
SuperiorZ=float(posicaoZ.iloc[:,[1]].max())

gradeamentoZ = (abs(SuperiorZ) + abs(InferiorZ)) / rz

for m in range(0,NF):
    concluido = m/NF*100
    print(concluido)
    for n in range(1, len(posicaoZ)):
        pz = math.floor((posicaoZ.iloc[n,m]-InferiorZ)/gradeamentoZ)

        if Tipo.iloc[n,m]<1.5:
            contador_tipo1.iloc[pz,m] = contador_tipo1.iloc[pz,m]+1
        else:
            contador_tipo2.iloc[pz, m] = contador_tipo2.iloc[pz, m] + 1

for n in range(0, len(contador_tipo1)):
        cout1.append((contador_tipo1.iloc[n,:]*v1)/((contador_tipo1.iloc[n,:]*v1)+(contador_tipo2.iloc[n,:]*v2)))

cout1=pd.DataFrame(cout1)
cout1.to_csv('axialTD07.csv')