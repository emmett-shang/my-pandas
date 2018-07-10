import matplotlib.pyplot as plt
import random

data = [3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10]
print(data)

plt.hist(data, bins=8, normed=False, alpha=0.6, color='g')

plt.show()

# --------------
# coin toss game
# --------------
# Head: 1Frequency Histogram.py:18
# Tail: 0


coin_toss = []

for i in range(50000):
    toss = random.randint(0, 1)
    coin_toss.append(toss)
    print(toss)

plt.hist(coin_toss, bins=10, alpha=0.5, normed=False, color='y', range=[0, 1], align='left')

plt.show()
