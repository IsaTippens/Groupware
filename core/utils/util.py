from io import TextIOWrapper
import json


def load_json(fileObj: TextIOWrapper):
    return json.load(fileObj)