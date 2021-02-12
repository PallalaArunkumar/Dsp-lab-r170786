import numpy as np
h=[1,2,3,4,5]
x=[1,2,3]
N1=len(h)

N2=len(x)
N=N1+N2-1
y=np.zeros(N)

for n in range(N):	
	for k in range(N):
		if n-k==N:
			break;
		y[n]=y[n]+x[n-k]*h[k]
for i in y:
	print(i)
