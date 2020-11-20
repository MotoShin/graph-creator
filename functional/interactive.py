import configparser

from enum import Enum
from functional.domain.input import InteractiveInput
from functional.values.mode import ApplicationMode


class Interactive:
    def __init__(self):
        self.inifile = configparser.ConfigParser()
        self.inifile.read('functional/config/config.ini')
        self.interactive_status = InteractiveStatus.CHOOSE_MODE
    
    def run(self):
        moving_average_term = 10
        while self.interactive_status != InteractiveStatus.FINISHED:
            if self.interactive_status == InteractiveStatus.CHOOSE_MODE:
                mode = input(self.inifile.get('INTERACTIVE', 'mode') + ' ') or '1'
                if int(mode) == ApplicationMode.MOVING_AVERAGE:
                    self.interactive_status = InteractiveStatus.INPUT_MOVING_AVERAGE_TERM
                    mode = ApplicationMode.MOVING_AVERAGE
                else:
                    self.interactive_status = InteractiveStatus.INPUT_CSV_FILE_PATH
                    mode = ApplicationMode.DEFAULT
                continue
            elif self.interactive_status == InteractiveStatus.INPUT_CSV_FILE_PATH:
                csv_file_path = input(self.inifile.get('INTERACTIVE', 'csv_file_path') + ' ') or 'example/example.csv'
                self.interactive_status = InteractiveStatus.INPUT_X_AXIS_NAME
                continue
            elif self.interactive_status == InteractiveStatus.INPUT_X_AXIS_NAME:
                x_axis_name = input(self.inifile.get('INTERACTIVE', 'x_axis_name') + ' ') or 'x'
                self.interactive_status = InteractiveStatus.INPUT_Y_AXIS_NAME
                continue
            elif self.interactive_status == InteractiveStatus.INPUT_Y_AXIS_NAME:
                y_axis_name = input(self.inifile.get('INTERACTIVE', 'y_axis_name') + ' ') or 'y'
                self.interactive_status = InteractiveStatus.INPUT_OUTPUT_IMG_NAME
                continue
            elif self.interactive_status == InteractiveStatus.INPUT_OUTPUT_IMG_NAME:
                output_img_name = input(self.inifile.get('INTERACTIVE', 'output_img_name') + ' ') or 'img.png'
                self.interactive_status = InteractiveStatus.FINISHED
                continue
            elif self.interactive_status == InteractiveStatus.INPUT_MOVING_AVERAGE_TERM:
                moving_average_term = input(self.inifile.get('INTERACTIVE', 'moving_average_term') + ' ') or '10'
                moving_average_term = int(moving_average_term)
                self.interactive_status = InteractiveStatus.INPUT_CSV_FILE_PATH

        return InteractiveInput(mode, csv_file_path, x_axis_name, y_axis_name, output_img_name, moving_average_term)

class InteractiveStatus(Enum):
    CHOOSE_MODE = 1
    INPUT_CSV_FILE_PATH = 2
    INPUT_X_AXIS_NAME = 3
    INPUT_Y_AXIS_NAME = 4
    INPUT_OUTPUT_IMG_NAME = 5
    INPUT_MOVING_AVERAGE_TERM = 6
    FINISHED = 0
