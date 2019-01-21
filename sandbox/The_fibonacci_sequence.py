sequence = 14
n1 = 0
n2 = 1
count = 0
if sequence <= 0:
    print('Please enter a number higher than zero')
elif sequence == 1:
    print('Fibonacci sequence up to:', sequence)
    print(n1)
else:
    print('Fibonacci sequence up to:',sequence)
    while count < sequence:
        print(n1,end=' , ')
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
