from logtest.bar import Baz

from .setup import setup_logging_config
setup_logging_config()

import logging
from sys import stdout

logger = logging.getLogger(__name__)
logger.warning('hello from foo!')

baz = Baz()
baz.do()
