import pandas as pd
import math
import numpy as np

cols = ['x', 'sin(x)', 'cos(x)']
lst = []

for x in np.arange(0, 10.01, 0.01):
    lst.append([x, math.sin(x), math.cos(x)])

df = pd.DataFrame(lst, columns=cols)

df.to_csv('example2.csv', index=False)

def model(x, p):
    return x ** (2 * p + 1) / (1 + x ** (2 * p))

cols = ['x', '10', '15', '20', '30', '50', '100']
lst = []

for x in np.linspace(0.75, 1.25, 201):
    lst.append([x, model(x, 10), model(x, 15), model(x, 20), model(x, 30), model(x, 50), model(x, 100)])

df = pd.DataFrame(lst, columns=cols)
df.to_csv('example.csv', index=False)
