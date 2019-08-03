import numpy as np


x = np.array([1, 3, 5])
y = np.array([2, 4, 6])
X = np.array([[1, 2, 3], [4, 5, 6]])
Y = np.array([[2, 4, 6], [8, 10, 12]])


print(x[2])
print(x[0:2])
z = x + y
print(z)

print(X[:, 1]) #second column
print(Y[:, 1])
print(X[:, 1] + Y[:, 1])
print(X[1,:])  #second row
print(X[1,:])
print(X[1,:] + Y[1,:])
print(X[1])  #second row as well
print([2, 4] + [6, 8])
print(np.array([2, 4]) + np.array([6, 8]))