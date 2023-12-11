import numpy as np
from benchmark import Benchmark

SIZE = 1000

indexes = np.random.randint(0, SIZE - 1, size=(10 ** 6, 2)).tolist()

np_array = np.random.randint(0, 42, size=(SIZE, SIZE))
py_array = np_array.tolist()

bench = Benchmark()
with bench("Numpy random access (double indexing)"):
    for x, y in indexes:
        c = np_array[x][y]
with bench("Numpy random access (tuple indexing)"):
    for x, y in indexes:
        c = np_array[x, y]
with bench("Python random access"):
    for x, y in indexes:
        c = py_array[x][y]
print(bench)
