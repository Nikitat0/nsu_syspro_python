import numpy as np
from benchmark import Benchmark

SIZE = 256

indexes = np.random.randint(0, SIZE - 1, size=(10 ** 6, 3)).tolist()

np_array = np.random.randint(0, 42, size=(SIZE, SIZE, SIZE))
py_array = np_array.tolist()

bench = Benchmark()
with bench("Numpy random access (index thrice)"):
    for x, y, z in indexes:
        c = np_array[x][y][z]
with bench("Numpy random access (index twice)"):
    for x, y, z in indexes:
        c = np_array[x, y][z]
with bench("Numpy random access (index once)"):
    for x, y, z in indexes:
        c = np_array[x, y, z]
with bench("Python random access"):
    for x, y, z in indexes:
        c = py_array[x][y][z]
print(bench)
