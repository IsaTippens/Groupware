from io import TextIOWrapper
import json


def load_json(fileObj: TextIOWrapper):
    return json.load(fileObj)

def save_json(fileName: str, data: dict):
    with open(fileName, 'w') as f:
        json.dump(data, f)
    