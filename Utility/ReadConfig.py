import json
from pathlib import Path
from os import path


class Configurations:
    def __init__(self):
        curdir = path.abspath(__file__)
        rootdir = Path(curdir).parent.parent
        self.configPath = path.join(rootdir, 'Configurations','Config.json')
        self.configData={}
        with open(self.configPath, 'r') as config:
            self.configData = json.load(config)


    def getURL(self):
        return self.configData['AppURL']

    def getUsername(self):
        return self.configData['AppUsr']

    def getPassword(self):
        return self.configData['AppPwd']

