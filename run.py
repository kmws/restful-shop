import logging

from app import init_app, create_root
from tools.config_properties import init_config, get_config
from tools.logger_tag import LoggerTag


def create_logger():
    logger = logging.getLogger('tag')
    logger.level = logging.DEBUG
    handler = logging.StreamHandler()
    handler.setLevel(logger.level)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(tag)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)


if __name__ == '__main__':

    create_logger()
    LoggerTag('app').info('Run application')

    init_config()
    application = init_app()
    config = get_config()
    create_root(config.get_root_email(), config.get_root_password())
    application.run(host='0.0.0.0', port=8000)
