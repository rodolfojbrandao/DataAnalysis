import os
import numpy as np
import pandas as pd

NF = 601 #number of files

colCounter = np.zeros((NF,1))

path='/home/lablinux/Desktop/post_paraviewPP'
os.chdir(path)

for j in range (0,NF):
    force = pd.read_csv('force.{}.csv'.format(j))
    len = force.shape[0]
    colCounter[j] = len

print(colCounter)
#sum = np.sum(colCounter)
colCounter = pd.DataFrame(colCounter)
colCounter.to_csv('1-Number_of_Collisions_PP.csv')