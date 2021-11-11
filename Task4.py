import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

x = np.linspace(0, 1, num=10)
y = np.sin(2*np.pi*x)

inter_y = interp1d(x, y, kind="cubic")

xnew = np.linspace(0, 1, num=50)
ynew = inter_y(xnew)

plt.plot(x, y, 'r', xnew, ynew, 'k')
plt.show()
