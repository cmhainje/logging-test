def setup_logging_config():
    import logging
    import sys

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(logging.StreamHandler(sys.stdout))
