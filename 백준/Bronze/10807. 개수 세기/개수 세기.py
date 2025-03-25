import sys

n = int(sys.stdin.readline())
a=list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())
answer = 0
for i in a:
    if i == v:
        answer +=1

print(answer)