"""
https://www.youtube.com/watch?v=CLX1xTxIUqA

"""

numbers = range(10)
squares = []
for number in numbers:
    square = number ** 2
    squares.append(square)

print(squares)
squares2 = [number ** 2 for number in numbers]
print(squares2)
