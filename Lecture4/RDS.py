import numpy
x=numpy.random.randn(8)
xft=numpy.fft.fft(x)
for xx in xft:
    print (xx)

