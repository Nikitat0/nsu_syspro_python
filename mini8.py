from functools import wraps


def deprecated(f=None, since=None, will_be_removed=None):
    if f is None:
        return lambda f: deprecated(f, since, will_be_removed)

    if since is None or will_be_removed is None:
        return f

    @wraps(f)
    def wrapped(*args, **kwargs):
        print(
            f"Warning: function {f.__name__} is deprecated since version {since}. It will be removed {will_be_removed}")
        return f(*args, **kwargs)
    return wrapped


@deprecated
def sum(a, b):
    return a + b


@deprecated(since="0.1", will_be_removed="1.1")
def mul(a, b):
    return a * b


print(sum(1, 2))
print(mul(3, 4))
