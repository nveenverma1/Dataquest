## 2. ReLU Activation Function ##

# import matplotlib.pyplot as plt
# %matplotlib inline

# import numpy as np
# x = np.linspace(-2, 2, 20)

# def relu(x):
#     return x

# relu_y = relu(x)
# print(x)
# print(relu_y)

# plt.plot(x, relu_y)

import matplotlib.pyplot as plt
# %matplotlib inline

import numpy as np
x = np.linspace(-2, 2, 20)
def relu(values):
    return np.maximum(values, 0)

relu_y = relu(x)

print(x)
print(relu_y)

plt.plot(x, relu_y)

## 3. Trigonometric Functions ##

x = np.linspace(-2*np.pi, 2*np.pi, 100)

tan_y = numpy.tan(x)

print(x)
print(tan_y)

plt.plot(x, tan_y)
plt.show()

## 5. Hyperbolic Tangent Function ##

x = np.linspace(-40, 40, 100)

def tanh_y(x):
    return np.tanh(x)

tanh_y = tanh_y(x)
print(x)
print(tanh_y)

plt.plot(x, tanh_y)
plt.show()