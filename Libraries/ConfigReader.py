import json

class ConfigReader:
    def __init__(self, url):
        self.url = url

    def read_config(self):
        # Read Config File
        with open(self.url) as json_data_file:
            data = json.load(json_data_file)
        
        return data