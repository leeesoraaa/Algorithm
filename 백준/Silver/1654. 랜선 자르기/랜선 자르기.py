# 랜선 자르기
import sys
input = sys.stdin.readline
k, n = map(int, input().split())
k_list = [int(input()) for _ in range(k)]

# 가장 긴 랜선의 중간값으로 몇개 만들 수 있는지
## n보다 많이 만들 수 있으면 중간값보다 크게 자르기
## n보다 적으면 중간값보다 작게

start = 1
end = max(k_list)
answer = 0

while start <= end:
    mid = (start + end) // 2
    count = sum(line // mid for line in k_list)
    
    if count >= n:
        answer = mid
        start = mid + 1
    else:
        end = mid -1

print(answer)