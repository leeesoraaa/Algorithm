def solution(price, money, count):
    total = 0
    for c in range(1, count+1):
        total += price * c
    if total > money:
        answer = total - money
    else:
        answer = 0
    return answer