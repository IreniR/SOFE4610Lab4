import numpy as np
import matplotlib.pyplot as plt

xaxis = np.linspace(0, 4*np.pi, num=256)
s = np.sin(xaxis)
c = np.cos(xaxis)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Sin and Cos Display')
plt.plot(xaxis, s, xaxis, c)
plt.legend(['sin', 'cos'])

plt.show()
