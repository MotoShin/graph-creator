import matplotlib.pyplot as plt
import numpy as np
import sys

from functional.csv2numpy import CsvToNumpy
from functional.numpy2img import NumpyToImg
from functional.interactive import Interactive

class Application:
    @staticmethod
    def run():
        # interactive console
        interactive = Interactive()
        csv_file_path, x_axis_name, y_axis_name, output_file_name = interactive.run()

        # csv to numpy data
        csv2numpy = CsvToNumpy(csv_file_path)
        column_name, x, y_values = csv2numpy.read_csv()

        # numpy data to image
        numpy2img = NumpyToImg(x_axis_name, y_axis_name, output_file_name, column_name, x, y_values)
        numpy2img.create_img()

if __name__ == '__main__':
    Application.run()
