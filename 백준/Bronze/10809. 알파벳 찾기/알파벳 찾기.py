a = [-1] * 26
s = input()
for i in s:
    t = ord(i) - 97 # ord(i): 아스키코드 정수
    if a[t] == -1: # a[t]: 해당 알파벳의 인덱스 위치
        a[t] = s.index(i)
print(*a) # a의 원소를 공백으로 구분해 한 줄에 출력