from math import factorial
n, k = map(int, input().split())
c = factorial(n)//(factorial(k)*factorial(n-k))
print(c)