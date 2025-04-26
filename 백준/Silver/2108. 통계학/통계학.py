# 통계학
#1. 산술평균
#2. 중앙값
#3. 최빈값
#4. 범위

import sys
import statistics
from collections import Counter
input = sys.stdin.readline
n = int(input())
numbers = [int(input()) for _ in range(n)]
counter = Counter(numbers)
max_counter = max(counter.values())
modes = [key for key, count in counter.items() if count == max_counter]
if len(modes) > 1:
    modes.sort()
    mode = modes[1]
else:
    mode = modes[0]

print(round(sum(numbers)/len(numbers)))
print(statistics.median(numbers))
print(mode)
print(max(numbers) - min(numbers))
