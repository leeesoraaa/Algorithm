def solution(x, y, n):

    a = [1100000] * 1000001
    a[x] = 0

    for i in range(x, y + 1):
        if i+n<=y:
            a[i + n] = min(a[i + n], a[i] + 1)
        if i*2<=y:
            a[i * 2] = min(a[i * 2], a[i] + 1)
        if i*3<=y:
            a[i * 3] = min(a[i * 3], a[i] + 1)

    if a[y] == 1100000:
        return -1
    else:
        return a[y]