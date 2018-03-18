import random as rand
import matplotlib.pyplot as plt

nx = [0] # initial x value
ny = [0] # initial y value

for i in range(1, 50000): # loop 
    ri = rand.randint(0,99) # random integer

    if ri == 0:
    	x = 0
    	y = 0.16*ny[i-1]
    elif ri < 86:
    	x = 0.85*(nx[i-1])+0.04*(ny[i-1])
    	y = -0.04*(nx[i-1])+0.85*(ny[i-1]) + 1.6
    elif ri < 93:
    	x = 0.2*(nx[i-1])-0.26*(ny[i-1])
    	y = 0.23*(nx[i-1])+0.22*(ny[i-1]) + 1.6
    else:
    	x = -0.15*(nx[i-1])+0.28*(ny[i-1])
    	y = 0.26*(nx[i-1])+0.24*(ny[i-1]) + 0.44
    nx.append(x)
    ny.append(y)

plt.plot(nx, ny, ls='None', color='c', marker=',', ms=5)
plt.grid(True)
plt.show()
