import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def df_to_numpy(df):
    """
    pandas dataframe -> numpy array (x and any y values)
    """
    row, col = df.shape
    x = df.iloc[:,1].values
    y_values = df.iloc[:,2:col].values
    return x, y_values

if __name__ == '__main__':
    df = pd.read_csv('example-data/example.csv')

    column_name = df.columns[2:].values
    x, y_values = df_to_numpy(df)
    y_values_trans = y_values.T

    with plt.style.context(['science', 'ieee', 'no-latex']):
        fig, ax = plt.subplots(facecolor="w")
        for i in range(len(y_values_trans)):
            line, = ax.plot(x, y_values_trans[i])
            line.set_label(column_name[i])
        ax.legend()
        fig.savefig("output/img.png")
