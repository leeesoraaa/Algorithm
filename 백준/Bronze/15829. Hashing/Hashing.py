n = int(input())
string = input()
total = 0
M = 1234567891
for idx, s in enumerate(string):
    hash_str = (ord(s)-96)*(31**idx%M)
    total=(total + hash_str) % M

print(total)