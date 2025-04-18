# solved.ac
# 절사평균
## 1. n 의 15 % 계산 (반올림)
## 2. 정렬 후 양 끝 15% 씩 제외
## 3. 나머지의 평균 계산 (반올림)

import sys
import math
input = sys.stdin.readline
n = int(input())
if n == 0:
    print(0)
else:
    k = math.floor(n*0.15 + 0.5)

    levels = list(int(input().strip()) for _ in range(n))
    levels.sort()
    trimmed = levels[k:n-k]
    answer = sum(trimmed)/len(trimmed)
    print(math.floor(answer+0.5))
    # round(): 0.5 인 경우 가장 가까운 짝수로 반환 
    # math.floot(i + 0.5) 를 사용하는 것이이 일반적 반올림림