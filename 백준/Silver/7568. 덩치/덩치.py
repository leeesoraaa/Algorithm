import sys
input = sys.stdin.readline
n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]
# 키와 몸무게가 다 커야만 덩치가 큰 것
# 나보다 덩치가 큰 사람의 명수 + 1 = 내 등수
ranks = []
for i in range(n):
    rank=1
    for j in range(n):
        if i != j:
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                rank += 1
    
    ranks.append(rank)

print(*ranks)