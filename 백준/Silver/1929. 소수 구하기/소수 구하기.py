# 소수 구하기
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

sosu = [True] * (b+1)
sosu[0:2] = [False, False]

for i in range(2, int(b**0.5) + 1):
    if sosu[i]:
        for j in range(i*i, b+1, i):
            sosu[j] = False

for i in range(a, b+1):
    if sosu[i]:
        print(i)