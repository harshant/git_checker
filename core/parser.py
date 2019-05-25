import argparse
import sys


class ArgumentParser(object):
    def __init__(self):
        if len(sys.argv) < 2:
            print("For Usage info : python3 git_extractor.py -h")
            exit()
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument(
            "-i",
            "--input",
            help="Input a relative file path containing list of domain names",
            action="store",
        )
        self.args = self.parser.parse_args()
