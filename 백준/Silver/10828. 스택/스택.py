# 스택
import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    cmd = input().strip()
    if cmd.startswith("push"):
        x = int(cmd.split()[1])
        stack.append(x)
    elif cmd == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif cmd == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    elif cmd == 'size':
        print(len(stack))
