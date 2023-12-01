def solution(n):
    answer = 0
    b = bin(n)[2:]
    a = b.count('1')
    for i in range(n+1, n+100):
        if bin(i)[2:].count('1') == a:
            answer = i
            break
    return answer