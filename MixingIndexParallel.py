import os
import numpy as np
import pandas as pd
import math
from pandas import DataFrame
from MixingIndex_functionParallel import ReadFile, CellCount, GenerateFile
from multiprocessing import Pool

N=8
NF = 100 #number of files
NP = 7382 #number of particles
r1 = 0.003
r2 = 0.003
v1=(4/3*math.pi*r1*r1*r1)
v2=(4/3*math.pi*r2*r2*r2)

path='/home/rodolfo/Desktop/dados'
os.chdir(path)

#Read input list ==================================
ReadInput = [
[NF,NP,N,0],
[NF,NP,N,1],
[NF,NP,N,2],
[NF,NP,N,3],
[NF,NP,N,4],
[NF,NP,N,5],
[NF,NP,N,6],
[NF,NP,N,7],
]
if __name__=='__main__':
    Tarefas=len(ReadInput)
    with Pool(Tarefas) as p:
        res = p.map(ReadFile,ReadInput)
res = [sum(i) for i in zip(*res)]
posicaoX=res[0]
posicaoY=res[1]
posicaoZ=res[2]
Tipo=res[3]

#CellCount Input list ===============================
CellCountInput = [
[posicaoX, posicaoY, posicaoZ,Tipo,v1,v2,NF,0,N],
[posicaoX, posicaoY, posicaoZ,Tipo,v1,v2,NF,1,N],
[posicaoX, posicaoY, posicaoZ,Tipo,v1,v2,NF,2,N],
[posicaoX, posicaoY, posicaoZ,Tipo,v1,v2,NF,3,N],
[posicaoX, posicaoY, posicaoZ,Tipo,v1,v2,NF,4,N],
[posicaoX, posicaoY, posicaoZ,Tipo,v1,v2,NF,5,N],
[posicaoX, posicaoY, posicaoZ,Tipo,v1,v2,NF,6,N],
[posicaoX, posicaoY, posicaoZ,Tipo,v1,v2,NF,7,N],
]
if __name__=='__main__':
    Tarefas=len(CellCountInput)
    with Pool(Tarefas) as p:
        res = p.map(CellCount,CellCountInput)
res = [sum(i) for i in zip(*res)]
Volume=res[0]
contador_tipo1=res[1]
contador_tipo2=res[2]

cout1 = GenerateFile(Volume, contador_tipo1, contador_tipo2,v1,v2,NF)
cout1 = pd.DataFrame(cout1)
indice = pd.DataFrame(cout1.std())
indice.to_csv('dados07cParallel.csv')