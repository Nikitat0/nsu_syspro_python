import numpy as np
from random import randint, sample, shuffle
from string import ascii_lowercase
from benchmark import Benchmark

trash = []
trash += np.random.rand(100).tolist()
trash += np.random.randint(0, 2, 100).tolist()
for _ in range(100):
    trash.append(''.join(sample(ascii_lowercase, randint(0, 10))))
trash += [True, False] * 10
shuffle(trash)

np_array = np.empty((len(trash), len(trash), len(trash)), np.bool_)

bench = Benchmark()
with bench("NumPy with typecast"):
    for i in range(len(trash)):
        for j in range(len(trash)):
            for k in range(len(trash)):
                np_array[i, j, k] = trash[i]

trash = list(map(bool, trash))
with bench("NumPy without cast"):
    for i in range(len(trash)):
        for j in range(len(trash)):
            for k in range(len(trash)):
                np_array[i, j, k] = trash[i]

trash = list(map(bool, trash))
np_array = np.empty((len(trash), len(trash), len(trash)), np.int64)
with bench("NumPy fallback"):
    for i in range(len(trash)):
        for j in range(len(trash)):
            for k in range(len(trash)):
                np_array[i, j, k] = trash[i]
print(bench)
