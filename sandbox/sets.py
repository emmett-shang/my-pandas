ids = set()
ids = set([1, 2, 4, 6, 7, 8, 9])
print(len(ids))

ids.add(10)
print(ids)
ids.add(2)
print(ids)

ids.pop()
print(ids)
ids.pop()
print(ids)
ids.pop()
print(ids)
print(len(ids))

ids = set(range(10))
print(ids)
males = set([1, 3, 5, 7])
females = ids - males
print(type(females))
print(females)
print(males)

everyone = males | females
print(everyone)
everyone & set([1, 2, 3])

word = "antidisestablishmentarianism"
letters = set(word)
print(len(letters))
