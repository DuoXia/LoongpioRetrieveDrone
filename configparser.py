from configparser import ConfigParser


class HandleConfig:
    def __init__(self, filename):
        self.filename = filename
        self.config = ConfigParser()
        self.config.read(self.filename, encoding="utf-8")

    def save_data(self, group, key, data):

        if not self.config.has_section(group):
            self.config.add_section(group)
        self.config.set(group, key, str(data))
        with open(self.filename, "w") as file:
            self.config.write(file)

    def get_data(self, group, key):
        data = self.get_value(group, key)
        data = str(data)[1:-1].split(',')
        data = list(map(int, data))
        return data

    def get_value(self, section, option):
        return self.config.get(section, option)
