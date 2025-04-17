# 요세푸스 문제 0
## 큐를 이용해 푼다!
from collections import deque

n, k = map(int,input().split())
queue = deque(range(1, n+1))
answer = []
while queue:
    queue.rotate(-(k-1)) # 왼쪽으로 k-1칸 돌림
    answer.append(queue.popleft()) # k번째 제거거

print('<' + ', '.join(map(str, answer)) + '>')