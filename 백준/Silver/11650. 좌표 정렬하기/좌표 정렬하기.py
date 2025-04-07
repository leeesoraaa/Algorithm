import sys
input = sys.stdin.readline
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
grid.sort(key = lambda x : (x[0], x[1]))
for xy in grid:
    print(f'{xy[0]} {xy[1]}')