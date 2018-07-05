import matplotlib.pyplot as plt

data = [3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10]
print(data)

plt.hist(data, bins=8, normed=False, alpha=0.6, color='g')

plt.show()
