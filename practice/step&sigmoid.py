import numpy as np
import matplotlib.pylab as plt

#ステップ関数
def step_function(x):
    return np.array(x > 0, dtype = np.int)

#シグモイド関数
def sigmoid(x):
    return 1 / (1+np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y_step = step_function(x)
y_sigmoid = sigmoid(x)

#グラフの生成
plt.plot(x, y_step, linestyle = "--", label = "step")
plt.plot(x, y_sigmoid, label = "sigmoid")
plt.ylim(-0.1, 1.1)
plt.xlabel("x")
plt.ylabel("y")
plt.title('step & sigmoid')
plt.legend()
plt.show()