import logging

logger = logging.getLogger(__name__)

class Baz:
    def __init__(self):
        self.logger = logger
        self.logger.info('Baz instantiated!')

    def do(self):
        self.logger.info('Baz doing something!')
