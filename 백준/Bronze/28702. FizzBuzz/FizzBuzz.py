def fizzbuzz(x):
    if x % 15 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return str(x)
a=input()
b=input()
c=input()
sequence=[a,b,c]
if sequence[0].isdigit():
    start = int(sequence[0])
elif sequence[1].isdigit():
    start = int(sequence[1])-1
else:
    start = int(sequence[2])-2

for i in range(3):
    if fizzbuzz(start+i) != sequence[i]:
        break
else:
    print(fizzbuzz(start + 3))