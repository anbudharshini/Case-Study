import configparser

class PropertyUtil:
    @staticmethod
    def getPropertyString(filepath):
        config = configparser.ConfigParser()
        config.read(filepath)
        print("Sections found:", config.sections())
        db = config['DB']
        return {'host':db['host'],
                'port':int(db['port']),
                'database':db['dbname'],
                'user':db['username'],
                'password':db['password']}
