import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(size = 1000)
plt.hist(x);
plt.show()
plt.hist(x, normed = True);
plt.show()
plt.hist(x, normed = True, bins = np.linspace(-5, 5, 21 ));
plt.show()


