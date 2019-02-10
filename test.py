import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10)
y = np.sin(x)

plt.plot(x,y, "r--")
plt.show()