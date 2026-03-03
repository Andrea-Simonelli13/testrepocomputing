import math

import numpy as np
from matplotlib import pyplot as plt

n = 1000

rng = np.random.default_rng()  # crea un generatore moderno

phi = rng.uniform(0., 2 * math.pi, size=n)
#phi = np.random.uniform(0., 2* math.pi, size = n)
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


