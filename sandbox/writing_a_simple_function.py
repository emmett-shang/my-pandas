import random


def intersect(s1, s2):
    res = []
    for i in s1:
        if i in s2:
            res.append(i)
    return res


result = intersect([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])
print(intersect([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))


def password(length):
    pw = str()
    characters = "abcdefghijklmnopqrstuvwxyz" + "0123456789"
    for i in range(length):
        pw = pw + random.choice(characters)
    return pw


print(password(4))
print(password(8))
print(password(10))
print(password(50))


def do_rsum(n):
    rsum = 0
    for k in range(n):
        rsum += k # rsum = rsum + k
    return rsum


print(do_rsum(5))

def monkey(n):
    rsum = 0
    for i in range(n):
        rsum += i
    return rsum

print(monkey(10))