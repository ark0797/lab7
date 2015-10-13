import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-60,60.01,0.5)
plt.plot(x,(np.exp**((x**2+1)*np.exp**(-abs(x)/10))/(np.exp**(1+np.tg(1/(1+np.sin(x)**2))))
plt.show()
