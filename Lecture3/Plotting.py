import numpy
from matplotlib import pyplot as plt

#plotting sin
x = numpy.arange(0,30,0.1)
y = numpy.sin(x)

plt.plot(x,y)
plt.show()
