import matplotlib.pyplot as plt
import numpy as np
import sys

from functional.numpy2img import NumpyToImg
from functional.interactive import Interactive


class Application:
    @staticmethod
    def run():
        # interactive console
        interactive = Interactive()
        interactive_input = interactive.run()

        # numpy data to image
        numpy2img = NumpyToImg(interactive_input)
        numpy2img.create_img()

if __name__ == '__main__':
    Application.run()
