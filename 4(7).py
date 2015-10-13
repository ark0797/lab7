import math
import pylab
import matplotlib as mlab
tmax=20
tmin=-20
dt=0.01
tlist=mlab.frange(tmin,tmax,dt)
pylab.ion
for a in range(20):
    xlist=[math.sin(t+a) for t in tlist]
    ylist=[math.cos(2*t) for t in tlist]
    pylab.plot(tlist,xlist)
    pylab.plot(tlist,ylist)
    pylab.draw()
pylab.close()

