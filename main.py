import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

def df_to_numpy(df):
    """
    pandas dataframe -> numpy array (x and any y values)
    """
    _row, col = df.shape
    x = df.iloc[:,0].values
    y_values = df.iloc[:,1:col].values
    return x, y_values

if __name__ == '__main__':
    # default value
    csv_file_path = 'example/example.csv'
    x_axis_name = 'x'
    y_axis_name = 'y'
    output_file_name = 'img.png'

    if len(sys.argv) == 2:
        # csv file name
        csv_file_path = sys.argv[1]
    elif len(sys.argv) == 3:
        # csv file name and output file name
        csv_file_path = sys.argv[1]
        output_file_name = sys.argv[2]
    elif len(sys.argv) == 4:
        # axis name value
        csv_file_path = sys.argv[1]
        x_axis_name = sys.argv[2]
        y_axis_name = sys.argv[3]
    elif len(sys.argv) == 5:
        csv_file_path = sys.argv[1]
        x_axis_name = sys.argv[2]
        y_axis_name = sys.argv[3]
        output_file_name = sys.argv[4]

    df = pd.read_csv(csv_file_path)

    column_name = df.columns[1:].values
    x, y_values = df_to_numpy(df)
    y_values_trans = y_values.T

    with plt.style.context(['science', 'no-latex']):
        fig, ax = plt.subplots(facecolor="w")
        for i in range(len(y_values_trans)):
            line, = ax.plot(x, y_values_trans[i])
            line.set_label(column_name[i])
        ax.set_xlabel(x_axis_name)
        ax.set_ylabel(y_axis_name)
        ax.legend()
        fig.savefig("output/"+output_file_name, dpi=300)
