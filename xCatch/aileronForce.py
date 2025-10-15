import numpy as np
import matplotlib.pyplot as plt

surfaceArea = 128.412
p = 0.0000442708
maxSpeed = 325
V = np.linspace(0, maxSpeed, 1)
C = 1.5
F=[]
for i in V:
    F.append(0.5*surfaceArea * p * (i**2)*C)
plt.plot(V, F)
plt.show()