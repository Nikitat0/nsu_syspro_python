from functools import wraps


def coroutine(gen):
    @wraps(gen)
    def patched_gen():
        itr = gen()
        next(itr)
        return itr

    return patched_gen


@coroutine
def storage():
    values = set()
    was_there = False

    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)


st = storage()
assert st.send(42) == False
assert st.send(42) == True
assert st.send(42) == True
