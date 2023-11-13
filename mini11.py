from functools import wraps


def singleton(_class):
    constructor = _class.__new__
    initializer = _class.__init__

    @wraps(initializer)
    def no_init(*args):
        pass

    @wraps(constructor)
    def singleton_constructor(*args):
        if _class.__instance__ is None:
            _class.__instance__ = constructor(*args)
            initializer(_class.__instance__)
            _class.__init__ = no_init
        return _class.__instance__

    _class.__instance__ = None
    _class.__new__ = singleton_constructor
    return _class


@singleton
class Counter():
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1

    def get(self):
        return self.value


Counter().inc()
Counter().inc()
assert Counter().get() == 2
