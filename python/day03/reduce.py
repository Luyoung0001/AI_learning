from functools import reduce

def add(x,y):
    return x+y

l = [1,2,3,4,5,6,7,8,9]
sum = reduce(add,l)

print(sum)

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

d = char2num('123')
for each in d:
    print(each)