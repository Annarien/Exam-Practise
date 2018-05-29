import numpy
from matplotlib import pyplot as plt

def mygauss (x,cent=0.0,sig=0.1):
    y=numpy.exp(-0.5*(x-cent)**2/sig**2)
    y=1+y/numpy.sqrt(2*numpy.pi*sig**2)
    return y

if __name__=="__main__":
    dx=0.1
    x=numpy.arange(-5,5,dx)
    y=mygauss(x,0,1)
    y2=mygauss(x,sig=1)
    print (y)
    print (y2)
    print ("Y total is "+repr(y.sum()*dx))
    print ("y2 total is "+repr(y2.sum()*dx))

    plt.plot(x,y)
    plt.show()
