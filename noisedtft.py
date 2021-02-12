import numpy as np
from matplotlib import pyplot as plt

w=np.arange(-1*np.pi,np.pi,0.01*np.pi)
j=(-1)**0.5
y=[]
f=250
fs=500
x=np.random.rand(100)
for i in range(0,len(w)):
	s=0
	for n in range(0,len(x)):
		s=s+(x[n]*np.exp(-1*j*w[i]*n))
	y.append(s)

plt.subplot(211)
plt.plot(w,np.abs(y))
plt.subplot(212)
plt.plot(w,np.angle(y))
plt.show()
