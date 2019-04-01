l1 = [2,3,4]
print(l1)
l2 = l1
print(l2)
l1[0] = 24
print(l1)
l = [1,2,3]
m = [1,2,3]
if l == m:
    print("True")
else:
    print("False")

if l is m:
    print("True")
else:
    print("False")

print(id(l))
print(id(m))
L = [1,2,3]
M = L
M = list(L)
if M is L:
    print("True")
else:
    print("False")

if M == L:
    print("True")
else:
    print("False")
M = L[:]
print(M)
