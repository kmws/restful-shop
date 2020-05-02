import logging


class LoggerTag:
    def __init__(self, tag):
        self.tag = tag
        self.logger = logging.getLogger('tag')

    def info(self, message):
        self.logger.info(message, extra={'tag': self.tag})

    def debug(self, message):
        self.logger.debug(message, extra={'tag': self.tag})

    def warning(self, message):
        self.logger.warning(message, extra={'tag': self.tag})

    def error(self, message):
        self.logger.error(message, extra={'tag': self.tag})