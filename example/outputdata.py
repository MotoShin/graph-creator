import pandas as pd
import math
import numpy as np

cols = ['x', 'sin(x)', 'cos(x)']
lst = []

for x in np.arange(0, 10.01, 0.01):
    lst.append([x, math.sin(x), math.cos(x)])

df = pd.DataFrame(lst, columns=cols)

print(df)

df.to_csv('example.csv', index=False)
