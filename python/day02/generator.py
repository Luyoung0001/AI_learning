g = (x*x for x in range(1,100))
print(type(g))
for gg in g:
    print(next(g))