from functools import wraps


def singleton(_class):
    _class.__instance__ = None

    @wraps(_class)
    def f(*args):
        if _class.__instance__ is None:
            _class.__instance__ = _class(*args)
        return _class.__instance__

    return f


@singleton
class Counter():
    def __init__(self, value=2):
        self.value = value

    def inc(self):
        self.value += 1

    def get(self):
        return self.value

print(Counter.__init__)
Counter(2).inc()
Counter(2).inc()
assert Counter().get() == 4
