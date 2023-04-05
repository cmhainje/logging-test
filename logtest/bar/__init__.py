from .baz import Baz

import logging

from sys import stdout

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.info('initializing bar!')

baz = Baz()