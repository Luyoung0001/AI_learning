# reduce
再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
```py
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
```