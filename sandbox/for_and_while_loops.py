for i in range(0, 10):
    print(i)

names = ['Jim', 'Tom', "Nick", "Pam", "Sam", "Tim"]
for name in names:
    print(name)

for i in range(len(names)):
    print(names[i])

age = {"Jim":"31", "Nick": "31", "Pam": "27", "Sam": "35", "Tim": "31", "Tom": "50"}
print(age)

print(age.keys())

for name in age.keys():
    print(name, age[name])

for name in age:
    print(name, age[name])

for name in sorted(age.keys()):
    print(name, age[name])

for name in sorted(age.keys(), reverse=True):
    print(name, age[name])