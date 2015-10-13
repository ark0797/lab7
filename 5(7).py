import matplotlib.pyplot as plt
import numpy as np
def building_function(x,t):
    y=eval(t)
    return(y)
function=input()
x=np.arange(-20,20,0.1)
y=[building_function(_x,function) for _x in x]
plt.xkcd()
plt.plot(x,y)
plt.show()

