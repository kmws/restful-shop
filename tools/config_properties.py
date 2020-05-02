import configparser
from os.path import exists, dirname, realpath

config_properties = None


def get_config():
    return config_properties


def init_config(config_file=None):
    global config_properties

    if config_file is None:
        config_file = 'config.properties'

    config_properties = ConfigProperties(config_file)


class Config(object):
    SUPPORTED_LANGUAGES = {'en': 'English'}
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = False


class ProductionConfig(Config):
    DEBUG = False


class ConfigProperties:
    def __init__(self, config_file):
        self.config = configparser.RawConfigParser()
        path = dirname(dirname(realpath(__file__))) + '/' + config_file
        if not exists(path):
            raise AttributeError('Path not exists!')
        self.config.read(path)

    def get_flask_config(self):
        return self.config.get('FlaskSection', 'flask_config')

    def get_secret_key(self):
        return self.config.get('FlaskSection', 'secret_key')

    def get_db_config(self):
        return self.config.get('DatabaseSection', 'db_config')

    def get_db_type(self):
        return self.config.get('DatabaseSection', 'db_type')

    def get_language(self):
        return self.config.get('AppSection', 'language')

    def is_production(self):
        return self.get_flask_config() == 'production'


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
