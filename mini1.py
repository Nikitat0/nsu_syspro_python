n = int(input())

c = 0
if n < 0:
    c += 1
    mask = 0
    while mask & (~n + 1) != ~n + 1:
        mask = (mask << 1) + 1
    n = n & mask

while n != 0:
    c += n & 1
    n >>= 1
print(c)
