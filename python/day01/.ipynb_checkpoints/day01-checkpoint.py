# -*- coding: utf-8 -*-

print('hello')

# 变量
a = 100
if a >= 19:
    print(a)
else:
    print(-a)

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

'''
如果你不太确定应该用什么，%s永远起作用,它会把任何数据类型转换为字符串,
>>> 'Age: %s. Gender: %s' % (25, True)
'Age: 25. Gender: True'
'''

# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')


sum = 0
for x in range(101):
    sum = sum + x
print(sum)

L = ['Bart', 'Lisa', 'Adam']

for name in L:
    print(name)

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
a = d['Michael']
print(a)

set1 = set([1,2,3,4,1,4])
print(set1)

