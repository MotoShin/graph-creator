import numpy as np
import pandas as pd

class CsvToNumpy:
    def __init__(self, csv_file_path):
        """
        constructor
        """
        self.df = pd.read_csv(csv_file_path)

    def read_csv(self):
        """
        read csv
        return column name list, x value list and y values list
        """
        column_name = self.df.columns[1:].values
        _row, col = self.df.shape
        x = self.df.iloc[:,0].values
        y_values = self.df.iloc[:,1:col].values

        return column_name, x, y_values
