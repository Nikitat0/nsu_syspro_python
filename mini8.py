from functools import wraps


def deprecated(f=None, since=None, will_be_removed=None):
    if f is None:
        return lambda f: deprecated(f, since, will_be_removed)

    template = "Warning: function {} is deprecated{}. It will be removed in {}."
    msg = template.format(
        f.__name__,
        "" if since is None else f" since version {since}",
        "future versions" if will_be_removed is None
        else f"version {will_be_removed}",
    )

    @wraps(f)
    def wrapped(*args, **kwargs):
        print(msg)
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
