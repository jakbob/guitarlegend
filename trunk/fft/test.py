import math
import pydft
import pylab

a = []
for i in range(128):
    a.append(math.sin(2*math.pi*i/128))

b = pydft.DFT(a)

print b

pylab.plot(b)
pylab.show()
