"""

https://www.youtube.com/watch?v=9aMsiTBM-dk
"""

def update(n,x):
    n = 2
    x.append(4)
    print('Update: ', n, x)

def main():
    n = 1
    x = [0,1,2,3]
    print('main: ', n, x)
    update(n,x)
    print('main: ', n, x)

print(main())