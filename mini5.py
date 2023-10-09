def specialize(f, *applied_args, **applied_kwargs):
    return lambda *args, **kwargs: f(*applied_args, *args, **kwargs, **applied_kwargs)


def sum(x, y):
    return x + y


plus_one = specialize(sum, y=1)
print(plus_one(10))

just_two = specialize(sum, 1, 1)
print(just_two())
