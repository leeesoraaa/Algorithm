t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    y=n%h
    x=(n//h) +1
    if y == 0:
        y = h
        x = n // h
    print(f"{y}{x:02}")