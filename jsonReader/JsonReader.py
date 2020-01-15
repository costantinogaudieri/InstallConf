import json

def readRelease(path):

    with open(path) as json_file:
        data = json.load(json_file)
        release, snapshot = str.split(data['version'], "-")
        return release

