import sys
read = sys.stdin.readline

n, m = map(int, read().split())
ice = []
for i in range(n):
    ice.append(list(map(int, read().rstrip())))

def check_ice(row, col):
    if row < 0 or row >= n or col < 0 or col >= m:
        return False
    if not ice[row][col]:
        ice[row][col] = 99
        check_ice(row, col+1)
        check_ice(row, col-1)
        check_ice(row+1, col)
        check_ice(row-1, col)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if check_ice(i, j):
            result += 1

print(result)