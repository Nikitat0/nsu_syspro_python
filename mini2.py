def zip(a, b):
    l = min(len(a), len(b))
    return [(a[i], b[i]) for i in range(l)]


a, b = [list(map(int, input().split())) for _ in range(2)]
print(*zip(a, b))
