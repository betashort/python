import math
import numpy as np
import matplotlib.pyplot as plt

def gauss(x):
    return 1/(math.sqrt(2*math.pi))*np.exp((-x**2)/2)

x = np.arange(-5.0, 5.0, 0.1)
y = gauss(x)

plt.plot(x, y, label = "Gauss")
plt.xlabel("x")
plt.ylabel("y")
plt.ylim(-0.01, 0.5)
plt.title("Gaussian distribution")
plt.show()