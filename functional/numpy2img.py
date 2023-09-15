import matplotlib.pyplot as plt
import scienceplots

from functional.domain.input import InteractiveInput


class NumpyToImg:
    def __init__(self, data: InteractiveInput):
        """
        constructor
        """
        self.x_axis_name, self.y_axis_name, self.output_file_name, self.column_name, self.x, self.y_values = data.get()

    def create_img(self):
        """
        create image
        """
        y_values_trans = self.y_values.T
        with plt.style.context(['science']):
            fig, ax = plt.subplots(facecolor="w")
            for i in range(len(y_values_trans)):
                line, = ax.plot(self.x, y_values_trans[i])
                line.set_label(self.column_name[i])
            ax.set_xlabel(self.x_axis_name)
            ax.set_ylabel(self.y_axis_name)
            ax.legend()
            fig.savefig("output/"+self.output_file_name, dpi=300)
