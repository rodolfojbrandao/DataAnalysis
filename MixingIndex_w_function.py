import os
import numpy as np
import pandas as pd
import math
from pandas import DataFrame
from MixingIndex_functions import ReadFile, CellCount, GenerateFile
import time
start = time.time()

NF = 100 #number of files
NP = 7382 #number of particles
r1 = 0.003
r2 = 0.003
v1=(4/3*math.pi*r1*r1*r1)
v2=(4/3*math.pi*r2*r2*r2)

path='/home/rodolfo/Desktop/dados'
os.chdir(path)

posicaoX, posicaoY, posicaoZ, Tipo = ReadFile(NF,NP)
Volume, contador_tipo1, contador_tipo2 = CellCount(posicaoX, posicaoY, posicaoZ,Tipo,v1,v2,NF)
cout1 = GenerateFile(Volume, contador_tipo1, contador_tipo2,v1,v2,NF)

cout1 = pd.DataFrame(cout1)
indice = pd.DataFrame(cout1.std())
indice.to_csv('dados07cSerial.csv')

end = time.time()
print(end - start)