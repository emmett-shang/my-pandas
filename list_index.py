random = ['Messi','Pele','Maradona','Ronaldinho','Ronaldo']
index = random.index('Messi')
print("The index of Messi is:", index)

random.append('Zidane')
print('Updated animal list: ', random)

random_2 = ['Modric', 'Griezemann', 'Neymar ', 'Salah', 'Suarez', 'Sanchez']

random.extend(random_2)
print('random list:', random)
