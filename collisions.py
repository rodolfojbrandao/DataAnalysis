import os
import numpy as np
import pandas as pd
import math
from pandas import DataFrame

NF = 4000 #number of files
NP = 246 #number of particles

collisions = np.zeros((NP,NF))
col = pd.DataFrame(np.zeros((NF,1)))
path='/home/rodolfo/Desktop/25/CSVs_gran'
os.chdir(path)

for j in range (0,NF):
    filenumber = 18150 + 726 * j
    Dados = pd.read_csv('dumpgran{}.csv'.format(filenumber))
    collisions[:, j] = Dados.iloc[:, 1].copy()
    col=np.sum(collisions, axis=0)
    col = pd.DataFrame(col)
col.to_csv('dados_gran.csv')
