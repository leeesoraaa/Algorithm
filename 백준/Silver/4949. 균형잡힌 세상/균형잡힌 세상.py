import sys

while True:
    line = sys.stdin.readline().rstrip()
    if line == '.':
        break

    stack = []
    
    for char in line:
        if char in '([':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                print('no')
                break
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                print('no')
                break
            stack.pop()
        elif char == '.' and stack:
            print('no')
            break
    
    else:
        print('yes')