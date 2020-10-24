import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

def df_to_numpy(df):
    """
    pandas dataframe -> numpy array (x and any y values)
    """
    row, col = df.shape
    x = df.iloc[:,1].values
    y_values = df.iloc[:,2:col].values
    return x, y_values

if __name__ == '__main__':
    csv_file_path = 'example/example.csv'
    x_axis_name = 'x'
    y_axis_name = 'y'

    if len(sys.argv) == 2:
        csv_file_path = sys.argv[1]
    elif len(sys.argv) == 4:
        csv_file_path = sys.argv[1]
        x_axis_name = sys.argv[2]
        y_axis_name = sys.argv[3]

    df = pd.read_csv(csv_file_path)

    column_name = df.columns[2:].values
    x, y_values = df_to_numpy(df)
    y_values_trans = y_values.T

    with plt.style.context(['science', 'ieee', 'no-latex']):
        fig, ax = plt.subplots(facecolor="w")
        for i in range(len(y_values_trans)):
            line, = ax.plot(x, y_values_trans[i])
            line.set_label(column_name[i])
        ax.set_xlabel(x_axis_name)
        ax.set_ylabel(y_axis_name)
        ax.legend()
        fig.savefig("output/img.png")
