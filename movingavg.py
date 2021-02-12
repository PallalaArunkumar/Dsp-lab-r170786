import numpy as np
from matplotlib import pyplot as plt

y=np.random.rand(10)
z=np.zeros(len(y))

m=int(input("the order:"))

for n in range(0,len(y)):
	s=0
	for k in range(0,m):
		if n-k>=0:
			s=s+y[n-k]
	z[n]=s/m
plt.subplot(211)
plt.stem(y)
plt.subplot(212)
plt.stem(z)
plt.show()

