import numpy as np
from matplotlib import pyplot as plt
n1=np.arange(0,500);
F1=250
fs1=10000
F2=200
fs2=10000
A1=1*np.cos(2*np.pi*F1/fs1*n1+np.pi/2)
A2=1*np.cos(2*np.pi*F2/fs2*n1+np.pi/2)
A3=A1+A2
plt.subplot(311)
plt.stem(n1,A1)
plt.subplot(312)
plt.stem(n1,A2)
plt.subplot(313)
plt.stem(n1,A3)
plt.show()
