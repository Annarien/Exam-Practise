import numpy
from matplotlib import pyplot as plt
import FunctionsInPython

x=numpy.arange(-1,1,0.002)
y=FunctionsInPython.mygauss(x,cent=0.5,sig=0.05)
gg=FunctionsInPython.mygauss
y2=gg(x,cent=0.5,sig=0.05)
delt=numpy.abs(y2-y)
print("Error is "+repr(delt.sum()))
plt.plot(x,y,'r')
plt.show()