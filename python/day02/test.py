from collections.abc import Iterable

a = isinstance("abc",Iterable)
print(a)

for i, ch in enumerate("hello"):
    print(i,ch)

