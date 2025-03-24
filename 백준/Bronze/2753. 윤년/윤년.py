year = int(input())
def what(year):
    if year % 4==0 and year%100 != 0:
        return 1
    elif year % 400 == 0:
        return 1
    else:
        return 0
    
print(what(year))