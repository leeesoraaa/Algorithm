def solution(arr):
    answer = []
    if len(arr) == 1:
        answer = [-1]
    else:
        minnum = min(arr)
        for i in arr:
            if i != minnum:
                answer.append(i)
    return answer