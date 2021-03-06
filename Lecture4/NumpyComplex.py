import numpy

def exp_prod(m,n,N):
    #defining an imaginary unit
    J=numpy.complex(0,1)
    #rest of code is real numbers
    x=numpy.arange(0,0,N)*2*J*numpy.pi/N
    return numpy.sum (numpy.exp(-1*x*m)*numpy.exp(x*n))

if __name__=='__main__':
    print (exp_prod(0,0,8))
    print (exp_prod(2,4,8))
    print (exp_prod(3,3,8))
    print (exp_prod(0,7,8)) 

