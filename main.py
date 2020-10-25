import matplotlib.pyplot as plt
import numpy as np
import sys

from functional.csv2numpy import CsvToNumpy

class Application:
    def __init__(
        self,
        csv_file_path='example/example.csv',
        x_axis_name='x',
        y_axis_name='y',
        output_file_name='img.png'):
        self.csv2numpy = CsvToNumpy(csv_file_path)
        self.x_axis_name = x_axis_name
        self.y_axis_name = y_axis_name
        self.output_file_name = output_file_name
    
    def run(self):
        column_name, x, y_values = self.csv2numpy.read_csv()
        y_values_trans = y_values.T
        with plt.style.context(['science', 'no-latex']):
            fig, ax = plt.subplots(facecolor="w")
            for i in range(len(y_values_trans)):
                line, = ax.plot(x, y_values_trans[i])
                line.set_label(column_name[i])
            ax.set_xlabel(self.x_axis_name)
            ax.set_ylabel(self.y_axis_name)
            ax.legend()
            fig.savefig("output/"+self.output_file_name, dpi=300)

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

    app = Application(
        csv_file_path=csv_file_path,
        x_axis_name=x_axis_name,
        y_axis_name=y_axis_name,
        output_file_name=output_file_name)
    
    app.run()
