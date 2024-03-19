import numpy as np
x = np.random.randint(100,size=(5,))
print(x)
x = np.random.randint(100,size=(5,6))
print(x)
x = np.random.rand(5)
print(x)

x = np.random.rand(3, 5)
print(x)

x = np.random.choice([3,5,7,9])
print(x)

x = np.random.choice([3, 5, 7, 9], size=(3, 5))
print(x)