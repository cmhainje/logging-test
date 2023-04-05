from .setup import setup_logging_config
setup_logging_config()

from logtest.bar import Baz

import logging
from sys import stdout

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.warning('hello from foo!')

baz = Baz()
baz.do()
