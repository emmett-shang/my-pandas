import numpy as np
"""
http://cs231n.github.io/python-numpy-tutorial/

"""
x = np.array([
    [1, 2],
    [3, 4]
], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)

print(x)
print(y)

# Elementwise sum; both produce the array
# [[ 6.0  8.0]
#  [10.0 12.0]]
print(x + y)
print(np.add(x, y))

# Elementwise difference; both produce the array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print(x - y)
print(np.subtract(x, y))

# Elementwise product; both produce the array
# [[ 5.0 12.0]
#  [21.0 32.0]]
print(x * y)
print(np.multiply(x, y))

# Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print(x / y)
print(np.divide(x, y))

# Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print(np.sqrt(x))

# -------------
a = np.array([
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7]
], dtype=np.float64)

b = np.array([
    [5, 6, 7],
    [7, 8, 9],
    [8, 9, 10]
], dtype=np.float64)

print(a + b)
print(np.add(a, b))

print(a - b)
print(np.subtract(a, b))

print(a * b)
print(np.multiply(a, b))

print(a / b)
print(np.divide(a, b))

print(np.sqrt(a))
print(np.sqrt(b))
