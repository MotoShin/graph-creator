import matplotlib.pyplot as plt
import numpy as np
import sys

from functional.csv2numpy import CsvToNumpy
from functional.numpy2img import NumpyToImg

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
        numpy2img = NumpyToImg(self.x_axis_name, self.y_axis_name, self.output_file_name, column_name, x, y_values)
        numpy2img.create_img()

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
