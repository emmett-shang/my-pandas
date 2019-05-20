filename = "input.txt"
for line in open(filename):
    print(line)

for line in open(filename):
    line = line.rstrip()
    print(line)

for line in open(filename):
    line = line.rstrip().split(" ")
    print(line)

f = open("input.txt", "w")
f.write("Python\n")
f.close()