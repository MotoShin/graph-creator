import numpy as np
import matplotlib.pyplot as plt

class NumpyToImg:
    def __init__(self, x_axis_name, y_axis_name, output_file_name, column_name, x, y_values):
        """
        constructor
        """
        self.x_axis_name = x_axis_name
        self.y_axis_name = y_axis_name
        self.output_file_name = output_file_name
        self.column_name = column_name
        self.x = x
        self.y_values = y_values

    def create_img(self):
        """
        create image
        """
        y_values_trans = self.y_values.T
        with plt.style.context(['science', 'no-latex']):
            fig, ax = plt.subplots(facecolor="w")
            for i in range(len(y_values_trans)):
                line, = ax.plot(self.x, y_values_trans[i])
                line.set_label(self.column_name[i])
            ax.set_xlabel(self.x_axis_name)
            ax.set_ylabel(self.y_axis_name)
            ax.legend()
            fig.savefig("output/"+self.output_file_name, dpi=300)
