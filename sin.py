import numpy as np
from matplotlib import pyplot as plt
n=np.arange(0,500)
F= 250
f=10000
s=0.5*np.cos(2*np.pi*F/f*n+np.pi/2)
plt.subplot(2,2,1);
plt.stem(n,s)
plt.show()
plt.subplot(2,2,2)
plt.plot(n,s)
plt.show()
