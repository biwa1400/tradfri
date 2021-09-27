import json

def readConfigFile(file):
    with open(file, 'r') as load_f:
        return json.load(load_f)