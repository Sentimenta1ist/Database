from configparser import ConfigParser

class Config:
    def __init__(self, config_file):
        parser = ConfigParser()
        parser.read(config_file)
        db = {}
        section = 'postgresql'
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                if param[0] == 'host':
                    self.host = param[1]
                elif param[0] == 'port':
                    self.port = param[1]
                elif param[0] == 'database':
                    self.database = param[1]
                elif param[0] == 'user':
                    self.user = param[1]
                elif param[0] == 'password':
                    self.password = param[1]
                else:
                    raise Exception('Wrong key {0} in section {1}'.format(param[0], section))
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, config_file))

    def to_dict(self):
        return {
            'host': self.host,
            'port': self.port,
            'database': self.database,
            'user': self.user,
            'password': self.password
         }

    def __str__(self):
        return "[Config: {}, {}, {}, {}, {}]".format(self.host, self.port, self.database, self.user, self.password)

