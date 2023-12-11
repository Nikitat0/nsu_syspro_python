from operator import itemgetter
from time import time


def transpose(matrix):
    return list(zip(*matrix))


def format_column(column):
    column = list(map(str, column))
    max_len = max(map(len, column))
    column = list(map(
        lambda col: f"| {col:<{max_len}} ",
        column,
    ))
    column.insert(1, '|' + '-' * (max_len + 2))
    return column


def str_join(iterable):
    return "".join(iterable)


class Benchmark:
    def __init__(self):
        self._results = dict()

    def __getitem__(self, k):
        return self._results.get(k, 0.0)

    def __setitem__(self, k, v):
        self._results[k] = v

    def __call__(self, name):
        class BenchmarkCtx:
            def __init__(self, parent, name):
                self._parent = parent
                self._name = name

            def __enter__(self):
                self._time = time()

            def __exit__(self, *_):
                self._parent[self._name] += time() - self._time

        return BenchmarkCtx(self, name)

    def __str__(self):
        headers = ["Bench", "Result"]
        rows = list(
            sorted(map(tuple, self._results.items()), key=itemgetter(1)))
        columns = list(map(format_column, transpose([headers] + rows)))
        return str_join([str_join(row) + "|\n" for row in transpose(columns)])
