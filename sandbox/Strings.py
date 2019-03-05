
"""
https://www.youtube.com/watch?v=w0sPqKsY7Ls
HARUPRXX2016-V001900
"""


S = "python"
print(len(S))
print(S[0])
print(S[-1])
print(S[0:3])
print(S[-3])

print(S[-3:])

if "y" in S:
    print("true")
else:
    print("false")
if "Y" in S:
    print("true")
else:
    print("false")
print(12 + 12)

print("hello" + "world")

print(3 * S)
print("eight equals" + str(8))
print(dir(str))
name = "Tina Fey"
name.replace("T", "t")
new_name = name.replace("T", "t")
print(name)
print(new_name)

names = ["Tina", "Fey"]
names = name.split(" ")
print(type(names))
print(len(names))
print(names[0])
print(names[1])
print(type(names[0]))
print(names[0].upper())
print(names[1].lower())
