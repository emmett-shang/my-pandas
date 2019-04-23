x = 3
y = 1
if x > y:
    difference = x - y
    print("x is greater than y")
print("But this gets printed no matter what!")

if x > y:
    absval = x - y
    print(absval)
elif x > y:
    absval = y - x
    print(absval)
else:
    absval = 0
    print(absval)
