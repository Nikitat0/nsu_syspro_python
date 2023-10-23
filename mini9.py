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


def format_table(benchs, algos, results):
    headers = ["Benchmark"] + algos
    rows = [[bench] + result for bench, result in zip(benchs, results)]
    columns = list(map(format_column, transpose([headers] + rows)))
    return str_join([str_join(row) + "|\n" for row in transpose(columns)])


if __name__ == "__main__":
    print(format_table(
        ["best case", "worst_case"],
        ["quick sort", "merge_sort", "bubble_sort"],
        [
            [1.23, 1.56, 2.0],
            [3.3, 2.9, 3.9],
        ],
    ))
