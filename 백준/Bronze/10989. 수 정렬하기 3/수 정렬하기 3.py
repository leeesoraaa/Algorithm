import sys
input = sys.stdin.readline
print = sys.stdout.write
count = [0]*10001
n = int(input())
for _ in range(n):
    num = int(input())
    count[num]+=1

for i in range(1, 10001):
    for _ in range(count[i]):
         print(str(i) + "\n")