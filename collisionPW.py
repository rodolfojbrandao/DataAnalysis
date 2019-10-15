import os
import pandas as pd
from multiprocessing import Pool
import numpy as np
import math

N = 4   #number of cores
a = list(range(N))
NF = 600
forceTotal = np.zeros((NF,1))
colCounter = np.zeros((NF,1))

path = '//home/rodolfo/Desktop/15102019/colForcePW'
os.chdir(path)
result = 0

#os dados devem ser exportados do paraview como csv cell

def f(a):
    inicio = int(a*NF/N)
    fim = int((a+1)*NF/N)
    for j in range(inicio,fim):
        filenumber = j
        data = pd.read_csv('PW.{}.csv'.format(filenumber))
        force = data.iloc[:,8:11]
        force.to_csv('force.{}.csv'.format(filenumber))

if __name__=='__main__':
    Tarefas=len(a)
    with Pool(Tarefas) as p:
        p.map(f,a)

for j in range (0,NF):
    force = pd.read_csv('force.{}.csv'.format(j))
    len = force.shape[0]
    colCounter[j] = len

    forceTotal1 = np.zeros((len, 1))
    forceTotal2 = np.zeros((len, 1))
    forceTotal3 = np.zeros((len, 1))
    a = np.zeros((len, 1))
    b = np.zeros((len, 1))
    c = np.zeros((len, 1))
    d = np.zeros((len, 1))

    forceTotal1 = force.iloc[:, 1].copy()
    forceTotal2 = force.iloc[:, 2].copy()
    forceTotal3 = force.iloc[:, 3].copy()

    a = np.power(forceTotal1, 2)
    b = np.power(forceTotal2, 2)
    c = np.power(forceTotal3, 2)
    complete=j/NF*100
    print(complete)

    for i in range (0, len):
        d[i] = math.sqrt(a[i] + b[i] + c[i])

    forceTotal[j] = np.mean(d)

colCounter = pd.DataFrame(colCounter)
colCounter.to_csv('1-Number_of_Collisions_PW.csv')
forceTotal = pd.DataFrame(forceTotal)
forceTotal.to_csv('2-AverageForce_PW.csv')