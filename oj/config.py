import os
import json

__author__ = "imdreamrunner"
__email__ = "imdreamrunner@gmail.com"

CONFIG = json.load(open(os.path.abspath(os.path.realpath(__file__) + "/../../config.json")))
