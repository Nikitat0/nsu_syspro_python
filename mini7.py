def flatten(src, depth=None):
    if depth == 0:
        return src
    return sum([
        flatten(elem, depth and depth - 1) if isinstance(elem, list) else [elem] for elem in src],
        [],
    )


print(flatten([1, 2, [4, 5], [6, [7]], 8]))
print(flatten([1, 2, [4, 5], [6, [7]], 8], depth=1))
