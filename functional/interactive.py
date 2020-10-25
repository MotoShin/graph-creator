import configparser

from enum import Enum

class Interactive:
    def __init__(self):
        self.inifile = configparser.ConfigParser()
        self.inifile.read('functional/config/config.ini')
        self.interactive_status = InteractiveStatus.CHOOSE_MODE
    
    def run(self):
        while self.interactive_status != InteractiveStatus.FINISHED:
            if self.interactive_status == InteractiveStatus.CHOOSE_MODE:
                _mode = input(self.inifile.get('INTERACTIVE', 'mode') + ' ') or '1'
                self.interactive_status = InteractiveStatus.INPUT_CSV_FILE_PATH
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

        return csv_file_path, x_axis_name, y_axis_name, output_img_name

class InteractiveStatus(Enum):
    CHOOSE_MODE = 1
    INPUT_CSV_FILE_PATH = 2
    INPUT_X_AXIS_NAME = 3
    INPUT_Y_AXIS_NAME = 4
    INPUT_OUTPUT_IMG_NAME = 5
    FINISHED = 6
