n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())
tshirt = 0
for s in size:
    if s%t == 0:
        tshirt += s//t
    else:
        tshirt += (s//t) +1
print(tshirt)
print(n//p, n%p)