import numpy as np
"""

https://www.youtube.com/watch?v=QicQZfx2CRk
"""

z1 = np.array([1,3,5,7,9])
z2 = z1 + 1
print(z2)
ind = [0,2,3]
print(z1[ind])
ind = np.array([0,2,3])
print(z1[ind])
print(z1 > 6)
print(z1[z1 > 6]) #prints numbers in the array z1 that are greater than 6
print(z2[z1 > 6]) #Index vector is still identifying those elements of z1 that happen to be greater than 6, but in this case, however, this line is using the vector to access the element in the array, z2
print(z2[z2 > 6])
ind = z1 > 6
print(ind)
print(z1[ind])
print(z2[ind])
z1 = np.array([1,3,5,7,9])
w = z1[0:3]
print(w)
w[0] = 3
print(w)
print(z1)
z1 = np.array([1,3,5,7,9])
ind = np.array([0,1,2])
W = z1[ind]
W[0] = 3
print(W)
print(z1)
