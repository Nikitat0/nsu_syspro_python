def cycle(iterable):
    while True:
        yield from iterable


def chain(*iterables):
    for iterable in iterables:
        yield from iterable


def take(iterable, count=-1):
    if count == -1:
        yield from iterable
    for _, e in zip(range(count), iterable):
        yield e


print(*take(cycle([1, 2, 3]), 10))
print(*chain([1, 2, 3], "hello", "there"))
