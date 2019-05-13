import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""
https://github.com/hadrienj/deepLearningBook-Notes/blob/master/2.8%20Singular%20Value%20Decomposition/2.8%20Singular%20Value%20Decomposition.ipynb

"""

x = np.linspace(-1, 1, 5)
y = np.sqrt(1 - (x ** 2))
plt.plot(x, y, sns.color_palette().as_hex()[0])
plt.plot(x, -y, sns.color_palette().as_hex()[0])
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.show()
