import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0,x)

x = np.array([-1.0, 1.0, 2.0])
result = sigmoid(x)
print(result)

t = np.array([1.0, 2.0, 3.0])
print(1.0 + t)
print(1.0 / t)

#그래프로 출력
x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()

y = relu(x)
plt.plot(x, y)
plt.xlim(-5.0, 5.0)
plt.ylim(-1.0, 5.0)
plt.show()
