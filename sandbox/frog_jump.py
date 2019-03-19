
"""
Frog jump

"""

num_of_jumps = 53


a = 1/2.0

destination = 0

next_step = a
for i in range(0, num_of_jumps):
    print(next_step)
    destination = destination + next_step
    next_step = next_step / 2.0

print("where am I:")
print(destination)

print("how far am I from the destination pond:")
print(1 - destination)





