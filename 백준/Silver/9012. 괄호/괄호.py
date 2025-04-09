import sys
n = int(input())

for _ in range(n):
    stack = []
    line = sys.stdin.readline()
    vps = True
    for char in line:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                vps = False
                break
            stack.pop()
    if stack:
        vps = False

    print('YES' if vps else 'NO')    