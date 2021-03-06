"""

https://www.youtube.com/watch?v=PHz0lm32z_Y
"""

import matplotlib.pyplot as plt
import numpy as np


x = np.linspace( 0, 10, 20)
y_1 = x ** 2.0
y_2 = x ** 1.5
plt.loglog(x, y_1, "bo-", linewidth = 2, markersize = 10, label = "first")
plt.loglog(x, y_2, "gs-", linewidth = 2, markersize = 10, label = "second")
plt.xlabel("$X$")
plt.ylabel("$Y$")
plt.axis([-0.5, 10.5, -5, 105])
plt.legend(loc="upper left")
plt.show()
plt.savefig("myplot.pdf")
plt.savefig("myplot.png")


x = np.logspace(-1, 1, 20)
y_1 = x ** 2.0
y_2 = x ** 1.5
plt.loglog(x, y_1, "bo-", linewidth = 2, markersize = 10, label = "first")
plt.loglog(x, y_2, "gs-", linewidth = 2, markersize = 10, label = "second")
plt.xlabel("$X$")
plt.ylabel("$Y$")
plt.axis([-0.5, 10.5, -5, 105])
plt.legend(loc="upper left")
plt.show()
plt.savefig("myplot.pdf")
plt.savefig("myplot.png")