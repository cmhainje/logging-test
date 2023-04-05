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

The fail results are given in `fail.py`, `fail2.py`.

```bash
$ poetry run python -m logtest.fail 
WARNING:__main__:hello from foo!
INFO:logtest.bar.baz:Baz instantiated!
INFO:logtest.bar.baz:Baz doing something!

$ poetry run python -m logtest.fail2
hello from foo!
Baz instantiated!
Baz doing something!
```

Both of these fail because the log messages from initializing the `bar` submodule are not printed. The first one fails additionally because the correct formatting is not applied to the messages; the setup code isn't even read!

We could go into `bar/__init__.py` and change the local configuration there to `logging.DEBUG`; if we do this, the result for `fail2` becomes

```bash
$ poetry run python -m logtest.fail2
INFO:logtest.bar:initializing bar!
INFO:logtest.bar.baz:Baz instantiated!
WARNING:__main__:hello from foo!
hello from foo!
INFO:logtest.bar.baz:Baz instantiated!
Baz instantiated!
INFO:logtest.bar.baz:Baz doing something!
Baz doing something!
```

which is also definitely not right! Now the `bar` submodule's logs are visible, but they aren't formatted according to the global configuration. Further, the `Baz` class's logs are getting duplicated, once in stderr with the `bar` submodule's logger, and once in stdout with the correct configuration.

The solution is to set the desired configuration on the root logger, obtained from `logging.getLogger()` (with no argument), _before_ any other logging operations happen. Then, the `logging.basicConfig` in `bar/__init__.py` will no longer have an effect, and all loggers will inherit the correct configuration from the root logger.
