n = int(input())

if n >= 5:
    count0 = n//5 + n//25 + n//125
else:
    count0=0

print(count0)