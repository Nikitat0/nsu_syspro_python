matrix = list(
    map(lambda row: list(map(int, row.split())), input().split('|'))
)
print(*matrix, sep='\n')
