import string
s = str(input())
alphabet = list(string.ascii_lowercase)
for alpha in alphabet:
    count = s.index(alpha) if alpha in s else -1
    print(count, end=' ')