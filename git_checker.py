#!/usr/bin/env python3
import os
from core import parser
from core import scanner


class MainProgram(object):
    """A simple base class to be used for initializing stuff
    """

    def __init__(self):
        self.args_obj = parser.ArgumentParser()
        self.base_path = os.path.dirname(os.path.realpath(__file__))
        self.result = scanner.Scan(self.args_obj, self.base_path)


if __name__ == "__main__":
    main = MainProgram()
