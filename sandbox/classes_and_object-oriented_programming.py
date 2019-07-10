ml = [5,9,3,6,8,11,4,3]
ml.sort()
print(ml)

x = [5,2,9,11,10,2,7]
print(min(x))
print(max(x))
print(x)
x.remove(10)
print(x)


class MyList(list):
    def remove_min(self):
        self.remove(min(self))
    def remove_max(self):
        self.remove(max(self))


x = [10,3,5,1,2,7,6,4,8]
y = MyList(x)
print(dir(x))
print(dir(y))
print(x)
y.remove_min()
print(y)
y.remove_max()
print(y)