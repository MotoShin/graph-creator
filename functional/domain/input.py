from functional.values.mode import ApplicationMode
from functional.domain.service.csv2numpy import CsvToNumpy


class InteractiveInput(object):
    def __init__(self,
                mode,
                csv_file_path,
                x_axis_name,
                y_axis_name,
                output_img_name,
                moving_average_term):
        self.mode = mode
        self.csv_file_path = csv_file_path
        self.x_axis_name = x_axis_name
        self.y_axis_name = y_axis_name
        self.output_img_name = output_img_name
        self.moving_average_term = moving_average_term

    def get_mode(self):
        return self.mode

    def get_csv_file_path(self):
        return self.csv_file_path

    def get_x_axis_name(self):
        return self.x_axis_name

    def get_y_axis_name(self):
        return self.y_axis_name

    def get_output_img_name(self):
        return self.output_img_name

    def get_moving_average_term(self):
        return self.moving_average_term

    def get(self):
        csv2numpy = CsvToNumpy(self.csv_file_path)
        if self.mode == ApplicationMode.MOVING_AVERAGE:
            column_name, x, y_values = csv2numpy.read_csv_with_moving_average(self.moving_average_term)
        else:
            column_name, x, y_values = csv2numpy.read_csv()
        
        return self.x_axis_name, self.y_axis_name, self.output_img_name, column_name, x, y_values
