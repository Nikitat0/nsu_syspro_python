import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from benchmark import Benchmark

SIZE = int(input("Enter size (512): ") or 512)
STEPS = int(input("Enter steps (128): ") or 128)
VISUALIZE = input("Type something to run in visual mode: ") and True or False

common_field = np.random.choice(a=[False, True], size=(SIZE, SIZE))


bench = Benchmark()
with bench("Python"):
    field1 = common_field.tolist()
    field2 = [[None] * SIZE for _ in range(SIZE)]
    if VISUALIZE:
        _, ax = plt.subplots()
        plt.ion()
    for _ in range(STEPS):
        for x in range(SIZE):
            for y in range(SIZE):
                c = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if (dx, dy) == (0, 0):
                            continue
                        c += field1[(x + dx) % SIZE][(y + dy) % SIZE]
                if field1[x][y]:
                    field2[x][y] = c in range(2, 3)
                else:
                    field2[x][y] = c == 3
        field1, field2 = field2, field1
        if VISUALIZE:
            ax.clear()
            ax.matshow(field1, cmap=ListedColormap(["w", "k"]))
            plt.pause(0.5)
    if VISUALIZE:
        plt.close()

if VISUALIZE:
    exit()

with bench("NumPy (double index)"):
    field1, field2 = common_field, np.empty((SIZE, SIZE), np.bool_)
    for _ in range(STEPS):
        for x in range(SIZE):
            for y in range(SIZE):
                c = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if (dx, dy) == (0, 0):
                            continue
                        c += field1[(x + dx) % SIZE][(y + dy) % SIZE]
                if field1[x][y]:
                    field2[x][y] = c in range(2, 3)
                else:
                    field2[x][y] = c == 3
        field1, field2 = field2, field1


with bench("NumPy (tuple index)"):
    field1, field2 = common_field, np.empty((SIZE, SIZE), np.bool_)
    for _ in range(STEPS):
        for x in range(SIZE):
            for y in range(SIZE):
                c = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if (dx, dy) == (0, 0):
                            continue
                        c += field1[(x + dx) % SIZE, (y + dy) % SIZE]
                if field1[x, y]:
                    field2[x, y] = c in range(2, 3)
                else:
                    field2[x, y] = c == 3
        field1, field2 = field2, field1

print(bench)
