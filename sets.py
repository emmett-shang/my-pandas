animals = {'cat', 'dog'}
print('cat' in animals)  # Check if an element is in a set; prints "True"
print('fish' in animals)  # prints "False"
animals.add('fish')  # Add an element to a set
print('fish' in animals)  # Prints "True"
print(len(animals))  # Number of elements in a set; prints "3"
animals.add('cat')  # Adding an element that is already in the set does nothing
print(len(animals))  # Prints "3"
animals.remove('cat')  # Remove an element from a set
print(len(animals))  # Prints "2"

animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))
# Prints "#1: fish", "#2: dog", "#3: cat"

book_series = {'Sherlock Holmes', 'Foundation', 'Harry Potter', 'Tintin', 'Asterix'}
print('Sherlock Holmes' in book_series)
print('Diary of a wimpy kid' in book_series)
book_series.add('Diary of a wimpy kid')
print('Diary of a wimpy kid' in book_series)
print(len(book_series))
book_series.add('Foundation')
print(len(book_series))
book_series.remove('Harry Potter')
print(len(book_series))

book_series = {'Sherlock Holmes', 'Foundation', 'Harry Potter', 'Tintin', 'Asterix', 'Diary of a wimpy kid'}
for idy, book_series in enumerate(book_series):
    print('#%d : %s' % (idy + 1, book_series))
