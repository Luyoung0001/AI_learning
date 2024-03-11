from collections.abc import Iterator
from collections.abc import Iterable
def f(x):
    return x*x

r = map(f,range(1,10))
l = list(r)

for item in l:
    print(item)

print(isinstance(r,Iterator))
print(isinstance(r,Iterable))
