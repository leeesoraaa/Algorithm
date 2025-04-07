import sys
input = sys.stdin.readline
n = int(input())
people = []
for i in range(n):
    age, name = input().split()
    people.append((int(age), name, i))
people.sort(key=lambda x : (x[0], x[2]))

for p in people:
    print(f'{p[0]} {p[1]}')