def reverse_dict(src):
    dst = dict()
    repeated = set()
    for k, v in src.items():
        if v in dst:
            dst[v] = (dst[v], )
            repeated.add(v)
        if v in repeated:
            dst[v] += (k, )
        else:
            dst[v] = k
    return dst


print(reverse_dict({1: "a", (3, 2): "b", (4, 5): "b"}))
try:
    print(reverse_dict({"a": [], "b": 2, "c": 2}))
except TypeError:
    print("TypeError exception catched")
