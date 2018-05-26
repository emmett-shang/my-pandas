"""
# https://www.datacamp.com/community/tutorials/python-list-comprehension
"""

# print odd numbers from 0 to 20
print("This is the odd number list from 0 to 20:")
numbers = range(0, 20)
for n in numbers:
    if n % 2 != 0:
        print(n)

# print event numbers from 30 to 50
print("This is the even number list from 30 to 50:")
numbers_E = range(30, 51)
for nE in numbers_E:
    if nE % 2 == 0:
        print(nE)
