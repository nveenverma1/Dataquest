## 3. Differentiation ##

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 6, 110)
y = -(2*x) + 3
plt.plot(x, y)
plt.show()


## 6. Power Rule ##

slope_one = 5*(2**4)
slope_two = 9*(0**8)

## 7. Linearity Of Differentiation ##

x3 = 1
fx3 = (x3**5) - x3
slope_three = 5*(x3**4) - 1

x4 = 2
fx4 = (x4**3) - (x4**2)
slope_four = 3*(x4**2) - 2*x4

print(slope_three)
print(slope_four)

## 8. Practicing Finding Extreme Values ##

critical_points = [0, 1]
rel_min = [2/3]
rel_max = [0]

