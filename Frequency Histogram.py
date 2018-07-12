import matplotlib.pyplot as plt
import numpy as np
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

frac = 0.5
coin_toss = np.random.binomial(1, frac, size=50000)

plt.hist(coin_toss, bins=10, alpha=0.5, normed=False, color='y', range=[0, 1], align='left')

plt.show()
