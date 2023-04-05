# logtest

How do you configure `logging` _once_ in such a way that module-level loggers will inherit this configuration?

Our desired configuration is set in `setup.py`: output goes to stdout, no formatting (just the messages!). Our goal is to then have all logging messages from throughout the package get printed with this configuration.

The successful result is given by `foo.py`.

```bash
$ poetry run python -m logtest.foo 
initializing bar!
Baz instantiated!
hello from foo!
Baz instantiated!
Baz doing something!
```

The fail result happens with `fail.py`.

```bash
$ poetry run python -m logtest.fail 
hello from foo!
```

This script fails to log any of the messages from the `bar` submodule, even when its child classes are imported and used outside of the submodule. The reason is that the loggers in the `bar` submodule are instantiated before we set our logging configuration. Further, the logging configuration explicitly disables existing loggers, so even if the `bar` submodule has its own logger with its own configuration, its messages will be suppressed.

The solution is to set the desired configuration on the root logger, the logger with name `""` in the config dict, _before_ any other logging operations happen. Then, the `logging.basicConfig` in `bar/__init__.py` will no longer have an effect, and all loggers will inherit the correct configuration from the root logger.
