import statsmodels.api as sm
from pandas import DataFrame
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import math

path='/home/rodolfo/GitHub/Data/Segregacao'
os.chdir(path)

Dados = pd.read_csv('k.csv')
print(Dados)
X1=Dados['x1']
X2=Dados['x2']
X = [[X1,X2]]
Y = Dados['k']

print(len(X1))
print(len(X2))
print(len(Y))

plt.scatter(X1, Y)
plt.scatter(X2, Y)
plt.show()

X = sm.add_constant(X) # adding a constant

model = sm.OLS(Y, X).fit()
predictions = model.predict(X)

print_model = model.summary()
print(print_model)

#print(Dados)