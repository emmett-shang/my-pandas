fruits = {'apple': 'juicy', 'banana': 'soft'}  # Create a new dictionary with some data
print(fruits['apple'])  # Get an entry from a dictionary; prints "juicy"
print('apple' in fruits)  # Check if a dictionary has a given key; prints "True"
fruits['pear'] = 'wet'  # Set an entry in a dictionary
print(fruits['pear'])  # Prints "wet"
# print(d['monkey'])  # KeyError: 'monkey' not a key of d
print(fruits.get('mango', 'N/A'))  # Get an element with a default; prints "N/A"
print(fruits.get('pear', 'N/A'))  # Get an element with a default; prints "wet"
del fruits['pear']  # Remove an element from a dictionary
print(fruits.get('pear', 'N/A'))  # "pear" is no longer a key; prints "N/A"
                                                                                                                                        