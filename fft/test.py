import math
import pydft
from pylab import plot, show

a = []
for i in range(1024):
    a.append(math.sin(2*math.pi*i/128))
#print "a = ", a
 
b = pydft.DFT(a)

#print b

plot(b)
show()
