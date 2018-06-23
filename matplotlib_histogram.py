import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

"""

matplotlib_histogram.py:5
"""
x = [3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10]
num_bins = 8
n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='blue', alpha=0.5)
plt.xlabel('amount of vertices of the polygons')
plt.ylabel('frequency of polygons vertices')
plt.title('Histogram polygon vertices')
y = mlab.normpdf(bins, 6.5, 1)
plt.plot(bins, y, 'r--.')
plt.show()
