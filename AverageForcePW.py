import math
import os
import numpy as np
import pandas as pd

NF = 601 #number of files

forceTotal = np.zeros((NF,1))

path='/home/lablinux/Desktop/post_paraviewPW'
os.chdir(path)

for j in range (0,NF):
    force = pd.read_csv('force.{}.csv'.format(j))
    len = force.shape[0]

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

    for i in range (0, len):
        d[i] = math.sqrt(a[i] + b[i] + c[i])

    forceTotal[j] = np.mean(d)

print(forceTotal)
forceTotal = pd.DataFrame(forceTotal)
forceTotal.to_csv('2-AverageForce.csv')