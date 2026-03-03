from matplotlib import pyplot as plt
import math
import random
import numpy as np
import time

n = 1000

phi = np.random.uniform(0., 2* math.pi, size = n)
x = np.sin(phi).cumsum()
y = np.cos(phi).cumsum()

# x=[0.]
# y=[0.]

# for i in range(n):
#     phi = random.uniform(0., 2 * math.pi)
#     x.append(x[-1] + math.sin(phi))
#     y.append(y[-1] + math.cos(phi))

plt.figure()
plt.plot(x, y)
plt.gca().set_aspect("equal")
plt.show()    


