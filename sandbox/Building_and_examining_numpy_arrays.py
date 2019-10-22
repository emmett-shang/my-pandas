import numpy as np

x = np.linspace(0, 100, 10)
print(x)

y = np.logspace(1, 2, 10) # The integers must be the log of a certain number
print(y)

a = np.logspace(np.log10(250), np.log10(500), 10)
print(a)

X = np.array([[1,2,3], [4,5,6]])
print(X.shape)
print(X.size)

Y = np.random.random(10)
print(Y)
print(np.any(Y > 0.9))
print(np.all(Y >= 0.1))