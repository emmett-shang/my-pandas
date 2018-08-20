random = ['Messi','Pele','Maradona','Ronaldinho','Ronaldo']
index = random.index('Messi')
print("The index of Messi is:", index)

random.append('Zidane')
print('Updated list: ', random)

random_2 = ['Modric', 'Griezemann', 'Neymar ', 'Salah', 'Suarez','Kane', 'Hazard']

random.extend(random_2)
print('random list:', random)

random.insert(7, 'Sanchez')
print('Updated', random)

random.remove('Kane')
print('Updated list', random)

count = random.count('Ronaldinho')
print('The count of Ronaldinho is:', count)
count = random.count('Cavani')
print('The count of Cavani is:', count)

Return_name = random.pop(12)
print('Updated list:', random)


