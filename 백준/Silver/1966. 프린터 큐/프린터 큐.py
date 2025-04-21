import sys
from collections import deque
input = sys.stdin.readline

def printer(queue, m):
    count = 0
    while True:
        if queue[0] != max(queue):
            queue.append(queue.popleft())
            if m == 0:
                m = len(queue) -1
            else:
                m -= 1
        else:
            queue.popleft()
            count += 1
            if m == 0:
                print(count)
                break
            else:
                m -= 1
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    levels = list(map(int, input().split()))
    queue = deque()
    for i in levels:
        queue.append(i)
    printer(queue, m)