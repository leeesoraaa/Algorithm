n = int(input())
string = input()
total = 0
for idx, s in enumerate(string):
    hash_str = (ord(s)-96)*31**idx
    total+=hash_str

print(total)