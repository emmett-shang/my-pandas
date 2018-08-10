from random import *
from math import sqrt

inside = 0
n = 50000000
for i in range(0, n):
    x = random()
    y = random()
    if sqrt(float(x * x + y * y)) <= 1:
        inside += 1
pi = 4.0 * inside / n
print pi
