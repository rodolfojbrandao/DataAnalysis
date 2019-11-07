import numpy as np
import pandas as pd
import cupy
import cudf

N=100000000
x=np.random.rand(N)
y=np.random.rand(N)

z=x+y
print(z)
print(N)