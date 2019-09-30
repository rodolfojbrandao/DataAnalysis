import math
import os
import numpy as np
import pandas as pd

NF = 601 #number of files

velTotal = np.zeros((NF,1))

path='/home/lablinux/Desktop/post_paraviewPP'
os.chdir(path)

for j in range (0,NF):
    velocity = pd.read_csv('velocity2.{}.csv'.format(j))
    len = velocity.shape[0]

    velTotal1 = np.zeros((len, 1))
    velTotal2 = np.zeros((len, 1))
    velTotal3 = np.zeros((len, 1))
    a = np.zeros((len, 1))
    b = np.zeros((len, 1))
    c = np.zeros((len, 1))
    d = np.zeros((len, 1))

    velTotal1 = velocity.iloc[:, 1].copy()
    velTotal2 = velocity.iloc[:, 2].copy()
    velTotal3 = velocity.iloc[:, 3].copy()

    a = np.power(velTotal1, 2)
    b = np.power(velTotal2, 2)
    c = np.power(velTotal3, 2)

    for i in range (0, len):
        d[i] = math.sqrt(a[i] + b[i] + c[i])

    velTotal[j] = np.mean(d)

print(velTotal)
velTotal = pd.DataFrame(velTotal)
velTotal.to_csv('4-AverageVelocity2.csv')
