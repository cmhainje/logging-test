def setup_logging_config():
    import logging.config

    logging.config.dictConfig({
        "version": 1,
        "disableExistingLoggers": True,
        "formatters": { 
            "standard": { 
                "format": "%(message)s"
            },
        },
        "handlers": {
            "default": {
                "level": "INFO",
                "formatter": "standard",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
        },
        "loggers": {
            "": {  # root logger
                "handlers": ["default"],
                "level": "DEBUG",
            }
        }
    })
