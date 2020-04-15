import json


class ConfigFile:
    def __init__(self, config_name: str, data):
        self.config_name = config_name
        self.data = data

    def get_value(self, key: str):
        return self.data[key]

    def set_value(self, key: str, value):
        self.data[key] = value
        json.dump(self.data, self.config_name)


def get_config(config_name: str) -> ConfigFile:
    with open(config_name, 'r') as config:
        data = json.load(config)

    return ConfigFile(config_name, data)
