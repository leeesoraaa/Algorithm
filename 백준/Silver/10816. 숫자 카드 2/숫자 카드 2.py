import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
n_count = Counter(n_list)
result = [str(n_count[num]) for num in m_list]

print(' '.join(result))