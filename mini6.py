def flatten(src):
    return sum([flatten(elem) if isinstance(elem, list) else [elem] for elem in src], [])


print(flatten([1, 2, [4, 5], [6, [7]], 8]))
